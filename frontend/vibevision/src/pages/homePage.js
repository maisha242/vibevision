import './homePage.css';
import { useNavigate } from 'react-router-dom';
import { 
  Box, ButtonGroup, Button, ButtonBase, Table, TableBody, TextField,
  TableCell, TableContainer, TableHead, TableRow, Paper, Checkbox, TableSortLabel, 
  Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle
} from '@mui/material';

function HomePage() {

  const navigate = useNavigate();

  function gotoHomePage() {
    try {
      navigate("/");
    } catch (error) {
      alert(error);
    }
  }

  function gotoWhatPage() {
    try {
      navigate("/what");
    } catch (error) {
      alert(error);
    }
  }

  function gotoWhoPage() {
    try {
      navigate("/who");
    } catch (error) {
      alert(error);
    }
  }

  function gotoHowPage() {
    try {
      navigate("/how");
    } catch (error) {
      alert(error);
    }
  }

  async function startModel() {
    try {
      console.log("maisha remove this")
      const response = await fetch("http://localhost:5005/call_function?param=hello"); 
      if (!response.ok){
          alert("Failed to fetch data");
      } 
      console.log(response.status);

      return response;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  }

  async function freesound_auth() {
    try {
      const response = await fetch('http://localhost:5001/get_access_token');
      if (!response.ok) {
        throw new Error('Failed to fetch access token');
      }
      const data = await response.json();
      console.log('Access Token:', data.access_token); 
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  async function searchSounds(query, filter = "", sort = "score", groupByPack = "0", weights = "") {
    try {
      const payload = {
        query: query,
        filter: filter,
        sort: sort,
        group_by_pack: groupByPack,
        weights: weights
      };
  
      const response = await fetch('http://localhost:5001/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });
  
      if (!response.ok) {
        throw new Error('Search failed');
      }
      
      const data = await response.json();
      console.log('Search Results:', data);  
    } catch (error) {
      console.error('Error:', error);
    }
  }
  

  async function tryit(){
    freesound_auth();
    startModel();
   // searchSounds("meow")
  }

  return (
    <>
      <Box className="nav-box">
        <ButtonGroup variant="text">
          <Button className="nav-buttongroup" onClick={gotoWhatPage}>What?</Button>
          <Button className="nav-buttongroup" onClick={gotoHowPage}>How?</Button>
          <Button className="nav-buttongroup" onClick={gotoWhoPage}>Who?</Button>
        </ButtonGroup>
      </Box>

      <div className="logo-container">
        <ButtonBase className="logo" onClick={gotoHomePage}>
          <img src="/images/vibe2.png" alt="Clickable" className="image" />
        </ButtonBase>
      </div>
      <div className="text">
        Every Object is an Instrument—<br />Compose Your Reality
      </div>
      <div className='button-box'>
        <Button variant="contained" className='button' onClick={tryit}>Try It!</Button>
      </div>
    </>
  );
}

export default HomePage;
