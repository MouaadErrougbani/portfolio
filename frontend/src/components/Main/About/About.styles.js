const styles = {
    about: {
        box: (theme) => ({
            backgroundColor: theme.palette.background.default,

            paddingTop: theme.spacing(6),
            paddingBottom: theme.spacing(6),

            [theme.breakpoints.up("sm")]: {
                paddingTop: theme.spacing(7),
                paddingBottom: theme.spacing(7),
            },

            [theme.breakpoints.up("md")]: {
                paddingTop: theme.spacing(9),
                paddingBottom: theme.spacing(9),
            },

            [theme.breakpoints.up("lg")]: {
                paddingTop: theme.spacing(11),
                paddingBottom: theme.spacing(11),
            },

            [theme.breakpoints.up("xl")]: {
                paddingTop: theme.spacing(13),
                paddingBottom: theme.spacing(13),
            },
        }),

        container: (theme) => ({
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",

            width: "100%",

            gap: theme.spacing(4),

            "& > :first-of-type": {
                flex: 1.2,
                minWidth: 0,
            },

            "& > :last-child": {
                flex: 0.8,
                display: "flex",
                justifyContent: "center",
            },

            [theme.breakpoints.up("sm")]: {
                gap: theme.spacing(5),
            },

            [theme.breakpoints.up("md")]: {
                gap: theme.spacing(6),
            },

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(8),
            },

            [theme.breakpoints.up("xl")]: {
                gap: theme.spacing(10),
            },

            [theme.breakpoints.down("md")]: {
                flexDirection: "column-reverse",
                justifyContent: "center",
                alignItems: "center",
                textAlign: "center",

                "& > :first-of-type": {
                    width: "100%",
                    flex: 1,
                },

                "& > :last-child": {
                    width: "100%",
                    flex: 1,
                },
            },
        }),
    },
};

export default styles;