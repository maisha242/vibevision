import './homePage.css';
import { useNavigate } from 'react-router-dom';
import { Box, ButtonGroup, Button, ButtonBase } from '@mui/material';
import { useState } from 'react';

function HomePage() {
  const navigate = useNavigate();
  const [currentAudio, setCurrentAudio] = useState(null);  // State to hold the current audio element

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

  let debounceTimeout = null; // Variable to hold the debounce timeout

  async function startModel() {
    const eventSource = new EventSource("http://127.0.0.1:5000/call_function?param=hello");

    eventSource.onmessage = (event) => {
      const data = event.data;
      console.log(data);
      searchSounds(data);
    }
    // try {
    //   const response = await fetch("http://127.0.0.1:5000/call_function?param=hello");

    //   if (!response.ok) {
    //     alert("Failed to fetch data");
    //     return;
    //   }

    //   const reader = response.body.getReader();
    //   const decoder = new TextDecoder();
    //   let result = '';
    //   let lastItem = "";  // Track the last item detected

    //   while (true) {
    //     const { done, value } = await reader.read();
    //     if (done) break;

    //     result = decoder.decode(value, { stream: true });
    //     if (result.trim() && result.trim() !== lastItem) {
    //       lastItem = result.trim();  // Update last item
    //       console.log("found item", lastItem)

    //       // If debounce timeout exists, clear it
    //       if (debounceTimeout) {
    //         clearTimeout(debounceTimeout);
    //       }

    //       // Set new debounce timeout
    //       debounceTimeout = setTimeout(() => {
    //         searchSounds(lastItem);  // Call searchSounds after the debounce period
    //       }, 1000); // 500ms debounce time
    //     }
    //   }
    // } catch (error) {
    //   console.error("Error fetching data:", error);
    // }
  }

  async function searchSounds(query) {
    try {
      const payload = { query: query };

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

  function playSound(url) {
    const audio = new Audio(url);

    audio.play()
      .then(() => {
        console.log("Sound is playing...");
        // The sound will continue as long as the object remains the same.
      })
      .catch((error) => {
        console.error("Error playing sound:", error);
      });
  }

  async function tryit() {
    freesound_auth();
    startModel();
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
