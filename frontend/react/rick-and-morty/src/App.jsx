import './App.css'
import axios from 'axios'
import Container from 'react-bootstrap/Container'
import NavBar from './components/NavBar'
import Banner from './components/Banner'
import { useState, useEffect } from 'react'
import { Outlet } from 'react-router-dom'

function App() {

    return (
      <>
        <Container>
          <NavBar/>
          <Banner/>
          <Outlet/>
        </Container>
      </>
    )
}

export default App
