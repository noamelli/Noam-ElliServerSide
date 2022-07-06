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


function myFunction() {
    console.log("connected!!!:)")
    let id = document.getElementById("id").value;
    fetch("https://reqres.in/api/users/ " + id).then(
        response => response.json()
    ).then(
        response => createUsersList(response.data)
    ).catch(
        err => console.log(err)
    );
}

function createUsersList(response) {
    let id = document.getElementById("id").value;
    const currMain = document.querySelector("main")
    if (id != '') {
        let user = response
        console.log(user)
        const section = document.createElement('section')
        section.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
             <span>id: ${user.id} </span>
             <span> ,Full name: ${user.first_name} ${user.last_name}</span>
             <br>
             <a href="mailto:${user.email}">Send Email</a>
            </div>          
                     `
        currMain.appendChild(section)
    }

}

