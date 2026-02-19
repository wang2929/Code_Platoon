import axios from 'axios';
import generateCard from './generateCard';
import resetTemplate from './resetTemplate';

const grabMorePokemon = async(data) => {
    // Step 1) Get list of potential Pokemon members
    let pokemonTypes = data["types"];
    const typeURLs = pokemonTypes.map(t => t.type.url);
    let pokeRecruitList = [];
    for (let url of typeURLs) {
        let response = await axios.get(url);
        pokeRecruitList = pokeRecruitList.concat(response.data.pokemon)
    }
    pokeRecruitList.splice(pokeRecruitList.indexOf(data), 1)
    
    // Step 2) Pick random mon from the recruit list. Fill out 5 mons.
    while (document.getElementsByClassName("card").length < 6) {
        let randomID = Math.floor(Math.random() * pokeRecruitList.length) + 1
        let memberURL = pokeRecruitList[randomID].pokemon.url
        pokeRecruitList.splice(randomID, 1)
        let response = await axios.get(memberURL)
        if (response.data.sprites.front_default != null) {
            generateCard(response.data)
        }
    }

    // Step 3) add reset
    let restartBtn = document.createElement("button")
    restartBtn.type = "text"
    restartBtn.id = "restart"
    restartBtn.innerText = "Restart"
    restartBtn.onclick = () => { resetTemplate() }
    let header = document.getElementById("top")
    header.appendChild(restartBtn)
}
export default grabMorePokemon;