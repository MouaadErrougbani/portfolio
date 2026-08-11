import { Box, Typography } from "@mui/material";
import styles from "./Formation.styles";
import { useTranslation } from "react-i18next";

function Diplome({diplome}){

    const {t, i18n} = useTranslation()

    return(
        <Box sx={styles.diplome.box}>
            <Typography sx={styles.diplome.h3} component="h3" variant="h3">{t(diplome.name)}</Typography>
            <Typography sx={styles.diplome.h4} component="h4" variant="h4">{t(diplome.establishment)}</Typography>
            <Typography sx={styles.diplome.h5} component="h5" variant="h5">{diplome.start_date} - {diplome.end_date}</Typography>
        </Box>
    )
}


export default Diplome;