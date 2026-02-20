function HighlightVowels({word}) {

    const vowels = () => {
        return ['a','e','i','o','u','y','A','E','I','O','U','Y']
    }

    const assignClass = (char) => {
        if (vowels().indexOf(char) > -1) {
            return "vowel";
        } else {
            if (char === ' ') {
                return "space";
            }
            else {
                return "consonant"
            }
        }
    }
    return (
        <>
        <div className="formatted-word">
            {
                word.split('').map((char) => (
                    <p className={ assignClass(char) }>
                        {char}
                    </p>
                ))
            }
        </div>
        </>
    )
}

export default HighlightVowels;