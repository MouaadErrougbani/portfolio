import { Box } from "@mui/material";
// import photo from "../../../../assets/images/photo.jpg";
import styles from "./Right.styles";
import ContactItems from "./ContactItems";
import getMyInfos from "../../../../config/myInfos";



function Right() {
    const myInfos = getMyInfos()
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