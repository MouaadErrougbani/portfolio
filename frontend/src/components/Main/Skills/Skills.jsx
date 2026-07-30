import { Box, Container, Typography } from "@mui/material";
import Section from "../Section";
import getSkilles from "../../../config/skilles";
import styles from "./Skills.styles";
import InfiniteSkills from "./InfiniteSkills";





function SKills(){
    const skills = getSkilles()
    const categories = Object.keys(skills)
    
    return (
        <Box component="section" sx={styles.box}>
            <Container maxWidth="lg" >
            <Section label="Skills"/>
                {
                    categories.map((categorie, index) => (
                        <Box key={index}>
                            <Typography component="p" variant="body1" sx={styles.typography} >
                                {categorie}
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