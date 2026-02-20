const resetGame = (e, setFeedback, setReset, answer) => {
    e.preventDefault()
    setFeedback("")
    setReset(false)
    answer.current = Math.floor(Math.random() * 100) + 1
  }

export default resetGame;