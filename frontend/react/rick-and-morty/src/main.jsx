import { createRoot } from 'react-dom/client'
import router from './router.jsx';
import './index.css'
import { RouterProvider } from 'react-router-dom'

createRoot(document.getElementById('root')).render(
  <RouterProvider router={router}/>
)
