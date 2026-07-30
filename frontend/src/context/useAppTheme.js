import { useContext } from "react";
import ThemeContext from "./ThemeContext";

function useAppTheme() {
    const context = useContext(ThemeContext);

    if (!context) {
        throw new Error(
            "useAppTheme must be used inside AppThemeProvider"
        );
    }

    return context;
}

export default useAppTheme;