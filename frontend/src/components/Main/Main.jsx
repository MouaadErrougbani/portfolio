import { Box, Container } from "@mui/material";
import styles from "./Main.styles";

import About from "./About/About";
import Skills from "./Skills/Skills"
import Projets from "./Projets/Projets"
import Formation from "./Formation/Formation"
import Contact from "./Contact/Contact"
import useNavigations from "../../hooks/useNavigations";

function getSection(section) {
    switch(section){
        case "about" :
            return <About />
        case "skills" :
            return <Skills />
        case "projects" :
            return <Projets/>
        case "formation" :
            return <Formation />
        case "contact" :
            return <Contact/>
        default: 
            return null;
    }
}

function Main(){

    const navigation = useNavigations()

    return (
        <Box component="main" sx={styles.main.box}>
            {
                navigation.map((item) =>
                    item.enabled ? (
                        <Box key={item.id}>
                            {getSection(item.label)}
                        </Box>
                    ) : null
                )
            }
        </Box>
    )
}

export default Main;