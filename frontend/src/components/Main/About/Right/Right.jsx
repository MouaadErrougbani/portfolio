import { Box } from "@mui/material";
import styles from "./Right.styles";
import ContactItems from "./ContactItems";
import useMyInfos from "../../../../hooks/useMyInfos";



function Right() {
    const infos = useMyInfos()
    const myInfos = infos[0];
    if (!myInfos) {
        return null;
    }
    return (
        <Box sx={styles.right.box}>
            <Box
                component="img"
                src={myInfos.image}
                alt="Photo"
                sx={styles.right.img}
            />

            <ContactItems />
        </Box>
    );
}

export default Right;