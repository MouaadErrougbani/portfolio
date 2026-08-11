import { useEffect, useState } from "react"
import getLanguages from "../api/languageApi";

const useLanguages = () => {
    const [language, setLanguage] = useState([]);

    useEffect(() => {
        const loadLanguages = async () => {
            const languages = await getLanguages();

            setLanguage(languages);
        };

        loadLanguages();
    }, []);

    return language;
};

export default useLanguages;