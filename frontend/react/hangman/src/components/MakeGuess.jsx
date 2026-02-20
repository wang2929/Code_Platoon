import alphabet from "../utils/alphabet"

export default function MakeGuess({onClick}) {
    return (
        <main>
            <form className="make-guess" onSubmit={ onClick }>
                <label htmlFor='guess-text'>Enter a letter</label>
                <input type="text" id="guess-text" />
                <button type="submit">Guess!</button>
            </form>
        </main>
    )
}
