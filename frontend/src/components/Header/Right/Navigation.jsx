import { Box, Link, Typography } from "@mui/material";
import getNavigation from "../../../config/navigation";
import styles from "./Right.styles";
import { useEffect } from "react";

function Navigation() {
    const navigation = getNavigation()

    function capitalize(text) {
        return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    }

    return (
        <Box 
            sx={styles.navigation.box}
        >
            {navigation.map((item) => (
                item.enable && 
                <Link key={item.id} 
                    underline="none" 
                    href={`#${item.label}`}
                >
                    {capitalize(item.label)}
                </Link> 
            ))}
        </Box>
    )
}

export default Navigation;