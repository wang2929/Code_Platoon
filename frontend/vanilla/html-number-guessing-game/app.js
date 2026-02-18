// Your function(s) should go here that will interact with the webpage or DOM
const startBtn = document.querySelector("#start");
const gameForm = document.querySelector("#game")
const answer = Math.floor(Math.random() * 100) + 1;

const gameStart = () => {
    // Update text
    let newContent = document.createElement("h2");
    newContent.appendChild(document.createTextNode("Guess a number 1-100"))

    // Add text box input
    let newInput = document.createElement("input");
    newInput.setAttribute("type", "text");
    newInput.setAttribute("id", "guess-text");

    // Add button
    let newBtn = document.createElement("button");
    newBtn.setAttribute("type", "submit");
    newBtn.setAttribute("id", "enter-guess");
    newBtn.appendChild(document.createTextNode("Guess"))

    // Add feedback
    let feedback = document.createElement("p");
    feedback.setAttribute("id", "feedback");

    gameForm.replaceChildren(newContent, newInput, newBtn, feedback);
}

gameForm.addEventListener("submit", (event) => {
    event.preventDefault();

    let userGuess = document.querySelector("#guess-text").value;
    let feedback = document.querySelector("#feedback");
    try {
        userGuess = parseInt(userGuess);
    } catch(error) {
        console.error(error)
    }

    if (userGuess < answer) {
        feedback.replaceChildren(document.createTextNode(`${userGuess} is too low`));
    } else if (userGuess > answer) {
        feedback.replaceChildren(document.createTextNode(`${userGuess} is too high`));
    } else {
        feedback.replaceChildren(document.createTextNode(`${userGuess} is correct! Nice!`));
        // Option to restart
        let guessBtn = document.getElementById("enter-guess")
        guessBtn.setAttribute("disabled", "True")
        let resetBtn = document.createElement("button")
        resetBtn.setAttribute("id", "reset")
        resetBtn.appendChild(document.createTextNode("Restart Game"))
        resetBtn.addEventListener("click", (event) => {
            event.preventDefault()
            gameStart()
        })
        gameForm.appendChild(resetBtn)
    }
    console.log(answer);
        
})

startBtn.addEventListener("click", (event) => {
    event.preventDefault()
    gameStart()
})