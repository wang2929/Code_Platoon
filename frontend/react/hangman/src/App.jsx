import { useState, useEffect } from 'react'
import './App.css'
import randomWord from './utils/randomword'
import RunHangman from './components/RunHangman'
import MakeGuess from './components/MakeGuess'
import GuessedLettersList from './components/GuessedLettersList'

function App() {
  const [puzzle, setPuzzle] = useState("")
  useEffect(() => { setPuzzle(randomWord()) }, []);
  const [guessedLetters, setGuessedLetters] = useState([])
  useEffect(() => { console.log(`${guessedLetters} from useEffect`) }, []);
  console.log(puzzle)
  return (
    <>
      <main>
        <h1>Let's play Hangman</h1>
        <RunHangman puzzle={puzzle} guessedLetters={guessedLetters}/>
        <MakeGuess puzzle={puzzle} guessedLetters={guessedLetters} setGuessedLetters={setGuessedLetters}/>
        <GuessedLettersList puzzle={puzzle} guessedLetters={guessedLetters}/>
      </main>
    </>
  )
}

export default App
