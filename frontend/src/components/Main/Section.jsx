import { Typography } from "@mui/material";
import styles from "./Main.styles";
import { useTranslation } from 'react-i18next';

function Section({label}){
    const {t, i18n} = useTranslation()
    const id = label.toLowerCase()
    return (
        <Typography id={id} component="h2" variant="h3" sx={styles.section.typography}>
            {t(label.toLowerCase())}
        </Typography>
    )
}


export default Section;