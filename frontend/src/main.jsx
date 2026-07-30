import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './i18n';
import AppThemeProvider from "./context/ThemeProvider.jsx"




createRoot(document.getElementById('root')).render(
  
  <StrictMode>
    <AppThemeProvider>
      <App />
    </AppThemeProvider>
  </StrictMode>,
)
