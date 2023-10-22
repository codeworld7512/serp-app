// countCharacters.js

function countCharacters(text) {
    return text.length;
}

// script.js

function handleButtonClick() {
    const textarea = document.getElementById('input-area-A');
    const count = countCharacters(textarea.value);
    document.getElementById('result').innerText = count + " Characters";
}

document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById('submit-button');
    btn.addEventListener('click', handleButtonClick);
});
