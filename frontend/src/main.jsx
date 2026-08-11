import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import App from './App.jsx';
import { initI18n } from './i18n';
import AppThemeProvider from './context/ThemeProvider.jsx';

const startApp = async () => {
    await initI18n();

    createRoot(document.getElementById('root')).render(
        <StrictMode>
            <AppThemeProvider>
                <App />
            </AppThemeProvider>
        </StrictMode>
    );
};

startApp();