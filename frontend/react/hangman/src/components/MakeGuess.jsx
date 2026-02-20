import alphabet from "../utils/alphabet"
import RunHangman from "./RunHangman"
import WrongLettersList from "./WrongLettersList"
import { useState } from 'react'

export default function MakeGuess({puzzle, guessedLetters, setGuessedLetters}) {

    const onSubmit = (e) => {
        e.preventDefault()
        let letter = e.target[0].value.toUpperCase()
        if (guessedLetters && alphabet().indexOf(letter) >= 0) {
            if (guessedLetters.indexOf(letter) == -1) {
                setGuessedLetters([...guessedLetters, letter])
            } else {
                alert("You guessed that letter already dummy")
            }
        }
        e.target[0].value = ""
    }

    return (
        <main>
            <RunHangman key={key1} puzzle={puzzle} guessedLetters={guessedLetters}/>
            <form className="make-guess" onSubmit={onSubmit}>
                <label htmlFor='guess-text'>Enter a letter</label>
                <input type="text" id="guess-text" />
                <button type="submit">Guess!</button>
            </form>
            <WrongLettersList key={key2} puzzle={puzzle} guessedLetters={guessedLetters}/>
        </main>
    )
}
