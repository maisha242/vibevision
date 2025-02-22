import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/homePage'; 
import WhatPage from './pages/whatPage';  
import WhoPage from './pages/whoPage';
import HowPage from './pages/howPage';

function Apap() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} /> 
        <Route path="/what" element={<WhatPage />} />
        <Route path="/who" element={<WhoPage />} />
        <Route path="/how" element={<HowPage />} />
      </Routes>
    </Router>
  );
}

export default Apap;
