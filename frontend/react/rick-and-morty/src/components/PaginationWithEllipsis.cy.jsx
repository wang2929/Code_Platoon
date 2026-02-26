import React from 'react'
import PaginationWithEllipsis from './PaginationWithEllipsis'

describe('<PaginationWithEllipsis />', () => {
  it('renders', () => {
    // see: https://on.cypress.io/mounting-react
    cy.mount(<PaginationWithEllipsis page={1} endPage={42} updatePage={()=>console.log("Hello")} />)
  })
})