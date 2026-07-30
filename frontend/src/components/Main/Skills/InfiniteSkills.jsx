import { Box, Stack } from "@mui/material";
import styles from "./Skills.styles";


function InfiniteSkills({skills}){

    return (
        <Box sx={styles.slider}>
            <Stack sx={styles.track}>
                {[...skills, ...skills].map((skill, index) => (
                    <Box key={index} sx={styles.item}>
                        {skill}
                    </Box>
                ))}
            </Stack>
        </Box>
    );
}

export default InfiniteSkills;