const onSubmit = (e, reset, setFeedback, setReset, answer) => {
    e.preventDefault()
    if (reset) {
        return
    }
    let input = e.target[0].value
    try {
        if (parseInt(input) === answer.current) {
        setFeedback("You got it!")
        setReset(true)
        } else if (parseInt(input) > answer.current) {
        setFeedback(`${e.target[0].value} is too big!`)
        } else {
        setFeedback(`${e.target[0].value} is too small!`)
        }
        e.target[0].value = ""
    } catch {
        setFeedback("Unable to parse this number")
    }
}

  export default onSubmit;