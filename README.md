### 🔍 Overview
This project is an intelligent resume parser and scoring system that uses Natural Language Processing (NLP) and Machine Learning (Random Forest) to:
- Extract relevant information from PDF resumes (email, phone, skills).
- Score candidates based on their skills using a trained ML model.
- Store parsed and scored data into a MySQL database.

---

### ⚙ Technologies Used
- **Python**
- **NLTK** - Tokenization and Stopword Removal
- **PDFMiner.six** - Text extraction from PDF resumes
- **MySQL Connector** - Database operations
- **Scikit-Learn** - Random Forest Classifier for resume scoring
- **Joblib** - Model and vectorizer persistence

---

### 📁 Project Structure
```
├── resume_parser.py      # Main code file with ML-based resume parser
├── ml_model.pkl          # Trained Random Forest model (auto-generated)
├── vectorizer.pkl        # Vectorizer used for scoring resumes (auto-generated)
├── resumes/              # Folder to place PDF resumes
└── README.md             # Project description and setup guide
```

---

### 💡 Features
- Smart resume parsing using NLP.
- Resume scoring powered by a Random Forest model trained on labeled skill sets.
- Minimal effort needed to retrain and improve accuracy.
- Auto-creation of `ml_model.pkl` and `vectorizer.pkl` if not found.
- MySQL database integration for storage and analysis.

---

### 🔧 How to Run

#### 1. Install Required Packages
```bash
pip install nltk pdfminer.six mysql-connector-python scikit-learn joblib
```

#### 2. One-Time NLTK Setup
These will auto-download, but you can also run manually:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

#### 3. Setup MySQL
Make sure you have a MySQL database and table created:
```sql
CREATE DATABASE resume_db;

CREATE TABLE resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255),
    phone VARCHAR(50),
    skills TEXT,
    score INT,
    job_role VARCHAR(100)
);
```

#### 4. Add PDF Resumes
Put your resumes in the `resumes/` folder.

#### 5. Run the Script

-python resume_parser.py


### 📈 Improving Accuracy
You can modify the `train_ml_model()` function in the script to include more training samples and better labels for improved model performance.
