import { Box, Link, Typography } from "@mui/material";
import styles from "./Right.styles";
import { useTranslation } from "react-i18next";
import useNavigations from "../../../hooks/useNavigations";

function Navigation() {
    const navigation = useNavigations()

    function capitalize(text) {
        return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    }

    const {t, i18n} = useTranslation()
    
    return (
        <Box 
            sx={styles.navigation.box}
        >
            {navigation.map((item) => (
                item.enabled && 
                <Link key={item.id} 
                    underline="none" 
                    href={`#${item.label}`}
                >
                    {(t(item.label))}
                </Link> 
            ))}
        </Box>
    )
}

export default Navigation;