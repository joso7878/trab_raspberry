let token = null;

async function register() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch("/api/register", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name, email, password})
    });

    alert(await res.text());
}

async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await fetch("/api/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email, password})
    });

    const data = await res.json();
    token = data.token;

    alert("Logado!");
    loadData();
}

async function saveData() {
    const value = document.getElementById("dataInput").value;

    await fetch("/api/data", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
        },
        body: JSON.stringify({data: value})
    });

    loadData();
}

async function loadData() {
    const res = await fetch("/api/data", {
        headers: {
            "Authorization": "Bearer " + token
        }
    });

    const data = await res.json();

    const list = document.getElementById("list");
    list.innerHTML = "";

    data.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item.data;
        list.appendChild(li);
    });
}