const styles = {
    box: (theme) => ({
        backgroundColor: theme.palette.background.paper,

        paddingTop: theme.spacing(6),
        paddingBottom: theme.spacing(6),

        [theme.breakpoints.up("sm")]: {
            paddingTop: theme.spacing(7),
            paddingBottom: theme.spacing(7),
        },

        [theme.breakpoints.up("md")]: {
            paddingTop: theme.spacing(8),
            paddingBottom: theme.spacing(8),
        },

        [theme.breakpoints.up("lg")]: {
            paddingTop: theme.spacing(10),
            paddingBottom: theme.spacing(10),
        },

        [theme.breakpoints.up("xl")]: {
            paddingTop: theme.spacing(12),
            paddingBottom: theme.spacing(12),
        },
    }),

    slider: {
        overflow: "hidden",
        width: "100%",
    },

    track: (theme) => ({
        display: "flex",
        flexDirection: "row",
        width: "max-content",

        gap: theme.spacing(2),

        animation: "skills-slider 30s linear infinite",

        "&:hover": {
            animationPlayState: "paused",
        },

        "@keyframes skills-slider": {
            from: {
                transform: "translateX(0)",
            },

            to: {
                transform: "translateX(-50%)",
            },
        },

        [theme.breakpoints.up("lg")]: {
            gap: theme.spacing(3),
        },

        [theme.breakpoints.up("xl")]: {
            gap: theme.spacing(4),
        },
    }),

    item: (theme) => ({
        minWidth: 140,

        padding: theme.spacing(1.5, 2),

        display: "flex",
        justifyContent: "center",
        alignItems: "center",

        borderRadius: theme.shape.borderRadius * 2,

        backgroundColor: theme.palette.background.default,

        color: theme.palette.text.primary,

        textAlign: "center",

        fontWeight: 600,

        fontSize: "0.9rem",

        boxShadow: theme.shadows[2],

        transition: "all .3s ease",

        flexShrink: 0,

        "&:hover": {
            transform: "translateY(-4px)",
            boxShadow: theme.shadows[6],
            backgroundColor: theme.palette.primary.main,
            color: theme.palette.primary.contrastText,
        },

        [theme.breakpoints.up("sm")]: {
            minWidth: 160,
            fontSize: "0.95rem",
        },

        [theme.breakpoints.up("md")]: {
            minWidth: 180,
            padding: theme.spacing(2),
            fontSize: "1rem",
        },

        [theme.breakpoints.up("lg")]: {
            minWidth: 210,
            padding: theme.spacing(2.2),
            fontSize: "1.05rem",
        },

        [theme.breakpoints.up("xl")]: {
            minWidth: 240,
            padding: theme.spacing(2.5),
            fontSize: "1.1rem",
        },
    }),

    typography: (theme) => ({
        marginTop: theme.spacing(5),
        marginBottom: theme.spacing(2),

        color: theme.palette.primary.main,

        fontWeight: 700,

        fontSize: "1.2rem",

        letterSpacing: 0.5,

        textTransform: "capitalize",

        borderLeft: `4px solid ${theme.palette.primary.main}`,

        paddingLeft: theme.spacing(2),

        [theme.breakpoints.up("sm")]: {
            fontSize: "1.35rem",
        },

        [theme.breakpoints.up("md")]: {
            fontSize: "1.5rem",
        },

        [theme.breakpoints.up("lg")]: {
            marginTop: theme.spacing(6),
            marginBottom: theme.spacing(3),
            fontSize: "1.7rem",
        },

        [theme.breakpoints.up("xl")]: {
            fontSize: "1.9rem",
        },

        [theme.breakpoints.down("md")]: {
            display: "table",

            marginLeft: "auto",
            marginRight: "auto",

            textAlign: "center",

            borderLeft: "none",

            borderBottom: `3px solid ${theme.palette.primary.main}`,

            paddingLeft: 0,

            paddingBottom: theme.spacing(0.75),
        },
    }),
};

export default styles;