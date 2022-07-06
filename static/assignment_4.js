function myFunction() {
    document.querySelector('#feForm')?.addEventListener('submit', (e) => {
        e.preventDefault()
        const id = e.target.id.value
        fetch('https://reqres.in/api/users/' + id).then(
            response => response.json()
        ).then(
            response => createUsersList(response.data)
        ).catch(
            err => console.log(err)
        );
    })
}

function createUsersList(response) {
    console.log(response.data)

    const currMain = document.querySelector("form")

    const section = document.getElementById('feSection')
    section.innerHTML = `
       <img src="${response.avatar}" alt="picture">
        <h3>Full Name: ${response.first_name} ${response.last_name} </h3>
        <a href="mailto:${response.email}">Send Email</a>
    
    `
    currMain.appendChild(section)

}