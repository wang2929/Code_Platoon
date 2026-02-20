import './App.css'
import getRandomPokemon from './utils/getRandomPokemon'

function App() {

  return (
    <>
    <header id="top">
      <h1>Pokemon Theme Team</h1>
      <button id="generate" type="text" onClick = { () => getRandomPokemon() }>Generate Pokemon</button>
    </header>
    <main id='container'>
    </main>
    </>
  )
}

export default App
