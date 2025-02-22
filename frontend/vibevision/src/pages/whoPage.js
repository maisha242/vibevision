import './homePage.css';
import { 
  Box, ButtonGroup, Button, ButtonBase, Table, TableBody, TextField,
  TableCell, TableContainer, TableHead, TableRow, Paper, Checkbox, TableSortLabel, 
  Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle
} from '@mui/material';

function whoPage() {
  return (
    <>
      <Box className="nav-box">
        <ButtonGroup variant="text">
          <Button className="nav-buttongroup" >What is it?</Button>
          <Button className="nav-buttongroup" >How does it work?</Button>
          <Button className="nav-buttongroup">Who made it?</Button>
        </ButtonGroup>
      </Box>

      <div className="logo-container">
        <ButtonBase className="logo">
          <img src="/images/vibe2.png" alt="Clickable" className="image" />
        </ButtonBase>
      </div>
      <div className="text">
        Every Object is an Instrument—<br />Compose Your Reality
      </div>
      <div className='button-box'>
        <Button variant="contained" className='button'>Try It!</Button>
      </div>
    </>
  );
}

export default whoPage;
