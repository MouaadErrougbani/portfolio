const light = {
    primary: {
        main: "#1976d2",
    },

    secondary: {
        main: "#9c27b0",
    },

    success: {
        main: "#2e7d32",
    },

    error: {
        main: "#d32f2f",
    },

    warning: {
      main: "#ffa726",
    },

    info: {
      main: "#29b6f6",
    },

    background: {
        default: "#f5f5f5",
        paper: "#ffffff",
    },

    text: {
        primary: "#212121",
        secondary: "#616161",
    },
}

const dark = {
    primary: {
      main: "#90caf9",
    },

    secondary: {
      main: "#ce93d8",
    },

    success: {
      main: "#66bb6a",
    },

    error: {
      main: "#f44336",
    },

    warning: {
      main: "#ffa726",
    },

    info: {
      main: "#29b6f6",
    },

    background: {
      default: "#121212",
      paper: "#1e1e1e",
    },

    text: {
      primary: "#ffffff",
      secondary: "#b3b3b3",
    },
}


const types = {
    light,
    dark,
};

const palette = (mode = "light") => ({
    mode,
    ...(types[mode] ?? types.light),
});

export default palette;