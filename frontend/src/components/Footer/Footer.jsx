import { Box, Container, Typography, Stack, IconButton } from "@mui/material";

import GitHubIcon from "@mui/icons-material/GitHub";
import LinkedInIcon from "@mui/icons-material/LinkedIn";
import EmailIcon from "@mui/icons-material/Email";
import getContacts from "../../config/contacts"; 

import styles from "./Footer.styles";


const icons = {
    "MailRoundedIcon" : <EmailIcon />, 
    "GitHubIcon" : <GitHubIcon/>,
    // "Inventory2TwoToneIcon": <Inventory2TwoToneIcon/>, // Pour icon kaggle
    "LinkedInIcon": <LinkedInIcon/>
}

function ContactItem({contact}){
    const clickedHandler = (contact)=>{
        window.open(contact.lien, "_blank", "noopener,noreferrer");
    }

    return (
        <IconButton sx={styles.iconButton}  onClick={()=>clickedHandler(contact)}>
            {icons[contact.icon]}
        </IconButton>
    )
}

function Footer() {
    const year = new Date().getFullYear();
    const contacts = getContacts()
    return (
        <Box component="footer" sx={styles.footer}>
            <Container maxWidth="lg" sx={styles.container}>
                <Typography variant="body2" sx={styles.copyright}>
                    © {year} ER-ROUGBANI Mouaad. All Rights Reserved.
                </Typography>

                <Typography variant="body2" sx={styles.text}>
                    Built with React & Material UI.
                </Typography>

                <Stack direction="row" spacing={1}>
                    {
                        contacts.map((contact) => (
                            
                                icons[contact.icon] && <ContactItem contact={contact}/>
                            
                            )
                        )
                    }
                </Stack>
            </Container>
        </Box>
    );
}

export default Footer;