import axios from 'axios'
import Container from 'react-bootstrap/Container'
import NavBar from './components/NavBar'
import Banner from './components/Banner'
import { Outlet } from 'react-router-dom'
import './App.css'
import { useState, useEffect } from 'react'

function App() {

    return (
      <>
        <Container>
            <Banner/>
            <NavBar/>  
            <Outlet/>
        </Container>
      </>
    )
}

export default App
