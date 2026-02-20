export default function RunHangman({puzzle, guessedLetters}) {
    let word = [];
    for (let char of puzzle) {
        if (guessedLetters && guessedLetters.indexOf(char) == -1) {
            word.push(char);
        } else {
            word.push('_ ');
        }
    }
    return (
        <div className="hangman">
            <h2>{word.join('')}</h2>
        </div>
    )
}
