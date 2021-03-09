function copy () {
    let short = document.getElementById('short');
    short.select();
    short.setSelectionRange(0, 100);
    document.execCommand('copy');
}
