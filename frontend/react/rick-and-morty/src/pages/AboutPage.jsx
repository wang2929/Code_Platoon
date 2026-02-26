import { useState, useEffect } from 'react'
import axios from 'axios'
import ShowDetails from '../components/ShowDetails';

export default function AboutPage() {
    const [showData, setShowData] = useState(null)
    useEffect(() => getShowData(), []);

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

    // thinking of changing the API just because of the dangerouslysetinnerhtml but ah
    return (
        <>
            <h1>About the Show</h1>
            { showData ? ( 
                <div>
                    <ShowDetails data={showData.data}/>
                    <div id="dangerous-html-div" dangerouslySetInnerHTML={{__html: showData.data.summary}}></div>
                </div>
                 ) : (
                    <p> "loading..." </p>) }
        </>
    )
}
