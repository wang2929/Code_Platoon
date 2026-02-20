export default function WrongLettersList({key, puzzle, guessedLetters}) {
    let word = [];
    for (let char of puzzle) {
        if (guessedLetters.indexOf(char) > -1) {
            word.push(char);
        } 
    }
    return (
        <div key={key} className="wrong-letters"><p>{word.join('')}</p></div>
    )
}
