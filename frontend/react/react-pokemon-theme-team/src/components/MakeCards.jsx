import React from 'react'
import PokemonCard from './PokemonCard'

export default function MakeCards({ data, otherMonsList }) {
  const cards = []
  cards.push(<PokemonCard data={data}/>)
  while (cards.length < 6) {
    let idx = Math.floor(Math.random() * otherMonsList.length)
    let url = otherMonsList[idx].pokemon.url
    otherMonsList.splice(idx, 1)
    axios.get(url).then((response) => {
      if (response.data.sprites.front_default != null) {
        cards.push(<PokemonCard data={response.data}/>)
      }
    }).error((err) => console.log(err))
  }

  return (
    <div id="card-holder">{cards}</div>
  )
}
