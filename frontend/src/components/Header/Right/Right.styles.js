const styles = {
    navigation: {
        box: (theme) => ({
            display: "none",

            [theme.breakpoints.up("lg")]: {
                display: "flex",
                alignItems: "center",
                gap: theme.spacing(2),
            },

            "& a": {
                position: "relative",
                color: theme.palette.text.primary,
                textDecoration: "none",
                fontWeight: 500,
                transition: "color .25s ease",

                "&::after": {
                    content: '""',
                    position: "absolute",
                    left: 0,
                    bottom: -4,
                    width: 0,
                    height: 2,
                    backgroundColor: theme.palette.primary.main,
                    transition: "width .25s ease",
                },

                "&:hover": {
                    color: theme.palette.primary.main,
                },

                "&:hover::after": {
                    width: "100%",
                },
            },
        }),
    },

    right: {
        box: (theme) => ({
            display: "flex",

            alignItems: "center",

            justifyContent: "flex-end",

            gap: theme.spacing(2),

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(4),
            },
        }),
    },
};

export default styles;