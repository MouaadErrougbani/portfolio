import { useTranslation } from 'react-i18next';
import Container from '@mui/material/Container';
import navigation from './config/navigation';

import {
    Box,
    FormControl,
    IconButton,
    MenuItem,
    Select,
    Typography,
} from "@mui/material";
import {
    Brightness4,
    Brightness7,
} from "@mui/icons-material";

import useAppTheme from './context/useAppTheme'

import Header from './components/Header/Header';
import Main from './components/Main/Main';
import Footer from './components/Footer/Footer';





function App() {

  const {t, i18n} = useTranslation()
  const {mode, toggleTheme} = useAppTheme()
  
  const handleLanguageChange = (event) => {
    i18n.changeLanguage(event.target.value);
  };



  return (
    <Box sx={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
    }}>
      <Header/>
      <Main/>
      <Footer/>
    </Box>
    
  );
}

export default App

