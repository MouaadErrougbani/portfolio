import { Box, Container, Typography } from "@mui/material";
import Section from "../Section";
import styles from "./Skills.styles";
import InfiniteSkills from "./InfiniteSkills";
import { useEffect, useState } from "react";
import getSkills from "../../../api/skillApi";
import { useTranslation } from "react-i18next";





function SKills(){
    const [skills, setSkills] = useState([])
    const {t, i18n} =  useTranslation()

    useEffect((()=> {
        const loadingSkills = async () => {
            try {
                const data = await getSkills();
                setSkills(data);
            } catch (error) {
                console.error("Failed to load skills:", error);
            }
        }
        loadingSkills()
    }), []);

    const categories = Object.keys(skills)
    
    return (
        <Box component="section" sx={styles.box}>
            <Container maxWidth="lg" >
            <Section label="Skills"/>
                {
                    categories.map((categorie, index) => (
                        <Box key={index}>
                            <Typography component="p" variant="body1" sx={styles.typography} >
                                {t(categorie)}
                            </Typography>
                            <InfiniteSkills skills={skills[categorie]}/>
                        </Box>

                    ))
                }

            </Container>
        </Box>
    )
}

export default SKills;