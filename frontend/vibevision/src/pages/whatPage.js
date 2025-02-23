import './whatPage.css';
import { Box, ButtonGroup, Button, ButtonBase } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function WhatPage() {
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

    return (
        <>
            <Box className="nav-box">
                <ButtonGroup variant="text">
                    <Button className="nav-buttongroup" onClick={gotoWhoPage}>Who?</Button>
                    <Button className="nav-buttongroup" onClick={gotoWhatPage}>What?</Button>
                    <Button className="nav-buttongroup" onClick={gotoHowPage}>How?</Button>
                </ButtonGroup>
            </Box>

            <div className="logo-container">
                <ButtonBase className="logo" onClick={gotoHomePage}>
                    <img src="/images/vibe2.png" alt="Clickable" className="image" />
                </ButtonBase>
            </div>

            <div className="text-container">
                <div className="title-text">
                    What is VibeVision?
                </div>

                <div className="desc-text">
                    VibeVision is an interactive experience that combines real-time object detection with immersive soundscapes. <br/>
                    Using your camera, it detects objects in your environment and triggers sound effects with each item.<br/>
                    So you can turn turns everyday objects into musical instruments without the price point.<br/>
                    Also, try our new Experimental version: make a unique melody based on your object!<br/>
                </div>
            </div>
        </>
    );
}

export default WhatPage;
