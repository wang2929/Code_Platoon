describe('home', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:5173')
  })
})

describe('character', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:5173/character-cards')
  })
})