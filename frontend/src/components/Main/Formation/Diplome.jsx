import { Box, Typography } from "@mui/material";
import styles from "./Formation.styles";

function Diplome({diplome}){

    return(
        <Box sx={styles.diplome.box}>
            <Typography sx={styles.diplome.h3} component="h3" variant="h3">{diplome.name}</Typography>
            <Typography sx={styles.diplome.h4} component="h4" variant="h4">{diplome.establishment}</Typography>
            <Typography sx={styles.diplome.h5} component="h5" variant="h5">{diplome.startDate} - {diplome.endDate}</Typography>
        </Box>
    )
}


export default Diplome;