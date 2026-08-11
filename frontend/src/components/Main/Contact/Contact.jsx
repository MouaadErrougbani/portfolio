import { Box, Container } from "@mui/material";
import Section from "../Section";

import Left from "./Left";
import Right from "./Right";
import styles from "./Contact.styles";



function Contact(){
    return (
        <Box component="section">
            <Container sx={styles.contact.container}  maxWidth= "lg">
                <Section label="Contact"/>
                <Box sx={styles.contact.box}>
                    <Left/>
                    <Right/>
                </Box>
            </Container>
        </Box>
    )
}

export default Contact;