import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/homePage'; 
import WhatPage from './pages/whatPage';  

function Apap() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} /> {/* Use capitalized component names */}
        <Route path="/what" element={<WhatPage />} />
      </Routes>
    </Router>
  );
}

export default Apap;
