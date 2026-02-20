export default function puzzleSolved(puzzle, lettersList) {
    for (char of puzzle) {
        if (lettersList.indexOf(char) == -1) {
            return false
        }
    }
    return true
}