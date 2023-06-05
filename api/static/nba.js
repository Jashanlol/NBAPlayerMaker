const searchBar = document.querySelector("#searchBar");
searchBar.addEventListener("input", (event) => {
    const input = event.target.value;
    const alphaOnly = input.replace(/[^A-Za-z\s]/g, "");
    event.target.value = alphaOnly;
})

const button = document.querySelector("#searchImage");
button.addEventListener("click", (event) => {
    const _playerName = searchBar.value;

    updateHTML(_playerName);
    sendRequest(_playerName);
})

function updateHTML(_playerName) {
    const searchElement = document.querySelector(".search");
    searchElement.remove();

    const pElement = document.createElement("p");
    pElement.textContent = "Generating NBA Player... " + _playerName;
    pElement.classList.add("search");
    pElement.style.border = "none";
    document.body.appendChild(pElement);
}

function sendRequest(_playerName) {
    const requestOptions = {
        method: "POST", 
        headers: {
            "Content-Type": "application/json"
        }, 
        body: JSON.stringify({playerName: _playerName})
    };

    fetch('http://localhost:3000/generate', requestOptions)
        .then(response => response.text())
        .then(data => {
            postPlayer(data);
        })
        .catch(error => {
            console.log("Error", error)
        });

}

function postPlayer(player) {
    console.log("Received request for player: " + player);
}