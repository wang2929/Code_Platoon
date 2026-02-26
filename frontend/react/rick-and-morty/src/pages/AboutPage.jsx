import { useState, useEffect } from 'react'
import axios from 'axios'
import ShowDetails from '../components/ShowDetails';

export default function AboutPage() {
    const [showData, setShowData] = useState(null)
    useEffect(() => {
        const getShowData = async() => {
            let showURL = "https://api.tvmaze.com/shows/216"
            try {
                let response = await axios.get(showURL)
                setShowData(response)
            }
            catch(err) {
                console.error(err)
            }
        }
        getShowData()
    }, []);

    return (
        <>
            <h1>About the Show</h1>
            { showData ? ( 
                <div>
                    <ShowDetails data={showData.data}/>
                    <div id="inner-text">
                        <p>Rick is a mentally gifted, but sociopathic and alcoholic scientist and a grandfather to Morty; an awkward, impressionable, and somewhat spineless teenage boy. Rick moves into the family home of Morty, where he immediately becomes a bad influence.</p>
                    </div>
                </div>
                 ) : (
                    <p> "loading..." </p>) }
        </>
    )
}
