import { useState, useEffect, useRef } from 'react'
import axios from 'axios'
import './App.css'
import alphabet from './utils/alphabet'
import puzzleSolved from './utils/puzzlesolved'
import RunHangman from './components/RunHangman'
import MakeGuess from './components/MakeGuess'
import GuessedLettersList from './components/GuessedLettersList'

function App() {
  const [puzzle, setPuzzle] = useState("")
  const wordList = useRef([])
  const [isLoading, setLoading] = useState(true)
  const [guessedLetters, setGuessedLetters] = useState([])
  const [game, setGame] = useState(true)
  const [losing, setLosing] = useState(0)
  const [endGame, setEndGame] = useState("")

  useEffect(() => { 
    let url = `https://random-words-api.kushcreates.com/api?language=en&category=birds&type=uppercase`
    axios.get(url).then((response) => {
      wordList.current = response.data
      pickWord(response.data)
    }).catch(error => console.log(error))
   }, [])

  const pickWord = (arr) => {
    let idx = Math.floor(Math.random() * arr.length)
    setPuzzle(arr[idx].word)
    setLoading(false)
  }

  const onSubmit = (e) => {
    e.preventDefault()
    let letter = e.target[0].value.toUpperCase()
    if (guessedLetters && alphabet().includes(letter)) {
        if (!guessedLetters.includes(letter)) {
          setGuessedLetters([...guessedLetters, letter])
          checkEndGame(letter)
        } else {
            alert(`You guessed ${letter} already dummy`)
        }
    }
    e.target[0].value = ""
  }

  const checkEndGame = (char) => {
    if (puzzle.split('').includes(char)) {
      if (puzzleSolved(puzzle, [...guessedLetters, char])) {
        setEndGame("You win! Nice job!")
        setGame(false)
      }
    } else {
      setLosing(losing + 1)
      if (losing + 2 > 7) {
        setEndGame(`Answer was \"${puzzle.charAt(0).toUpperCase() + puzzle.slice(1).toLowerCase()}\". You lost stooOooOopid`)
        setGame(false)
      }
    }
  }

  const reset = () => {
    setLoading(true)
    setLosing(0)
    setGuessedLetters([])
    setGame(true)
    pickWord(wordList.current)
  }

  if (isLoading) {
    return <div className="loading-screen">Loading...</div>
  }
  else {
    return (
      <>
      {
        <main>
          <h1>Let's play bird-themed Hangman</h1>
          <RunHangman puzzle={puzzle} guessedLetters={guessedLetters}/>
          {
            game ? (
              <div>
                <MakeGuess onClick={onSubmit}/>
                <GuessedLettersList puzzle={puzzle} guessedLetters={guessedLetters}/>
                <p>Strikes: {losing} / 7</p>
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
}

export default App