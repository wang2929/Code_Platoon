export default function GuessedLettersList({guessedLetters}) {
    return (
        <div className="wrong-letters"><p>{guessedLetters.join(' ')}</p></div>
    )
}
