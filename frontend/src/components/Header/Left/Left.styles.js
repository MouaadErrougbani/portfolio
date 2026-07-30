const styles = {
    logo: {
        box: (theme) => ({
            display: "flex",
            alignItems: "center",
            justifyContent: "flex-start",

            width: 110,
            flexShrink: 0,

            color: theme.palette.text.primary,

            cursor: "pointer",

            transition: "transform .3s ease",

            "&:hover": {
                transform: "scale(1.03)",
            },

            "& svg": {
                width: "100%",
                height: "auto",
                display: "block",
            },

            [theme.breakpoints.up("sm")]: {
                width: 130,
            },

            [theme.breakpoints.up("md")]: {
                width: 160,
            },

            [theme.breakpoints.up("lg")]: {
                width: 190,
            },

            [theme.breakpoints.up("xl")]: {
                width: 220,
            },
        }),
    },
};

export default styles;