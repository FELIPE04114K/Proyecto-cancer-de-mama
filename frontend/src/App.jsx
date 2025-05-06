import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'

import './App.css'
import Home from './pages/Home'
import Sintomas from './pages/Sintomas'

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sintomas" element={<Sintomas />} />
        <Route path="/graficos" element={<Sintomas />} />
      </Routes>
    </Router>
  )

}

export default App
