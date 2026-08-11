import { Box, Link, Typography } from "@mui/material";

import MailRoundedIcon from '@mui/icons-material/MailRounded';
import GitHubIcon from '@mui/icons-material/GitHub';
import LinkedInIcon from '@mui/icons-material/LinkedIn';

import LocalPhoneIcon from '@mui/icons-material/LocalPhone';
import LocationPinIcon from '@mui/icons-material/LocationPin';
import WhatsAppIcon from '@mui/icons-material/WhatsApp';

import styles from "./Contact.styles";
import useContacts from "../../../hooks/useContacts";

const icons = {
    "MailRoundedIcon" : <MailRoundedIcon />, 
    "GitHubIcon" : <GitHubIcon/>,
    "LinkedInIcon": <LinkedInIcon/>,
    "LocalPhoneIcon": <LocalPhoneIcon/>,
    "LocationPinIcon": <LocationPinIcon/>,
    "WhatsAppIcon": <WhatsAppIcon/>,
}

function Left(){
    const contacts = useContacts()
    return(
        <Box sx={styles.left.box}>
            {
                contacts.map((contact)=>(
                    
                        icons[contact.icon] 
                        && 
                        <Box sx={styles.left.boxContact} key={contact.id}> 
                            {icons[contact.icon]}
                            {
                                contact.link ?   
                                <Link href={contact.link} 
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    underline="none"
                                    color="text.primary"
                                >{contact.label}</Link>
                                :
                                <Typography sx={styles.left.p} component="p" variant="body1" >{contact.label}</Typography> 

                            }
                        </Box>
                    
                ))
            }
        </Box>
    )
}
export default Left;