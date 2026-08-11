import { useState } from "react";
import {
    Box,
    Divider,
    Drawer,
    IconButton,
    List,
    ListItemButton,
    ListItemText,
} from "@mui/material";

import MenuIcon from "@mui/icons-material/Menu";

import Logo from "../Left/Logo";
import LanguageSwitcher from "./Switcher/LanguageSwitcher";
import ThemeSwitcher from "./Switcher/ThemeSwitcher";

import styles from "./DrawerMenu.styles";
import useNavigations from "../../../hooks/useNavigations";

function DrawerMenu() {
    const [open, setOpen] = useState(false);


    const navigation = useNavigations()

    function capitalize(text) {
        return text.charAt(0).toUpperCase() + text.slice(1).toLowerCase();
    }

    const closeDrawer = () => {
        setOpen(false);
    };

    return (
        <>
            <IconButton
                onClick={() => setOpen(true)}
                sx={styles.menuButton}
            >
                <MenuIcon />
            </IconButton>

            <Drawer
                anchor="right"
                open={open}
                onClose={closeDrawer}
                PaperProps={{
                    sx: styles.drawer,
                }}
            >
                <Box sx={styles.content}>
                    <Box sx={styles.logo}>
                        <Logo />
                    </Box>

                    <Divider />

                    <List sx={styles.list}>
                        {navigation
                            .filter((item) => item.enabled)
                            .map((item) => (
                                <ListItemButton
                                    key={item.id}
                                    component="a"
                                    href={`#${item.label}`}
                                    onClick={closeDrawer}
                                    sx={styles.item}
                                >
                                    <ListItemText
                                        primary={capitalize(item.label)}
                                    />
                                </ListItemButton>
                            ))}
                    </List>

                    <Divider />

                    <Box sx={styles.switchers}>
                        <LanguageSwitcher />
                        <ThemeSwitcher />
                    </Box>
                </Box>
            </Drawer>
        </>
    );
}

export default DrawerMenu;