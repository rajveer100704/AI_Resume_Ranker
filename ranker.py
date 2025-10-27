import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import os

# Load SpaCy model
nlp = spacy.load("en_core_web_md")

# -----------------------------
# PDF Text Extraction
# -----------------------------
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text")
    return text


# -----------------------------
# Preprocessing
# -----------------------------
def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)


# -----------------------------
# Ranking Logic
# -----------------------------
def rank_resumes(job_description, resume_paths):
    jd_processed = preprocess_text(job_description)
    resumes_text = [extract_text_from_pdf(p) for p in resume_paths]
    resumes_processed = [preprocess_text(t) for t in resumes_text]

    # TF-IDF Scores
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([jd_processed] + resumes_processed)
    tfidf_scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Keyword Overlap
    jd_keywords = set(jd_processed.split())
    keyword_scores = []
    for resume in resumes_processed:
        words = set(resume.split())
        keyword_scores.append(len(jd_keywords & words) / len(jd_keywords) if jd_keywords else 0)

    # Semantic Similarity
    jd_doc = nlp(job_description)
    semantic_scores = [jd_doc.similarity(nlp(text)) for text in resumes_text]

    # Weighted Final Score
    ranked = []
    for i, path in enumerate(resume_paths):
        score = (0.45 * keyword_scores[i]) + (0.45 * tfidf_scores[i]) + (0.10 * semantic_scores[i])
        ranked.append({
            "filename": os.path.basename(path),
            "score": round(score * 100, 2)
        })

    # Sort in descending order
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


# -----------------------------
# Professional PDF Report
# -----------------------------
def generate_pdf_report(ranked):
    os.makedirs("reports", exist_ok=True)
    pdf_path = "reports/HR_Report.pdf"

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Header Section
    c.setFillColorRGB(0.05, 0.15, 0.25)
    c.rect(0, height - 80, width, 80, fill=1)

    # Logo / Title
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(width / 2, height - 50, "AI Resume Ranking Report")

    # Table Heading
    y = height - 120
    c.setFont("Helvetica-Bold", 14)
    c.setFillColorRGB(0.08, 0.25, 0.35)
    c.drawCentredString(width / 2, y, "Ranked Candidate Scores")
    y -= 30

    # Table Data
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 12)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.line(70, y + 10, width - 70, y + 10)
    y -= 10

    for i, r in enumerate(ranked, 1):
        if y < 100:  # New page if content overflows
            c.showPage()
            y = height - 100

        c.setFont("Helvetica-Bold", 12)
        c.drawString(100, y, f"{i}. {r['filename']}")
        c.setFont("Helvetica", 12)
        c.drawRightString(width - 100, y, f"Score: {r['score']}")
        y -= 25

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawCentredString(width / 2, 50, "Generated automatically by AI Resume Ranker")

    c.showPage()
    c.save()
    return pdf_path
