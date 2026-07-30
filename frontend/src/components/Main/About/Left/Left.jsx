import { Box, Button, styled, Typography } from "@mui/material";
import { useTranslation } from "react-i18next";
import ArrowCircleDownIcon from '@mui/icons-material/ArrowCircleDown';

import styles from "./Left.styles";
import getMyInfos from "../../../../config/myInfos";

function Left(){
    const {t, i18n} = useTranslation()
    const myInfos = getMyInfos()
    function downloadCV() {
        const link = document.createElement("a");
        link.href = "/files/CV_ER-ROUGBANI_Mouaad.pdf";
        link.download = "CV_ER-ROUGBANI_Mouaad.pdf";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
    

    return(
        <Box component="div" sx={styles.left.box}>
            <Typography component="h2" 
                        variant="h5" 
                        sx={styles.left.h5}
            >
                {t(myInfos.welcome)}
            </Typography>
            <Typography component="p" 
                        variant="h6"
                        sx={styles.left.h6}
            >
                {t(myInfos.petitDesc)}
            </Typography>
            <Typography component="p" 
                        variant="body1"
                        sx={styles.left.body1}
            > 
                {t(myInfos.desc)} 
            </Typography>
            <Button variant="outlined" 
                onClick={downloadCV}
                startIcon={<ArrowCircleDownIcon />}
                sx={styles.left.button}
            >
                {t(myInfos.cv)}
            </Button>
        </Box>
    )
}

export default Left;