import { FormControl, MenuItem, Select } from "@mui/material";
import { useTranslation } from 'react-i18next';
import { useEffect } from "react";
import useLanguages from "../../../../hooks/useLanguages";


function LanguageSwitcher(){
    const {t, i18n} = useTranslation()
    
    const languages = useLanguages()
    
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
                    
                    languages.map((item, index) => (<MenuItem key={index} value={item.code}>{item.label}</MenuItem> ))
                }
            </Select>
        </FormControl>
    )
}

export default LanguageSwitcher;