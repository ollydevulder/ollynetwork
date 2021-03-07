function getCookie (name) {
    let r = RegExp(name + "=([^;]+)");
    let content = r.exec(document.cookie);
    return (content) ? decodeURI(content[1]) : false;
}

function setCookie (name, value) {
    document.cookie = `${name}=${value}`;
}
