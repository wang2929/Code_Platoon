import { useState, useEffect } from 'react'
import { useOutletContext } from 'react-router-dom'
import axios from 'axios'
import UserForm from '../components/UserForm'
import CardContainer from '../components/CardContainer'
import PaginationWithEllipsis from '../components/PaginationWithEllipsis'

export default function CharacterPage() {
    const [charData, setCharData] = useState([])
    const [page, setPage] = useState(1)
    const [endPage, setEndPage] = useState(1)
    const [name, setName] = useState("")
    
    useEffect(() => {
        getCharsList()
    }, []);

    // Search parameter should be either name or page number
    const getCharsList = async() => {
        try {
            let url = `https://rickandmortyapi.com/api/character?page=${page}`
            name ? url += `&name=${name}` : null
            let response = await axios.get(url)
            setCharData(response.data.results)
            setEndPage(response.data.info.pages)
        } catch (err) {
            console.error(err)
        }
    }

    const updateActivePage = (page) => {
        setPage(page)
        getCharsList()
    }

    const rmData = (id) => setCharData(charData.filter((c)=>(c.id !== id)))
    
    return (
        <>
            <UserForm name={name} setName={setName} filterData={getCharsList} />
            <CardContainer charData={charData} rmData={rmData}/>
            <PaginationWithEllipsis page={page} endPage={endPage} updatePage={updateActivePage}/>
        </>
    )
}
