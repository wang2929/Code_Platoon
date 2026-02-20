import { useState } from 'react'
import off from './assets/off.svg'
import on from './assets/on.svg'
import './App.css'


function App() {

  

  // helper to change image
  // function changeImage() {
  //   if (image === on) {
  //     setImage(off)
  //   } else { // if image is off currently
  //     setImage(on)
  //   }
  // }

  // track state of image
  const [image, setImage] = useState(on)

  return (
    <>
    <div>
      <h1>{image === on ? "on" : "off"}</h1>
      {/* Condition ? true : false
      If the image is on, set it to off. Otherwise (image is off), set to on. */}
      <div class="container">
        <img onClick = {() => image === on ? setImage(off) : setImage(on) } src = {image} />
      </div>
    </div>
    
    </>
  )
}

export default App
