import { Box, Container } from "@mui/material";
import Left from "./Left/Left";
import Right from "./Right/Right";
import styles from "./Header.styles";


function Header(){
    return (
        <Box component="header" sx={styles.header} >
            <Container  maxWidth="lg" 
                        sx={styles.container}>
                <Left/>
                <Right/>
            </Container>
        </Box>
    )
}

export default Header;