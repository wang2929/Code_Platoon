import { useState } from 'react'
import HighlightVowels from './HighlightVowels'

function ButtonTemplate({labelText, placeholder, buttonText }) {
    const [word, setWord] = useState("")

    const clicked = (e) => {
        e.preventDefault()
        setWord(e.target[0].value)
        e.target.reset()
    }

    return (
        <>
        <form className="game" onSubmit = { clicked }>
            <label htmlFor="letter">{labelText} </label>
            <input id="letter" type="text" placeholder={placeholder} />
            <button type="submit">{buttonText}</button>
            <HighlightVowels word={word}/>
        </form>
        </>
    )
}

export default ButtonTemplate;