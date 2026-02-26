export default function ShowDetails({ data }) {
    console.log(data)
    let component = data ? (
    <ul className="list-group">
        <li className="list-group-item">Genres: {data.genres.join(', ')}</li>
        <li className="list-group-item">Average rating: {data.rating.average}</li>
        <li className="list-group-item">Average runtime: {data.averageRuntime} minutes</li>
        <li className="list-group-item"><a href={data.officialSite} target="_blank">Official Site</a></li>
    </ul> ) : (
        <div><p>Loading...</p></div>
    )
    return component
}
