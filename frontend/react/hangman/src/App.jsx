import { useState, useEffect, useRef } from 'react'
import './App.css'
import randomWord from './utils/randomword'
import alphabet from './utils/alphabet'
import RunHangman from './components/RunHangman'
import MakeGuess from './components/MakeGuess'
import GuessedLettersList from './components/GuessedLettersList'

function App() {
  const [puzzle, setPuzzle] = useState(randomWord())
  const [guessedLetters, setGuessedLetters] = useState([])
  const [game, setGame] = useState(true)
  const [losing, setLosing] = useState(0)
  const [winning, setWinning] = useState(0)
  const [endGame, setEndGame] = useState("")

  const onSubmit = (e) => {
    e.preventDefault()
    let letter = e.target[0].value.toUpperCase()
    if (guessedLetters && alphabet().includes(letter)) {
        if (!guessedLetters.includes(letter)) {
          setGuessedLetters([...guessedLetters, letter])
          checkEndGame(letter)
        } else {
            alert("You guessed that letter already dummy")
        }
    }
    e.target[0].value = ""
  }

  const countLetters = (letter) => {
    const map = new Map()
    map.set(letter, (map.get(letter)))
  }

  const checkEndGame = (char) => {
    console.log(`${winning} ${puzzle.length} ${puzzle}`)
    if (puzzle.split('').includes(char)) {
      setWinning(winning + 1)
      if (winning + 1 === puzzle.length) {
        setEndGame("You win woOooOoOOo")
        setGame(false)
      }
    } else {
      setLosing(losing + 1)
      if (losing > 8) {
        setEndGame("You lost stooOoOoOOoOooOopid")
        setGame(false)
      }
    }
  }

  const reset = () => {
    setWinning(0)
    setLosing(0)
    setPuzzle(randomWord())
    setGuessedLetters([])
    setGame(true)
  }

  return (
    <>
    {
      <main>
        <h1>Let's play Hangman</h1>
        <RunHangman puzzle={puzzle} guessedLetters={guessedLetters}/>
        {
          game ? (
            <div>
              <MakeGuess onClick={onSubmit}/>
              <GuessedLettersList puzzle={puzzle} guessedLetters={guessedLetters}/>
            </div>
          ) : (
            <div>
            <h2>{endGame}</h2>
            <button type="button" onClick={ reset }>Play Again</button>
            </div>
          )
        }
      </main>
    }
    </>
  )
}

export default App