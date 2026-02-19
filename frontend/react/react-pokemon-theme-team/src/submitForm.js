import getPokemonData from "./getPokemonData";

const submitForm = (event) => {
    event.preventDefault();
    let data = Object.fromEntries(new FormData(event.target));
    console.log(data)
    getPokemonData(data["name"])
}
export default submitForm;