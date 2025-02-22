import './homePage.css';
import { 
  Box, ButtonGroup, Button, ButtonBase, Table, TableBody, TextField,
  TableCell, TableContainer, TableHead, TableRow, Paper, Checkbox, TableSortLabel, 
  Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle
} from '@mui/material';

function howPage() {
  return (
    <>
      <Box className="nav-box">
        <ButtonGroup variant="text">
          <Button className="nav-buttongroup" >What is it?</Button>
          <Button className="nav-buttongroup" >How does it work?</Button>
          <Button className="nav-buttongroup">Who made it?</Button>
        </ButtonGroup>
      </Box>

        <ButtonBase className="logo">
          <img src="/images/vibe2.png" alt="Clickable" className="image" />
        </ButtonBase>

    </>
  );
}

export default howPage;
