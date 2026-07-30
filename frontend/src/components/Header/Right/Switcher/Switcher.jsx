import { Box } from "@mui/material";
import LanguageSwitcher from "./LanguageSwitcher";
import ThemeSwitcher from "./ThemeSwitcher";
import styles from "./Switcher.styles";

function Switcher(){
    return(
        <Box component="nav" 
            sx={styles.box}
        >
            <LanguageSwitcher/>
            <ThemeSwitcher/>
        </Box>
    )
}


export default Switcher;