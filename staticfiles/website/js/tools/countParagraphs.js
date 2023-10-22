// countParagraphs.js

function countParagraphs(text) {
    // Split the text by two or more newline characters.
    const paragraphs = text.trim().split(/\n{2,}/);
    return paragraphs.length;
}


// script.js

function handleButtonClick() {
    const textarea = document.getElementById('input-area-A');
    const count = countParagraphs(textarea.value);
    document.getElementById('result').innerText = count + " Paragraphs";
}

document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById('submit-button');
    btn.addEventListener('click', handleButtonClick);
});
