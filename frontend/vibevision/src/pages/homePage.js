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
      const response = await fetch("http://127.0.0.1:5000/call_function?param=hello"); 
      if (!response.ok){
          alert("Failed to fetch data");
      } 

      return response.status;
    } catch (error) {
      console.error("Error fetching data:", error);
    }
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
        <Button variant="contained" className='button' onClick={startModel}>Try It!</Button>
      </div>
    </>
  );
}

export default HomePage;
