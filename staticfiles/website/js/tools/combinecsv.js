
function combineFiles() {
    const inputFiles = document.getElementById('inputFiles');
    const allFiles = inputFiles.files;
    
    if (allFiles.length === 0) {
        alert('Please select at least one file.');
        return;
    }

    const combinedData = [];

    let filesProcessed = 0;

    for (const file of allFiles) {
        const fileExt = file.name.split('.').pop().toLowerCase();
        const reader = new FileReader();
        
        reader.onload = function(event) {
            let data;

            if (fileExt === 'csv') {
                data = Papa.parse(event.target.result, {header: true}).data;
            } else if (fileExt === 'xls' || fileExt === 'xlsx') {
                const workbook = XLSX.read(event.target.result, {type: 'binary'});
                const sheetName = workbook.SheetNames[0];
                data = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName]);
            }

            if (data) {
                combinedData.push(...data);
            }

            filesProcessed++;
            
            if (filesProcessed === allFiles.length) {
                const csv = Papa.unparse(combinedData);
                downloadCSV(csv);
            }
        };

        if (fileExt === 'csv') {
            reader.readAsText(file);
        } else if (fileExt === 'xls' || fileExt === 'xlsx') {
            reader.readAsBinaryString(file);
        }
    }
}

function downloadCSV(csv) {
    const blob = new Blob([csv], {type: 'text/csv'});
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'combined.csv';
    a.click();
    window.URL.revokeObjectURL(url);
}
