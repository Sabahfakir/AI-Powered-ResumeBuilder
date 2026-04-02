const { jsPDF } = window.jspdf;

// Live Preview Update
document.querySelectorAll("input, textarea").forEach(el => {
    el.addEventListener("input", updatePreview);
});

function updatePreview() {
    document.getElementById("previewName").innerText =
        document.getElementById("name").value || "Your Name";

    document.getElementById("previewContact").innerText =
        document.getElementById("email").value + " | " +
        document.getElementById("phone").value;

    document.getElementById("previewSummary").innerText =
        document.getElementById("summary").value;

    document.getElementById("previewSkills").innerText =
        document.getElementById("skills").value;

    document.getElementById("previewExperience").innerText =
        document.getElementById("experience").value;

    document.getElementById("previewEducation").innerText =
        document.getElementById("education").value;
}

// AI Summary API Call
async function generateSummary() {
    const data = {
        name: name.value,
        skills: skills.value,
        experience: experience.value,
        education: education.value
    };

    const response = await fetch("/generate-summary", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    summary.value = result.summary;
    updatePreview();
}

// ATS Score
async function checkATS() {

    let score = Math.floor(Math.random() * 100); // temporary until backend connected

    let bar = document.getElementById("atsBar");
    bar.style.width = score + "%";
    bar.innerHTML = score + "%";
    
    const resumeText = document.getElementById("resumePreview").innerText;

    const response = await fetch("/ats-score", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            resume_text: resumeText,
            job_description: "Looking for Python Flask developer with API and SQL knowledge"
        })
    });

    const result = await response.json();

    document.getElementById("atsResult").innerHTML =
        "ATS Score: " + result.ats_score + " / 100";
}

// PDF Download using jsPDF
function downloadPDF() {
    const doc = new jsPDF();

    const content = document.getElementById("resumePreview").innerText;

    doc.text(content, 10, 10);
    doc.save("resume.pdf");
}