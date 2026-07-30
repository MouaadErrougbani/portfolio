const styles = {
    main: {
        box: (theme) => ({
            flexGrow: 1,

            width: "100%",

            backgroundColor: theme.palette.background.default,

            overflow: "hidden",
        }),

        container: (theme) => ({
            backgroundColor: theme.palette.background.paper,
        }),
    },

    section: {
        typography: (theme) => ({
            position: "relative",

            display: "inline-block",

            color: theme.palette.text.primary,

            fontWeight: 700,

            letterSpacing: 1,

            marginBottom: theme.spacing(4),

            fontSize: "1.8rem",

            "&::after": {
                content: '""',

                position: "absolute",

                left: 0,
                bottom: -8,

                width: 70,
                height: 4,

                borderRadius: 999,

                backgroundColor: theme.palette.primary.main,
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "2.1rem",

                "&::after": {
                    width: 80,
                },
            },

            [theme.breakpoints.up("md")]: {
                marginBottom: theme.spacing(5),
                fontSize: "2.4rem",

                "&::after": {
                    width: 90,
                },
            },

            [theme.breakpoints.up("lg")]: {
                marginBottom: theme.spacing(6),
                fontSize: "2.8rem",

                "&::after": {
                    width: 100,
                    height: 5,
                },
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "3.2rem",

                "&::after": {
                    width: 120,
                    height: 6,
                },
            },

            [theme.breakpoints.down("md")]: {
                display: "table",

                marginLeft: "auto",
                marginRight: "auto",

                textAlign: "center",

                "&::after": {
                    left: "50%",
                    transform: "translateX(-50%)",
                },
            },
        }),
    },
};

export default styles;