import { useMemo, useState } from "react";

import {
    ThemeProvider as MuiThemeProvider,
    CssBaseline,
} from "@mui/material";

import ThemeContext from "./ThemeContext";
import getTheme from "../theme/index";

function AppThemeProvider({ children }) {

    const [mode, setMode] = useState("dark");

    const toggleTheme = () => {
        setMode((prev) =>
            prev === "light"
                ? "dark"
                : "light"
        );
    };

    const theme = useMemo(() => {
        return getTheme(mode);
    }, [mode]);

    const value = useMemo(() => ({
        mode,
        setMode,
        toggleTheme,
    }), [mode]);

    return (
        <ThemeContext.Provider value={value}>
            <MuiThemeProvider theme={theme}>
                <CssBaseline />
                {children}
            </MuiThemeProvider>
        </ThemeContext.Provider>
    );
}

export default AppThemeProvider;