function copy () {
    let short = document.getElementById('path');
    let button = document.getElementById('copy-button');

    short.style.display = "block";
    short.select();
    short.setSelectionRange(0, 100);
    document.execCommand('copy');
    short.style.display = "none";

    let str = ' 👍'.repeat(3);
    if (button.textContent.endsWith(str)) {
        button.textContent = button.textContent.slice(0, -str.length);
    }
    button.textContent += ' 👍';
}
