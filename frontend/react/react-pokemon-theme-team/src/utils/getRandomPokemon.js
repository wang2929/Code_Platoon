import axios from 'axios';
import generateCard from './generateCard';
import grabMorePokemon from './grabMorePokemon';

const getRandomPokemon = async() => {
    let pokemonID = Math.floor(Math.random() * 1025) + 1;
    let requestURL = `https://pokeapi.co/api/v2/pokemon/${pokemonID}/`
    try {
        let response = await axios.get(requestURL);
        generateCard(response.data);
        grabMorePokemon(response.data);

        // Okay, time to restart stuff
        let startBtn = document.getElementById("generate")
        startBtn.disabled = true
    } catch (err) {
        console.error(err);
        alert("Pokemon doesn't exist");
    }
}
export default getRandomPokemon;