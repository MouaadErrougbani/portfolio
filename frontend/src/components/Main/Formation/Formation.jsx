import { Box, Container } from "@mui/material";
import Section from "../Section";
import getDiplomes from "../../../api/diplomeApi"; 
import Diplome from "./Diplome";
import styles from "./Formation.styles";
import { useEffect, useState } from "react";


function Formation(){
    const [diplomes, setDiplomes] = useState([]);

    useEffect(() => {
        const loadDiplomes = async () => {
            const diplomas = await getDiplomes();
            setDiplomes(
                [...diplomas].sort(
                    (a, b) => new Date(b.end_date) - new Date(a.end_date)
                )
            );
        };

        loadDiplomes();
    }, []);

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