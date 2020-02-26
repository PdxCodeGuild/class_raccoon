
//Getting elements from html page
let input_todo = document.querySelector("#input_todo")
let submit_todo = document.querySelector("#submit_todo")
let current = document.querySelector("#current")
let completed = document.querySelector("#completed")
let todo_list = document.querySelector("#todo_list")
let completed_list = document.querySelector("#completed_list")
let user_input = ""
let todos = []

submit_todo.addEventListener("click", function(){
    user_input = input_todo.value
    let li = document.createElement("li")
    console.log(li)
    li.innerText = user_input
//    adding complete button
    let li_complete = document.createElement("button")
    li_complete.addEventListener("click",complete_todo)
    li_complete.innerText="Complete"
//    adding delete button
    let li_delete = document.createElement("button")
    li_delete.addEventListener("click", delete_todo)
    li_delete.innerText="Delete"
//    appending buttons
    li.appendChild(li_complete)
    li.appendChild(li_delete)
//    appending li
    todo_list.appendChild(li)
    todos.push(li)
    
})

function complete_todo(){
    let li = this.parentNode
    completed_list.appendChild(li)
    this.style.backgroundColor = 'green'
    console.log(li)
    alert("way to go!")
    
    
}

function delete_todo(){
    let li = this.parentNode
    li.parentNode.removeChild(li)
    console.log(li)


    
}

