const BASE_URL = "http://127.0.0.1:5000";

// LOGIN
function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch(`${BASE_URL}/api/auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
    })
        .then(res => res.json())
        .then(data => {
            if (data.token) {
                localStorage.setItem("token", data.token);
                window.location.href = "dashboard.html";
            } else {
                alert("Login failed");
            }
        });
}

// LOAD TASKS
function loadTasks() {
    const token = localStorage.getItem("token");

    fetch(`${BASE_URL}/api/tasks/`, {
        headers: {
            "Authorization": "Bearer " + token
        }
    })
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("taskList");
            list.innerHTML = "";

            data.tasks.forEach(task => {
                const li = document.createElement("li");
                li.innerHTML = `${task.title} 
        <button onclick="deleteTask(${task.id})">"❌"</button>`;
                list.appendChild(li);
            });
        });
}

// ADD TASK
function addTask() {
    const token = localStorage.getItem("token");
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;

    fetch(`${BASE_URL}/api/tasks/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({ title, description })
    })
        .then(() => loadTasks());
}

// DELETE TASK
function deleteTask(id) {
    const token = localStorage.getItem("token");

    fetch(`${BASE_URL}/api/tasks/${id}`, {
        method: "DELETE",
        headers: {
            "Authorization": "Bearer " + token
        }
    })
        .then(() => loadTasks());
}
function register() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch("http://127.0.0.1:5000/api/auth/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, email, password })
    })
        .then(res => res.json())
        .then(data => {
            console.log(data);

            if (data.user) {
                alert("Registration successful!");
                window.location.href = "index.html";
            } else {
                alert(data.error || "Registration failed");
            }
        });
}