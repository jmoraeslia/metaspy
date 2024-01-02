let mainReport = document.getElementById('mainReport');
let generateMainReport = document.getElementById('generateMainReport');
let buttonAddReport = document.getElementById('reportAdd');
let buttonCleanReport = document.getElementById('reportClean');
let reportAfterModification = document.getElementById('reportAfterModification');
let buttonChangeTheme = document.getElementById('changeTheme');
let themeLink = document.getElementById('theme');
const savedTheme = sessionStorage.getItem('theme');


generateMainReport.addEventListener('click', analyze);
buttonAddReport.addEventListener('click', add);
buttonCleanReport.addEventListener('click', clean);
buttonChangeTheme.addEventListener('click', theme);
document.addEventListener('DOMContentLoaded', save);

function change() {

    if (themeLink.getAttribute('href').includes('light')) {
        themeLink.setAttribute('href', '../static/css/dark.css');
        sessionStorage.setItem('theme', 'dark');
    } else {
        themeLink.setAttribute('href', '../static/css/light.css');
        sessionStorage.setItem('theme', 'light');
    }
}

function analyze() {
    mainReport.style.display = 'block';
}

function add() {
    // 

}

function clean() {
    reportAfterModification.style.display = 'block';
}


function theme() {

    if (themeLink.getAttribute('href').includes('light')) {
        themeLink.setAttribute('href', '../static/css/dark.css');
        sessionStorage.setItem('theme', 'dark');
    } else {
        themeLink.setAttribute('href', '../static/css/light.css');
        sessionStorage.setItem('theme', 'light');
    }
}
function save() {

    if (savedTheme) {
        themeLink.setAttribute('href', `../static/css/${savedTheme}.css`);
    }

}