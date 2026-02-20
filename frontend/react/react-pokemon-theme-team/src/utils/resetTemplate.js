const resetTemplate = () => {
    let cards = document.getElementsByClassName("card");
    while (cards[0]) {
        cards[0].parentNode.removeChild(cards[0]);
    }
    document.getElementById("restart").remove()
    let startBtn = document.getElementById("generate");
    startBtn.disabled = false;
}
export default resetTemplate;