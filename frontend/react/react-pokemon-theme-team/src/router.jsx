import NotFoundPage from "./pages/NotFoundPage";
import HomePage from "./pages/HomePage";
import AboutPage from "./pages/AboutPage";
import App from "./App";
import { createBrowserRouter } from 'react-router-dom';

const router = createBrowserRouter([{
    path: '/',
    element:<App/>,
    children: [{
        index: true,
        element: <HomePage/>
    }, {
        path:'about',
        element: <AboutPage/>
    }, {
        path:'*',
        element: <NotFoundPage/>
    }]
}]);

export default router;