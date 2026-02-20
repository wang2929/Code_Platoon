export default function RunHangman({key, puzzle, guessedLetters}) {
    let word = [];
    for (let char of puzzle) {
        if (guessedLetters.indexOf(char) < 0) {
            word.push('_ ');
        } else {
            word.push(char);
        }
    }
    return (
        <div key={key} className="hangman">
            <h2>{word.join('')}</h2>
        </div>
    )
}
