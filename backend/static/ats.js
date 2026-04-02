async function uploadResume() {

    const fileInput = document.getElementById("resumeFile");
    const jobDescription = document.getElementById("jobDescription").value;

    const formData = new FormData();
    formData.append("resume", fileInput.files[0]);
    formData.append("job_description", jobDescription);

    const response = await fetch("/upload-resume", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    let score = result.ats_score;

    let bar = document.getElementById("atsBar");
    bar.style.width = score + "%";
    bar.innerHTML = score + "%";

    document.getElementById("analysisResult").innerHTML = `
        <p><strong>Keyword Matches:</strong> ${result.keyword_matches}</p>
        <p><strong>Readability Score:</strong> ${result.readability}</p>
        <p><strong>Missing Keywords:</strong> ${result.missing_keywords.join(", ")}</p>
    `;
}