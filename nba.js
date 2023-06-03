const searchBar = document.querySelector("#searchBar");
searchBar.addEventListener("input", (event) => {
    const input = event.target.value;
    const alphaOnly = input.replace(/[^A-Za-z\s]/g, "");
    event.target.value = alphaOnly;
})

const button = document.querySelector("#searchImage");
button.addEventListener("click", (event) => {
    const playerName = searchBar.value;

    updateHTML(playerName);
})

function updateHTML(playerName) {
    const searchElement = document.querySelector(".search");
    searchElement.remove();

    const pElement = document.createElement("p");
    pElement.textContent = "Generating NBA Player... " + playerName;
    pElement.classList.add("search");
    pElement.style.border = "none";
    document.body.appendChild(pElement);
}