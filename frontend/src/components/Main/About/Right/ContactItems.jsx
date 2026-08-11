import MailRoundedIcon from "@mui/icons-material/MailRounded";
import GitHubIcon from "@mui/icons-material/GitHub";
import Inventory2TwoToneIcon from "@mui/icons-material/Inventory2TwoTone";
import LinkedInIcon from "@mui/icons-material/LinkedIn";

import { IconButton, Stack } from "@mui/material";

import styles from "./Right.styles";
import useContacts from "../../../../hooks/useContacts";

const icons = {
    MailRoundedIcon: <MailRoundedIcon />,
    GitHubIcon: <GitHubIcon />,
    Inventory2TwoToneIcon: <Inventory2TwoToneIcon />,
    LinkedInIcon: <LinkedInIcon />,
};

function ContactItem({ contact }) {
    const clickedHandler = () => {
        window.open(contact.lien, "_blank", "noopener,noreferrer");
    };

    return (
        <IconButton onClick={clickedHandler}>
            {icons[contact.icon]}
        </IconButton>
    );
}

function ContactItems() {
    const contacts = useContacts().filter(
        (contact) => icons[contact.icon]
    );

    return (
        <Stack
            direction="row"
            spacing={2}
            sx={styles.contactItems.stack}
        >
            {contacts.map((contact) => (
                <ContactItem
                    key={contact.id}
                    contact={contact}
                />
            ))}
        </Stack>
    );
}

export default ContactItems;