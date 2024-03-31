const fname =document.getElementById('name')
// const lname =document.getElementById('ame')
const password =document.getElementById('password')
const form =document.getElementById('form')
const error =document.getElementById('error')

form.addEventListener('Sign-in',(e)=>{
    let message = []
    if (fname.value === "" || fname.value === null){
        message.push('Name is reqiured')
    }
    if (password.value.length<=6){
        message.push('password must be longer than 6 characters')
    }
    if (messages.length>0){
        e.preventDefault()
        errorElement.innerText = message.join(',')
    }
})

