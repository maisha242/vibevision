import './whatPage.css';
import { Box, ButtonGroup, Button, ButtonBase } from '@mui/material';
import { useNavigate } from 'react-router-dom';

function WhoPage() {
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
                    Who made VibeVision?
                </div>

                <div className="desc-text">
                    Our names are Maisha Iqbal and Roshan Nunna. <br/>
                    We are two graduating seniors @ RIT in Software Engineering and Computer Science, respectively. <br/>
                    Fun fact: This is inspired by a project we collaborated on during our first Brickhack (7) in our freshman year. <br/>
                    </div>
            </div>
        </>
    );
}

export default WhoPage;
