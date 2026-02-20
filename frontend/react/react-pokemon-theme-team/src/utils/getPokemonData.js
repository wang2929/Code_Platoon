import axios from 'axios';
import generateCard from './generateCard';

const getPokemonData = async(name) => {
    let requestURL = `https://pokeapi.co/api/v2/pokemon/${name}/`;
    try {
        let response = await axios.get(requestURL);
        generateCard(response.data);
    } catch (err) {
        console.error(err);
        alert("Pokemon doesn't exist");
    }
}
export default getPokemonData;