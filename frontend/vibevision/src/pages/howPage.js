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
                    How does VibeVision work?
                </div>

                <div className="desc-text">
                    Object Detection AI model: EfficientDet-Lite0 from Google MediaPipe <br/>
                    Open Source Sound Database: Freesound <br/>
                    Generative AI model: OpenAI GPT-4o Mini <br/>
                    Text to Music AI model: Beatoven.ai <br/>
                    Frontend Framework: React <br/>
                    Backend Framework: Flask <br/>
                </div>
            </div>
        </>
    );
}

export default WhatPage;
