import { Box, Button, Stack, Typography } from "@mui/material";
import styles from "./Projets.styles";
import GitHubIcon from '@mui/icons-material/GitHub';
import ArrowOutwardIcon from '@mui/icons-material/ArrowOutward';

function Tags({tags}){

    return (
        <Stack sx={styles.tags.stack}>
            {
                tags.map((tag, index)=>(
                    <Typography component="p" variant="body1" key={index} sx={styles.tags.p}>{tag}</Typography>
                ))
            }
        </Stack>
    )
}

function Cart({project}){

    const clickedHandler = (link)=>{
        link ?
        window.open(link, "_blank", "noopener,noreferrer") : console.log("Image")
    }

    return(
        <Box sx={styles.cart.box}>
            <Box component="img" onClick={() => clickedHandler(null)} src={project.image} sx={styles.cart.image}/>
            <Typography component="p" variant="body1" sx={styles.cart.pName}>{project.name}</Typography>
            <Typography component="p" variant="body1" sx={styles.cart.pDesc}>{project.description}</Typography>
            <Tags tags={project.tags}/>
            <Stack sx={styles.cart.stack}>
                <Button onClick={()=> clickedHandler(project.githubLink)} sx={styles.cart.button}><GitHubIcon/> </Button>
                <Button onClick={()=> clickedHandler(project.productionLink)} sx={styles.cart.button} >{project.name} <ArrowOutwardIcon/> </Button>
            </Stack>
        </Box>
    )
}


export default Cart;