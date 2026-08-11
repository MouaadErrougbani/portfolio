import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import LanguageDetector from 'i18next-browser-languagedetector';
import { getTraductions } from './api/traductionApi';


const loadTranslations = async () => {

    const translations = await getTraductions()

    const resources = {
        ar: {
            translation: {},
        },
        fr: {
            translation: {},
        },
        en: {
            translation: {},
        },
    };

    translations.forEach((item) => {
        resources.ar.translation[item.label] = item.ar;
        resources.fr.translation[item.label] = item.fr;
        resources.en.translation[item.label] = item.en;
    });

    return resources;
};

const initI18n = async () => {
    const resources = await loadTranslations();

    await i18n
        .use(LanguageDetector)
        .use(initReactI18next)
        .init({
            resources,

            fallbackLng: 'en',

            debug: true,

            interpolation: {
                escapeValue: false,
            },
        });
};

export { initI18n };

export default i18n;