import { useState, useRef } from 'react';
import ShowButton from './components/ShowButton';
import resetGame from './utils/resetGame';
import onSubmit from './utils/onSubmit';
import startGame from './utils/startGame';
import './App.css'

function App() {
  const [game, setGame] = useState(false)
  const [reset, setReset] = useState(false)
  const [feedback, setFeedback] = useState("")
  const answer = useRef(Math.floor(Math.random() * 100) + 1)

  return (
    <>
      <h1>Number Guessing Game</h1>
      {
        game ? (
          <form className="game" 
              onSubmit={(e) => onSubmit(e, reset, setFeedback, setReset, answer)} 
              onReset={(e) => resetGame(e, setFeedback, setReset, answer)}>
            <label className="game" htmlFor="guess-text">Guess a number 1-100:</label>
            <input className="game" type="text" id="guess-text"/>
            <ShowButton reset = {reset}/>
            <p>{ feedback }</p>
        </form>
        ) : (
          <button type="submit" id="start" onClick={(e) => startGame(e, setGame)}>Start</button>
        )
      }
    </>
  )
}

export default App
