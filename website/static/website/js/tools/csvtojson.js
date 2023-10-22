function convertCSVtoJSON() {
    const csvStr = document.getElementById('csvInput').value;

    Papa.parse(csvStr, {
        header: true,
        complete: function(results) {
            document.getElementById('jsonOutput').value = JSON.stringify(results.data, null, 2);
        }
    });
}
