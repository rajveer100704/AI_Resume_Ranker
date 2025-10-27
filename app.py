from flask import Flask, render_template_string, request, send_file
import os
from ranker import rank_resumes, generate_pdf_report

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# =======================
# HTML TEMPLATE (Dark UI)
# =======================
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>AI Resume Ranker</title>
    <style>
        body {
            background-color: #0f172a; /* dark navy */
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }

        .container {
            background: #1e293b;
            padding: 40px;
            border-radius: 16px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            width: 60%;
            text-align: center;
        }

        h1 {
            color: #14b8a6;
            margin-bottom: 20px;
        }

        textarea, input[type="file"] {
            width: 100%;
            background: #0f172a;
            color: #e2e8f0;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 10px;
            margin-top: 8px;
            margin-bottom: 16px;
        }

        button {
            background-color: #14b8a6;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
        }

        button:hover {
            background-color: #0d9488;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
        }

        th, td {
            padding: 12px;
            border-bottom: 1px solid #334155;
        }

        th {
            color: #14b8a6;
            font-weight: bold;
        }

        a {
            color: #14b8a6;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .logo {
            width: 100px;
            margin-bottom: 20px;
        }

        .back-btn {
            display: inline-block;
            margin-top: 20px;
            color: #38bdf8;
            text-decoration: none;
        }

        .back-btn:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        {% if not results %}
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="logo" alt="Logo">
        <h1>AI Resume Ranker</h1>
        <form action="/" method="POST" enctype="multipart/form-data">
            <label>Job Description:</label><br>
            <textarea name="job_description" rows="6" required></textarea><br>

            <label>Upload Resumes (PDF):</label><br>
            <input type="file" name="resumes" multiple required><br>

            <button type="submit">Rank Resumes</button>
        </form>

        {% else %}
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" class="logo" alt="Logo">
        <h1>Ranked Candidates</h1>
        <table>
            <tr>
                <th>Rank</th>
                <th>Candidate</th>
                <th>Score</th>
            </tr>
            {% for result in results %}
            <tr>
                <td>{{ loop.index }}</td>
                <td>{{ result['filename'] }}</td>
                <td>{{ result['score'] }}</td>
            </tr>
            {% endfor %}
        </table>

        <br>
        <a href="/download/report" class="download-link">📄 Download HR Report</a><br>
        <a href="/" class="back-btn">⬅️ Back to Upload</a>
        {% endif %}
    </div>
</body>
</html>
"""

# =======================
# ROUTES
# =======================

@app.route("/", methods=["GET", "POST"])
def upload_and_rank():
    if request.method == "POST":
        jd = request.form["job_description"]
        files = request.files.getlist("resumes")

        file_paths = []
        for file in files:
            if file.filename.endswith(".pdf"):
                save_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(save_path)
                file_paths.append(save_path)

        # Rank and generate report
        results = rank_resumes(jd, file_paths)
        generate_pdf_report(results)  # includes descending order already

        return render_template_string(TEMPLATE, results=results)

    return render_template_string(TEMPLATE, results=None)


@app.route("/download/report")
def download_report():
    return send_file("reports/HR_Report.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
