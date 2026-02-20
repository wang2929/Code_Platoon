import alphabet from "../utils/alphabet"
import RunHangman from "./RunHangman"
import WrongLettersList from "./WrongLettersList"
import { useState } from 'react'

export default function MakeGuess({puzzle}) {
    const [key1, setKey1] = useState(-1)
    const [key2, setKey2] = useState(1)
    const [guessedLetters, setGuessedLetters] = useState([])
    useEffect(() => { console.log(guessedLetters) }, []);

    const random = () => {
        setKey1(Math.random()*(100))
        setKey2(Math.random()*(-100))
    }
    
    const onSubmit = (e) => {
        e.preventDefault()
        console.log(`${guessedLetters} here`)
        let letter = e.target[0].value.toUpperCase()
        if (guessedLetters && alphabet().indexOf(letter) >= 0 && guessedLetters.indexOf(letter) == -1) {
            console.log(guessedLetters)
            setGuessedLetters([...guessedLetters, letter])
            random()
        }
    }

    return (
        <main>
            <RunHangman key={key1} puzzle={puzzle} guessedLetters={guessedLetters}/>
            <form className="make-guess" onSubmit={onSubmit}>
                <label htmlFor='guess-text'>Enter a letter</label>
                <input type="text" id="guess-text" />
                <button type="submit">Guess!</button>
            </form>
            <WrongLettersList key={key2} puzzle={puzzle} guessedLetters={guessedLetters}/>
        </main>
    )
}
