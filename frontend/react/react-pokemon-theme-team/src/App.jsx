import './App.css'
import axios from 'axios';
import { useState, useEffect, useRef } from 'react'
import GeneratePokemon from './components/GeneratePokemon';
import MakeCards from './components/MakeCards';
import { Outlet } from 'react-router-dom';

function App() {
  const [pokemonId, setPokemonId] = useState(-1)
  const [makeCards, setMakeCards] = useState(false)
  const pokemonData = useRef(null)
  const [pokeList, setPokeList] = useState([])

  useEffect(() => {
    if (pokemonId > 0) {    
      getAllData()
    }
  }, [pokemonId])

  const getAllData = () => {
    if (pokemonId <= 0) return;
    let pokeURL = `https://pokeapi.co/api/v2/pokemon/${pokemonId}/`;
    axios.get(pokeURL).
      then((pokeId) => {
        pokemonData.current = pokeId.data;
        getPokeList(pokeId.data.types);
      }).catch((err) => console.log(err));
  }

  const getPokeList = async(typeList) => {
    let tempList = [];
    for (let t of typeList) {
      // I wanted to do a then... catch... but the tempList didn't persist
      // outside of the block for some reason
      try {
        let response = await axios.get(t.type.url)
        tempList = tempList.concat(response.data.pokemon)
      } catch(err) {
        console.log(err)
      }
    }
    tempList.splice(tempList.indexOf(pokemonData.current), 1)
    setPokeList(tempList)
    setMakeCards(true)
  }

  const getId = () => {
    let id = Math.floor(Math.random() * 1025)
    setPokemonId(id)
    setMakeCards(true)
  }

  return (
    <>
    <main id='container'>
      <Outlet/>
      {/* <GeneratePokemon onClick={getId}/>
      { { makeCards } ? (
          <div>
            <MakeCards data={pokemonData.current} otherMonsList={ pokeList } />
            <button id="restart" type="text" onClick = { setMakeCards(false) }>Restart</button>
          </div>
        ) : (
          null
        )
      }  */}
    </main>
    </>
  )
}

export default App
