// Sets up the hangman progress
export default function RunHangman({puzzle, guessedLetters}) {
    let word = [];
    for (let char of puzzle) {
        // array.indexOf(elem) = i if array[i] === element else -1
        if (guessedLetters && guessedLetters.indexOf(char) > -1) {
            word.push(char);
        } else {
            word.push('_ ');
        }
    }
    console.log(word)
    return (
        <div className="hangman">
            <h2>{word.join('')}</h2>
        </div>
    )
}
