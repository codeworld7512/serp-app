function convertJSONtoCSV() {
    // Get reference to the ldBar progress bar
    let progressBar = document.querySelector(".ldBar");
    progressBar.setAttribute("data-value", "50");  // Set progress to 50% initially

    // Introduce a brief delay to simulate processing
    setTimeout(() => {
        let jsonInput = document.getElementById("jsonInput").value;
        let parsedJson;

        try {
            parsedJson = JSON.parse(jsonInput);
        } catch (error) {
            alert("Invalid JSON format.");
            progressBar.setAttribute("data-value", "0");  // Reset progress to 0%
            return;
        }

        // Convert JSON to CSV using PapaParse
        let csv = Papa.unparse(parsedJson);

        // Display the CSV in the output textarea
        document.getElementById("csvOutput").value = csv;

        // Indicate completion by setting progress to 100%
        progressBar.setAttribute("data-value", "100");
    }, 500);  // 500 milliseconds (0.5 seconds) delay
}

function downloadCSV() {
    let csvContent = document.getElementById("csvOutput").value;
    
    // Check if the CSV content is empty
    if (!csvContent) {
        alert("Please convert the JSON to CSV first.");
        return;
    }

    let blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    let downloadLink = document.createElement("a");

    let url = URL.createObjectURL(blob);
    downloadLink.href = url;
    downloadLink.download = "data.csv"; // You can rename the file if needed

    document.body.appendChild(downloadLink); // Required for Firefox
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

document.addEventListener("DOMContentLoaded", (event) => {
    let bar = new ldBar(".ldBar");
});
