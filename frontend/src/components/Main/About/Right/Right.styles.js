const styles = {
    right: {
        box: (theme) => ({
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",

            width: "100%",

            gap: theme.spacing(2),

            [theme.breakpoints.up("sm")]: {
                gap: theme.spacing(2.5),
            },

            [theme.breakpoints.up("md")]: {
                gap: theme.spacing(3),
            },

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(4),
            },

            [theme.breakpoints.down("md")]: {
                marginTop: theme.spacing(4),
            },

            [theme.breakpoints.down("sm")]: {
                marginTop: theme.spacing(3),
            },
        }),

        img: (theme) => ({
            objectFit: "cover",
            borderRadius: "50%",
            border: `5px solid ${theme.palette.primary.main}`,
            boxShadow: theme.shadows[8],
            transition: "all .3s ease",

            width: 180,
            height: 180,

            "&:hover": {
                transform: "scale(1.05)",
                boxShadow: theme.shadows[12],
            },

            [theme.breakpoints.up("sm")]: {
                width: 220,
                height: 220,
            },

            [theme.breakpoints.up("md")]: {
                width: 260,
                height: 260,
            },

            [theme.breakpoints.up("lg")]: {
                width: 300,
                height: 300,
            },

            [theme.breakpoints.up("xl")]: {
                width: 340,
                height: 340,
            },
        }),
    },

    contactItems: {
        stack: (theme) => ({
            display: "flex",
            justifyContent: "center",
            alignItems: "center",

            gap: theme.spacing(1),

            [theme.breakpoints.up("sm")]: {
                gap: theme.spacing(1.5),
            },

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(2),
            },

            "& .MuiIconButton-root": {
                width: 42,
                height: 42,

                color: theme.palette.text.primary,
                backgroundColor: theme.palette.background.paper,

                border: `1px solid ${theme.palette.divider}`,

                transition: "all .25s ease",

                "& svg": {
                    fontSize: 22,
                },

                "&:hover": {
                    color: theme.palette.primary.main,
                    backgroundColor: theme.palette.action.hover,
                    transform: "translateY(-4px)",
                    boxShadow: theme.shadows[4],
                },

                [theme.breakpoints.up("sm")]: {
                    width: 46,
                    height: 46,

                    "& svg": {
                        fontSize: 24,
                    },
                },

                [theme.breakpoints.up("md")]: {
                    width: 52,
                    height: 52,

                    "& svg": {
                        fontSize: 28,
                    },
                },

                [theme.breakpoints.up("lg")]: {
                    width: 56,
                    height: 56,

                    "& svg": {
                        fontSize: 30,
                    },
                },

                [theme.breakpoints.up("xl")]: {
                    width: 60,
                    height: 60,

                    "& svg": {
                        fontSize: 32,
                    },
                },
            },
        }),
    },
};

export default styles;