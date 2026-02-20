const generateCard = (data) => {
    let container = document.getElementById("container")
    let div = document.createElement("div")
    div.className = "card"
    let h3 = document.createElement("h3")
    let img = document.createElement("img")
    img.src = data["sprites"]["front_default"] 
    h3.innerText = data["name"]
    div.appendChild(img)
    div.appendChild(h3)
    container.appendChild(div)
}
export default generateCard;