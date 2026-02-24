import React from 'react'

export default function PokemonCard({data}) {
  return (
    <div className="card">
        <h3>{data.name}</h3>
        <img src={data.sprites.front_default} />
    </div>
  )
}
