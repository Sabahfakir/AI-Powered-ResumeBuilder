from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
#[pfrom dotenv import load_dotenv
import pdfplumber

from ai_summary import generate_summary
from ats import calculate_ats_score, calculate_ats_score_advanced

# load_dotenv()

app = Flask(__name__)
CORS(app)

# --------------------------
# FRONTEND ROUTES
# --------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ats")
def ats_page():
    return render_template("ats.html")


# --------------------------
# AI SUMMARY
# --------------------------

@app.route("/generate-summary", methods=["POST"])
def summary():
    data = request.json
    result = generate_summary(data)
    return jsonify({"summary": result})


# --------------------------
# ATS FROM TEXT
# --------------------------

@app.route("/ats-score", methods=["POST"])
def ats_score():
    data = request.json
    resume_text = data.get("resume_text")
    job_description = data.get("job_description")

    result = calculate_ats_score(resume_text, job_description)
    return jsonify(result)


# --------------------------
# ATS FROM PDF UPLOAD
# --------------------------

@app.route("/upload-resume", methods=["POST"])
def upload_resume():
    file = request.files.get("resume")
    job_description = request.form.get("job_description")

    resume_text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                resume_text += text + " "

    result = calculate_ats_score_advanced(resume_text, job_description)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)