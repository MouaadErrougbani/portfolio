import { useTranslation } from 'react-i18next';
import Box from '@mui/material/Box'
import LogoSvg from "../../../assets/images/logo.svg?react";

import styles from './Left.styles';

function Logo(){
    const {t, i18n} = useTranslation()
    return (
        <Box sx={styles.logo.box}>
            <LogoSvg />
        </Box>
    )
}


export default Logo;