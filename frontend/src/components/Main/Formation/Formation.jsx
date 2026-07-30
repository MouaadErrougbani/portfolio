import { Box, Container } from "@mui/material";
import Section from "../Section";
import getDiplomes from "../../../config/diplomes"; 
import Diplome from "./Diplome";
import styles from "./Formation.styles";
function Formation(){
    const diplomes = getDiplomes()
    return (
        <Box component="section" sx={styles.formation.box}>
            <Container maxWidth="lg" sx={styles.formation.container}>
            <Section label="Formation"/>
                {
                    diplomes.map((diplome)=>(<Diplome diplome={diplome} key={diplome.id}/>))
                }
            </Container>
        </Box>
    )
}

export default Formation;