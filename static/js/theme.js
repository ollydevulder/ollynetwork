/* Colour theme stuff */
const style = document.documentElement.style;

const light_theme = {
    'background': 'white',
    'primary': 'black',
    'secondary': '#bbb',
    'highlight': '#fbf855'
};

const dark_theme = {
    'background': '#222',
    'primary': 'white',
    'secondary': '#ccc',
    'highlight': '#7b3988'
};

const setTheme = (theme) => {
    for (let v in theme) {
        style.setProperty(`--${v}`, theme[v]);
    }
};

const switchTheme = () => {
    (getCookie('theme') == 'dark')
        ? setTheme(light_theme) : setTheme(dark_theme);
    (getCookie('theme') == 'dark')
        ? setCookie('theme', 'light') : setCookie('theme', 'dark');
}
