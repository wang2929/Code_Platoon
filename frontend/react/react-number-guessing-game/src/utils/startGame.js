const startGame = (e, setGame) => {
    e.preventDefault()
    e.target.hidden = true
    setGame(true)
}

export default startGame;