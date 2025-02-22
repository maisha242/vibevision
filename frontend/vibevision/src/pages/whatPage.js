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
        </>
    );
}

export default WhatPage;
