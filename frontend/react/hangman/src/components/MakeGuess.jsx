import alphabet from "../utils/alphabet"

export default function MakeGuess({addToKey, setAddKey, subFromKey, setSubKey, guessedLetters}) {

    const onSubmit = (e) => {
        e.preventDefault()
        console.log("is it working")
        let letter = e.target[0].value.toUpperCase()
        if (alphabet().indexOf(letter) >= 0 && guessedLetters.indexOf(letter) == -1) {
            guessedLetters.push(letter)
            console.log(guessedLetters)
            setAddKey(addToKey + 1)
            setSubKey(subFromKey - 1)
            console.log(`${addToKey} ${subFromKey}`)
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
