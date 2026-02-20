import { useState, useEffect } from 'react'
import './App.css'
import randomWord from './utils/randomword'
import RunHangman from './components/RunHangman'
import MakeGuess from './components/MakeGuess'
import WrongLettersList from './components/WrongLettersList'

function App() {
  const [puzzle, setPuzzle] = useState("")
  useEffect(() => { setPuzzle(randomWord()) }, []);
  
  return (
    <>
      <h1>Let's play Hangman</h1>
      <MakeGuess puzzle={puzzle}/>
    </>
  )
}

export default App
