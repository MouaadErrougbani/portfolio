const styles = {
    footer: (theme) => ({
        backgroundColor: theme.palette.background.paper,

        borderTop: `1px solid ${theme.palette.divider}`,

        marginTop: theme.spacing(2),

        padding: theme.spacing(3, 0),
    }),

    container: (theme) => ({
        display: "flex",

        justifyContent: "space-between",

        alignItems: "center",

        gap: theme.spacing(2),

        [theme.breakpoints.down("md")]: {
            flexDirection: "column",

            textAlign: "center",
        },
    }),

    copyright: (theme) => ({
        color: theme.palette.text.primary,

        fontWeight: 600,
    }),

    text: (theme) => ({
        color: theme.palette.text.secondary,
    }),

    iconButton: (theme) => ({
        color: theme.palette.text.secondary,

        transition: "all .3s ease",

        "&:hover": {
            color: theme.palette.primary.main,

            transform: "translateY(-3px)",
        },
    }),
};

export default styles;