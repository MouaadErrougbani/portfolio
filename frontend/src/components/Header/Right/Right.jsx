import { Box } from "@mui/material";
import Navigation from "./Navigation";
import Switcher from "./Switcher/Switcher";
import styles from "./Right.styles";
import DrawerMenu from "./DrawerMenu";


function Right() {
    return (
        <Box sx={styles.right.box}>
            <Navigation />
            <DrawerMenu />
            <Switcher />
        </Box>
    );
}

export default Right;