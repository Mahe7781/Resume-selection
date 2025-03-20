
# Resume Screening System with Machine Learning and Node.js Integration

## 🔍 Overview
This project is a hybrid resume parsing system using:
- **Python ML (Random Forest)** for intelligent resume scoring.
- **Node.js + Express.js** backend for API handling.
- **MySQL** for data storage.
- **HTML frontend** dashboard to visualize parsed resumes.

---

## 📂 Project Structure
```
├── python/
│   ├── resume_parser.py       # ML resume parser + DB insertion
│   ├── ml_model.pkl           # Trained Random Forest model
│   ├── vectorizer.pkl         # Vectorizer for skills
│   └── resumes/               # Folder for uploaded resumes
│
├── nodejs-backend/
│   ├── app.js                 # Node.js Express backend
│   ├── routes/
│   │   └── resume.js          # API endpoint to trigger resume_parser.py
│   └── package-lock.json
│
├── frontend/
│   ├── index.html             # Resume Selection Dashboard
│   └── styles.css, script.js  # UI styling and logic
```

---

## ⚙ Technology Stack
- Python 3.11+
- Scikit-learn, NLTK, PDFMiner, Joblib
- Node.js + Express.js
- MySQL Database
- HTML, CSS, JS (Frontend)

---

## 🔧 Setup Instructions

### ✅ Python Setup
Install dependencies:
```bash
pip install nltk pdfminer.six mysql-connector-python scikit-learn joblib
```

Download NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

Create MySQL database:
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

Test parser manually:
```bash
python python/resume_parser.py
```

---

### ✅ Node.js Setup
Install dependencies:
```bash
npm install
```

Trigger Python parsing from Node.js (in `resume.js`):
```js
const { exec } = require('child_process');
exec('python ../python/resume_parser.py', ...);
```

Start Node.js server:
```bash
node app.js
```

---

### ✅ Frontend Dashboard
Open `index.html` to view and filter parsed resumes from MySQL database.

---

## ✨ Future Enhancements
- ML job-role classification
- REST API to upload and score resumes dynamically
- Advanced analytics dashboard

---

## 📬 Contact
For questions or collaboration, feel free to connect!
