import { Box, Container } from "@mui/material";
import styles from "./Main.styles";

import getNavigation from "../../config/navigation";

import About from "./About/About";
import Skills from "./Skills/Skills"
import Projets from "./Projets/Projets"
import Formation from "./Formation/Formation"
import Contact from "./Contact/Contact"
import { useEffect } from "react";

function getSection(section) {
    switch(section){
        case "about" :
            return <About />
        case "skills" :
            return <Skills />
        case "projets" :
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
    const navigation = getNavigation()

    return (
        <Box component="main" sx={styles.main.box}>
            {
                navigation.map((item) =>
                    item.enable ? (
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