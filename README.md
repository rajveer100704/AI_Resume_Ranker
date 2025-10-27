# 🧠 AI Resume Ranker

**AI Resume Ranker** is a smart web application that ranks resumes against a given job description using **NLP** and **AI scoring**.
It evaluates resumes based on **keyword relevance**, **TF-IDF similarity**, and **semantic matching** to give recruiters an instant shortlist.

---

## 🚀 Features

* 🔍 **Automatic Resume Screening** — Upload multiple resumes and compare them to a job description.
* 🤖 **AI-Powered Scoring** — Combines keyword, TF-IDF, and semantic similarity for accurate ranking.
* 📊 **Detailed Reports** — Generates PDF reports highlighting candidate strengths and weaknesses.
* 🐳 **Docker Support** — Run the app easily inside a Docker container.
* 💾 **Clean Web Interface** — Built using Flask, HTML, and TailwindCSS.

---

## 🧹 Tech Stack

| Component            | Technology Used             |
| -------------------- | --------------------------- |
| **Backend**          | Python (Flask)              |
| **NLP & AI**         | spaCy, scikit-learn, TF-IDF |
| **Frontend**         | HTML, CSS, JavaScript       |
| **Containerization** | Docker & Docker Compose     |
| **Reports**          | FPDF / ReportLab            |

---

## 📁 Project Structure

```
Resume_Ranker/
├── app.py
├── ranker.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   └── styles.css
│
├── resumes/
├── uploads/
└── Reports/
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rajveer100704/AI_Resume_Ranker.git
cd AI_Resume_Ranker
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run with Docker (Optional)

```bash
docker compose up --build
```

---

## 💻 Usage

1. Upload one or more resumes (`.pdf` / `.docx`).
2. Paste the job description in the text area.
3. Click **“Rank Resumes”**.
4. View and download detailed ranking reports.

---

## 🧠 AI Scoring Logic

The overall ranking score combines three weighted metrics:

| Metric                  | Description                | Weight |
| ----------------------- | -------------------------- | ------ |
| **Keyword Match**       | Direct keyword overlap     | 0.45   |
| **TF-IDF Similarity**   | Textual relevance          | 0.45   |
| **Semantic Similarity** | Contextual meaning (spaCy) | 0.10   |

> 🔧 You can tune these weights in `ranker.py` to fit your hiring priorities.

---

## 🧠 Advanced Tips

Use a larger spaCy model for better semantic accuracy:

```bash
python -m spacy download en_core_web_md
```

Then update in `ranker.py`:

```python
nlp = spacy.load("en_core_web_md")
```

---

## 👨‍💻 Author

**Rajveer Singh Saggu**

---

## 🏁 License

This project is licensed under the **MIT License** — feel free to use and modify.
