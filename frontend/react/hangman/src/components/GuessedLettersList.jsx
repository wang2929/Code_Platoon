export default function GuessedLettersList({guessedLetters}) {
    console.log(guessedLetters)
    return (
        <div className="wrong-letters"><p>{guessedLetters.join(' ')}</p></div>
    )
}
