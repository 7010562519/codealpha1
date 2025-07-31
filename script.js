async function translateText() {
    const text = document.getElementById('inputText').value;
    const source = document.getElementById('sourceLang').value;
    const target = document.getElementById('targetLang').value;

    const response = await fetch(https://api.mymemory.translated.net/get?q=${text}&langpair=${source}|${target});
    const data = await response.json();
    
    document.getElementById('output').innerText = data.responseData.translatedText;
}

function copyText() {
    const translatedText = document.getElementById('output').innerText;
    navigator.clipboard.writeText(translatedText);
    alert("Copied to clipboard!");
}

function speakText() {
    const text = document.getElementById('output').innerText;
    const speech = new SpeechSynthesisUtterance(text);
    window.speechSynthesis.speak(speech);
}