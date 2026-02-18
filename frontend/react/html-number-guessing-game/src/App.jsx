import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  // adding from vanilla js
  const answer = Math.floor(Math.random() * 100) + 1;
  const gameForm = document.getElementById("game")
  const gameStart = (event) => {
    event.preventDefault()
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

  const playGame = (event) => {
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
