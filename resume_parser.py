import os
import re
import nltk
import mysql.connector
import joblib
from pdfminer.high_level import extract_text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer

# Download NLTK requirements
nltk.download('punkt')
nltk.download('stopwords')

# ------------------------------
# ML TRAINING SECTION (one-time setup, extendable)
def train_ml_model():
    data = [
        {"skills": "python django flask mysql", "label": 1},
        {"skills": "html css javascript react", "label": 0},
        {"skills": "python api rest nlp mysql", "label": 1},
        {"skills": "react node.js html css", "label": 0},
        {"skills": "python flask django rest", "label": 1},
    ]
    texts = [d["skills"] for d in data]
    labels = [d["label"] for d in data]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    y = labels

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "ml_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("✅ ML model trained and saved.")

# Train the model if not present
if not os.path.exists("ml_model.pkl") or not os.path.exists("vectorizer.pkl"):
    train_ml_model()

# Load trained model and vectorizer
ml_model = joblib.load("ml_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# ------------------------------
# Resume Parsing Section
ROLE_KEYWORDS = {
    "python_developer": ["python", "django", "flask", "mysql", "api", "rest", "nlp"],
    "web_developer": ["html", "css", "javascript", "node.js", "express", "react", "api"]
}

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_email(text):
    return re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)

def extract_phone(text):
    return re.findall(r'\+?\d[\d\-]{8,15}', text)

def extract_skills(text):
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [w for w in words if w.isalpha() and w not in stop_words]
    return filtered_words

def score_resume_ml(skills):
    skill_text = " ".join(skills)
    vectorized_input = vectorizer.transform([skill_text])
    score = ml_model.predict(vectorized_input)[0]
    return score

def parse_resume(file_path, job_role):
    text = extract_text_from_pdf(file_path)
    email = extract_email(text)
    phone = extract_phone(text)
    skills = extract_skills(text)
    score = score_resume_ml(skills)

    return {
        "email": email[0] if email else "",
        "phone": phone[0] if phone else "",
        "skills": list(set(skills)),
        "score": score
    }

def save_to_db(data, job_role):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="3012",
            database="resume_db"
        )
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO resumes (email, phone, skills, score, job_role)
            VALUES (%s, %s, %s, %s, %s)
        """, (data['email'], data['phone'], ', '.join(data['skills']), int(data['score']), job_role))
        conn.commit()
        print(f"✅ Saved to DB: {data['email']} ({job_role})")
    except mysql.connector.Error as err:
        print(f"❌ DB Error: {err}")
    finally:
        if conn.is_connected():
            conn.close()

def process_folder(folder_path, job_role):
    if not os.path.exists(folder_path):
        print(f"⚠ Folder '{folder_path}' does not exist. Creating it now...")
        os.makedirs(folder_path)
        print("📂 Place your PDF resumes in this folder and run again.")
        return

    files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]
    if not files:
        print("⚠ No PDF files found in the folder.")
        return

    for file in files:
        file_path = os.path.join(folder_path, file)
        result = parse_resume(file_path, job_role)
        save_to_db(result, job_role)
        print(f"✔ Parsed and stored: {file}")

# Entry point
if __name__ == "__main__":
    process_folder("resumes", "python_developer")
