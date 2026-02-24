import React from 'react'

export default function GeneratePokemon({ onClick }) {
  return (
    <header id="top">
      <h1>Pokemon Theme Team</h1>
      <p>Get your themed Pokemon team here!</p>
      <button id="generate" type="text" onClick = { onClick }>Generate Pokemon</button>
    </header>
  )
}
