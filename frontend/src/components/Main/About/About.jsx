import { Box, Container } from "@mui/material";
import Section from "../Section";
import Left from "./Left/Left";
import Right from "./Right/Right";
import styles from "./About.styles";

function About(){

    return (
        <Box component="section" sx={styles.about.box}>
            <Container maxWidth="lg">
                
                        <Section 
                            label="About"
                            />
                <Box sx={styles.about.container}>
                    <Box>
                        <Left/>
                    </Box>
                    <Right/>
                </Box>
            </Container>
        </Box>
    )
}

export default About;