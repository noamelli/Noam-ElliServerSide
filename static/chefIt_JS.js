const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
  if (link.href.includes(`${activePage}`)) {
    link.classList.add('active');
  }
});
var i = 0;
var txt = ["Please choose the category you want"]; /* The text */
var speed = 80;

typeWriter = () => {
  document.querySelector("#demo").innerHTML = txt[0].substring(0, i) + "<span>\u25ae </span>";
  if (i++ != txt[0].length) {
    setTimeout(typeWriter, speed);
  }
}
window.addEventListener("load", typeWriter)

