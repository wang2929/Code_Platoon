export default function puzzleSolved(puzzle, lettersList) {
    for (let char of puzzle) {
        if (!lettersList.includes(char)) {
            return false
        }
    }
    return true
}