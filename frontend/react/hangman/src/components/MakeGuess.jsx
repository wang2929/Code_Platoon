import alphabet from "../utils/alphabet"

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
    }

    return (
        <form className="make-guess" onSubmit={onSubmit}>
            <label htmlFor='guess-text'>Enter a letter</label>
            <input type="text" id="guess-text" />
            <button type="submit">Guess!</button>
        </form>
    )
}
