import './homePage.css';
import { useNavigate } from 'react-router-dom';
import { 
  Box, ButtonGroup, Button, ButtonBase
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

    const eventSource = new EventSource("http://127.0.0.1:5000/call_function?param=hello");

    eventSource.onmessage = (event) => {
      const data = event.data;
      console.log(data);
      searchSounds(data);
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
  
  async function searchSounds(query) {
    try {
      const payload = {
        query: query
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
  
      if (data.preview_url) {
        console.log("Attempting to play sound from URL:", data.preview_url);
        playSound(data.preview_url);  // Play the sound using the preview URL
      } else {
        console.log('No preview URL available for this sound.');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }
  
  async function generateAndPlayTrack(prompt) {
    try {
      const response = await fetch('http://localhost:5001/generate_and_play', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
      });
  
      if (!response.ok) {
        throw new Error('Track generation failed');
      }
  
      const data = await response.json();
      const trackUrl = data.track_url;
  
      // Play the generated track
      const audio = new Audio(trackUrl);
      audio.play();
    } catch (error) {
      console.error('Error generating and playing track:', error);
    }
  }
  
  function playSound(url) {
    const audio = new Audio(url);
    
    audio.play()
      .then(() => {
        console.log("Sound is playing...");
  
        // Check if the audio duration is greater than 5 seconds
        if (audio.duration > 5) {
          setTimeout(() => {
            audio.pause(); 
            console.log("Audio stopped after 5 seconds.");
          }, 5000); // 5 seconds
        }
      })
      .catch((error) => {
        console.error("Error playing sound:", error);
      });
  }

  async function normal(){
    freesound_auth();
    const word = await startModel();
    console.log("Playing sound for: ", word)
    searchSounds(word)
  }

  async function experimental(){
    freesound_auth();
    const word = await startModel();
    console.log("Playing sound for: ", word)
    generateAndPlayTrack(word);
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
        <Button variant="contained" className='button' onClick={normal}>Normal</Button>
        <Button variant="contained" className='button' onClick={experimental}>Experimental</Button>
      </div>
    </>
  );
}

export default HomePage;
