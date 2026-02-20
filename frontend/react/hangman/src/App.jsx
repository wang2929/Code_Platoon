import { useState, useRef, useEffect } from 'react'
import './App.css'
import randomWord from './utils/randomword'
import RunHangman from './components/RunHangman'
import MakeGuess from './components/MakeGuess'
import WrongLettersList from './components/WrongLettersList'

function App() {
  const [puzzle, setPuzzle] = useState("")
  const [hangmanKey, setHangmanKey] = useState(1)
  const [lettersKey, setLettersKey] = useState(-1)
  useEffect(() => { setPuzzle(randomWord()) }, []);
  const [guessedLetter, setGuessedLetter] = useState([])
  
  return (
    <>
    <main>
      <h1>Let's play Hangman</h1>
      <RunHangman key={hangmanKey} puzzle={puzzle} guessedLetters={guessedLetter}/>
      <MakeGuess addToKey={hangmanKey} setAddKey={setHangmanKey}
            subFromKey={lettersKey} setSubKey={setLettersKey} guessedLetters={guessedLetter}/>
      <WrongLettersList key={lettersKey} puzzle={puzzle} guessedLetters={guessedLetter}/>
    </main>
    </>
  )
}

export default App
