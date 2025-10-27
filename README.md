# 🧠 AI Resume Ranker

AI Resume Ranker is a smart web application that ranks resumes against a given job description using NLP (Natural Language Processing) and AI scoring.  
It evaluates resumes based on **keyword relevance, TF-IDF similarity**, and **semantic matching** to give recruiters an instant shortlist.

---

## 🚀 Features

- 🔍 **Automatic Resume Screening** — Upload multiple resumes and compare them to a job description.
- 🤖 **AI-Powered Scoring** — Combines keyword, TF-IDF, and semantic similarity for accurate ranking.
- 📊 **Detailed Reports** — Generates PDF reports showing candidate strengths and weaknesses.
- 🐳 **Docker Support** — Easily run the app inside a Docker container.
- 💾 **Web Interface** — Clean UI built using Flask, HTML, and TailwindCSS.

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend | Python (Flask) |
| NLP & AI | spaCy, scikit-learn, TF-IDF |
| Frontend | HTML, CSS, JS |
| Containerization | Docker & Docker Compose |
| Reports | FPDF / ReportLab |

---

## 📁 Project Structure

Resume_Ranker/
│
├── app.py # Flask app entry point
├── ranker.py # Core AI logic for resume scoring
├── requirements.txt # Python dependencies
├── Dockerfile # Docker setup
├── docker-compose.yml # Compose configuration
│
├── templates/ # HTML files (Flask templates)
│ ├── index.html
│ └── results.html
│
├── static/ # CSS/JS/Images
│ └── styles.css
│
├── resumes/ # Uploaded resumes
│
├── uploads/ # Temporary uploads
│
└── Reports/ # Generated PDF reports


---

## ⚙️ Installation

### 🧮 1. Clone the Repository
```bash
git clone https://github.com/rajveer100704/AI_Resume_Ranker.git
cd AI_Resume_Ranker

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

docker-compose up --build

---

Usage

Upload one or more resumes (.pdf / .docx).

Paste the job description in the text area.

Click Rank Resumes.

View and download detailed ranking reports.

---

🧠 AI Scoring Logic

The ranking score combines three metrics:

| Metric              | Description                | Weight |
| ------------------- | -------------------------- | ------ |
| Keyword Match       | Direct keyword overlap     | 0.45   |
| TF-IDF Similarity   | Textual relevance          | 0.45   |
| Semantic Similarity | Contextual meaning (spaCy) | 0.10   |

You can tune these weights in ranker.py to fit your hiring priorities.

---

Advanced Tips

Use a larger spaCy model for better accuracy:
python -m spacy download en_core_web_md

Then edit ranker.py to use:
nlp = spacy.load("en_core_web_md")

🧑‍💻 Author

Rajveer Saggu
GitHub
 | LinkedIn

🏁 License

This project is licensed under the MIT License — feel free to use and modify.


---

Would you like me to include a **“How to deploy on Render or Railway”** section too (so you can host it online easily)?
