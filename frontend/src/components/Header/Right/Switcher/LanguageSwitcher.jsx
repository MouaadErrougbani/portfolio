import { FormControl, MenuItem, Select } from "@mui/material";
import { useTranslation } from 'react-i18next';
import getLanguages from "../../../../config/languages"
import { useEffect } from "react";


function LanguageSwitcher(){
    const {t, i18n} = useTranslation()
    
    const languages = getLanguages()
    
    function changeDirection(language) {
        document.documentElement.lang = language;
        document.documentElement.dir = language === "ar" ? "rtl" : "ltr";
    }

    useEffect(() => {
        changeDirection(i18n.language);
    }, [i18n.language]);

    const handleLanguageChange = (event) => {
        const language = event.target.value;

        i18n.changeLanguage(language);
    };
    return (
        <FormControl size="small">
            <Select
                value={i18n.language}
                onChange={handleLanguageChange}
            >
                {
                    
                    languages.map((item, index) => (<MenuItem key={index} value={item.code}>{item.lable}</MenuItem> ))
                }
            </Select>
        </FormControl>
    )
}

export default LanguageSwitcher;