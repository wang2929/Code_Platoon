export default function WrongLettersList({puzzle, guessedLetters}) {
    let word = [];
    for (let char of puzzle) {
        if (guessedLetters && guessedLetters.indexOf(char) > -1) {
            word.push(char);
        } 
    }
    return (
        <div className="wrong-letters"><p>{word.join('')}</p></div>
    )
}
