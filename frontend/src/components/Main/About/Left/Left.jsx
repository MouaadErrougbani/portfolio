import { Box, Button, styled, Typography } from "@mui/material";
import { useTranslation } from "react-i18next";
import ArrowCircleDownIcon from '@mui/icons-material/ArrowCircleDown';

import styles from "./Left.styles";
import useMyInfos from "../../../../hooks/useMyInfos";

function Left(){
    const {t, i18n} = useTranslation()
    const infos = useMyInfos()

    const myInfos = infos[0];
    if (!myInfos) {
        return null;
    }

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
                {t(myInfos.message)}
            </Typography>
            <Typography component="p" 
                        variant="h6"
                        sx={styles.left.h6}
            >
                {t(myInfos.petit_desc)}
            </Typography>
            <Typography component="p" 
                        variant="body1"
                        sx={styles.left.body1}
            > 
                {t(myInfos.full_desc)} 
            </Typography>
            <Button variant="outlined" 
                onClick={downloadCV}
                startIcon={<ArrowCircleDownIcon />}
                sx={styles.left.button}
            >
                {t("download_cv")}
            </Button>
        </Box>
    )
}

export default Left;