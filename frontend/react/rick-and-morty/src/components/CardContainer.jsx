import CharacterCard from "./CharacterCard"

export default function CardContainer({ charData, rmData }) {
  return(
    <div 
        className="row row-cols-1 row-cols-md-2 g-4"
    >
    {
        charData ? (
        charData.map((char)=>(
        < CharacterCard 
            name={char.name}
            img={char.image}
            id={char.id}
            rmData={rmData}
            key={char.id}/>
        ))
        ) : (
            null
        )
    }
    </div>
    )
}
