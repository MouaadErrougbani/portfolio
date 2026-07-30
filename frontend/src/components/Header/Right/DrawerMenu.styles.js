const styles = {
    menuButton: (theme) => ({
        display: "flex",

        color: theme.palette.text.primary,

        [theme.breakpoints.up("lg")]: {
            display: "none",
        },
    }),

    drawer: (theme) => ({
        width: 290,

        backgroundColor: theme.palette.background.paper,

        color: theme.palette.text.primary,
    }),

    content: (theme) => ({
        display: "flex",
        flexDirection: "column",

        height: "100%",

        padding: theme.spacing(3),

        gap: theme.spacing(2),
    }),

    logo: (theme) => ({
        display: "flex",

        justifyContent: "center",

        alignItems: "center",

        paddingBottom: theme.spacing(1),
    }),

    list: (theme) => ({
        display: "flex",

        flexDirection: "column",

        gap: theme.spacing(0.5),

        flexGrow: 1,
    }),

    item: (theme) => ({
        borderRadius: theme.shape.borderRadius,

        transition: "all .25s ease",

        "&:hover": {
            backgroundColor: theme.palette.action.hover,

            color: theme.palette.primary.main,

            transform: "translateX(6px)",
        },

        "& .MuiTypography-root": {
            fontWeight: 500,
            fontSize: "1rem",
        },
    }),

    switchers: (theme) => ({
        display: "flex",

        justifyContent: "space-between",

        alignItems: "center",

        gap: theme.spacing(2),

        marginTop: theme.spacing(1),
    }),
};

export default styles;