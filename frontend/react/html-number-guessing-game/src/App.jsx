import { useState } from 'react'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  // adding from vanilla js
  const answer = Math.floor(Math.random() * 100) + 1;
  const gameStart = (event) => {
    event.preventDefault()
    let gameForm = document.getElementById("game")
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

    gameForm.replaceChildren(newContent, newInput, newBtn, feedback)
  }

  const playGame = (event) => {
    event.preventDefault();

    let userGuess = document.getElementById("guess-text").value;
    let feedback = document.getElementById("feedback");
    try {
        userGuess = parseInt(userGuess);
    } catch(error) {
        console.error(error)
    }

    if (userGuess < answer) {
        feedback.innerText = `${userGuess} is too low`;
    } else if (userGuess > answer) {
        feedback.innerText = `${userGuess} is too high`;
    } else {
        feedback.innerText = `${userGuess} is correct! Nice!`;

        // Disable button
        let guessBtn = document.getElementById("enter-guess")
        guessBtn.disabled = true

        // Option to restart
        // let resetBtn = document.createElement("button")
        // resetBtn.type = "reset"
        // resetBtn.addEventListener("click", gameStart(event))
        // resetBtn.appendChild(document.createTextNode("Restart Game"))
        // document.getElementById("game").appendChild(resetBtn)
    }
    console.log(answer);
  }


  return (
    <>
      <h1>Number Guessing Game</h1>
      <form id="game" onSubmit = {() => playGame(event)}>
        <button type="submit" id="start" onClick = {() => gameStart(event)}>Start</button>
      </form>
    </>
  )
}

export default App
