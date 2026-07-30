const styles = {
    contact: {
        container: (theme) => ({
            marginTop: theme.spacing(6),
            marginBottom: theme.spacing(6),

            [theme.breakpoints.up("sm")]: {
                marginTop: theme.spacing(7),
                marginBottom: theme.spacing(7),
            },

            [theme.breakpoints.up("md")]: {
                marginTop: theme.spacing(8),
                marginBottom: theme.spacing(8),
            },

            [theme.breakpoints.up("lg")]: {
                marginTop: theme.spacing(10),
                marginBottom: theme.spacing(10),
            },

            [theme.breakpoints.up("xl")]: {
                marginTop: theme.spacing(12),
                marginBottom: theme.spacing(12),
            },
        }),

        box: (theme) => ({
            display: "grid",

            gridTemplateColumns: "1fr 1fr",

            gap: theme.spacing(6),

            alignItems: "stretch",

            "& > *": {
                height: "100%",
            },

            [theme.breakpoints.down("md")]: {
                gridTemplateColumns: "1fr",
            },
        }),
    },

    left: {
        box: (theme) => ({
            display: "flex",
            flexDirection: "column",

            gap: theme.spacing(2),
            height: "100%",
            justifyContent: "space-between", 

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(2.5),
            },
        }),

        boxContact: (theme) => ({
            display: "flex",
            alignItems: "center",

            gap: theme.spacing(2),

            padding: theme.spacing(2),

            borderRadius: theme.shape.borderRadius * 2,

            backgroundColor: theme.palette.background.paper,

            border: `1px solid ${theme.palette.divider}`,

            boxShadow: theme.shadows[1],

            transition: "all .3s ease",

            "&:hover": {
                transform: "translateX(6px)",
                borderColor: theme.palette.primary.main,
                boxShadow: theme.shadows[4],
            },

            "& svg": {
                color: theme.palette.primary.main,
                fontSize: 24,
            },

            [theme.breakpoints.up("sm")]: {
                "& svg": {
                    fontSize: 26,
                },
            },

            [theme.breakpoints.up("md")]: {
                "& svg": {
                    fontSize: 28,
                },
            },

            [theme.breakpoints.up("lg")]: {
                padding: theme.spacing(2.5),

                "& svg": {
                    fontSize: 30,
                },
            },

            [theme.breakpoints.up("xl")]: {
                padding: theme.spacing(3),

                "& svg": {
                    fontSize: 34,
                },
            },
        }),

        p: (theme) => ({
            color: theme.palette.text.primary,
            fontWeight: 500,
            wordBreak: "break-word",

            fontSize: "0.95rem",

            [theme.breakpoints.up("sm")]: {
                fontSize: "1rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.05rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.1rem",
            },
        }),
    },

    right: {
        box: (theme) => ({
            display: "flex",
            flexDirection: "column",
            height: "100%",
            gap: theme.spacing(2),

            padding: theme.spacing(2.5),

            backgroundColor: theme.palette.background.paper,

            border: `1px solid ${theme.palette.divider}`,

            borderRadius: theme.shape.borderRadius * 2,

            boxShadow: theme.shadows[2],

            [theme.breakpoints.up("md")]: {
                padding: theme.spacing(3),
            },

            [theme.breakpoints.up("lg")]: {
                padding: theme.spacing(4),
            },

            [theme.breakpoints.up("xl")]: {
                padding: theme.spacing(5),
            },
        }),

        p: (theme) => ({
            color: theme.palette.text.primary,
            fontWeight: 700,

            fontSize: "1.25rem",

            marginBottom: theme.spacing(1),

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.4rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.6rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.8rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "2rem",
            },
        }),

        input: (theme) => ({
            border: `1px solid ${theme.palette.divider}`,
            borderRadius: theme.shape.borderRadius,

            padding: theme.spacing(1.5),

            backgroundColor: theme.palette.background.default,

            color: theme.palette.text.primary,

            fontSize: "0.95rem",

            outline: "none",

            transition: "all .25s ease",

            "&:focus": {
                borderColor: theme.palette.primary.main,
                boxShadow: `0 0 0 2px ${theme.palette.primary.main}20`,
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "1rem",
            },

            [theme.breakpoints.up("lg")]: {
                padding: theme.spacing(1.8),
            },
        }),

        textarea: (theme) => ({
            border: `1px solid ${theme.palette.divider}`,
            borderRadius: theme.shape.borderRadius,

            padding: theme.spacing(1.5),

            backgroundColor: theme.palette.background.default,

            color: theme.palette.text.primary,

            fontSize: "0.95rem",

            minHeight: 160,

            resize: "vertical",

            outline: "none",

            transition: "all .25s ease",

            "&:focus": {
                borderColor: theme.palette.primary.main,
                boxShadow: `0 0 0 2px ${theme.palette.primary.main}20`,
            },

            [theme.breakpoints.up("sm")]: {
                minHeight: 180,
                fontSize: "1rem",
            },

            [theme.breakpoints.up("lg")]: {
                minHeight: 220,
                padding: theme.spacing(1.8),
            },

            [theme.breakpoints.up("xl")]: {
                minHeight: 260,
            },
        }),

        button: (theme) => ({
            alignSelf: "flex-start",

            marginTop: theme.spacing(1),

            padding: `${theme.spacing(1.2)} ${theme.spacing(3.5)}`,

            borderRadius: theme.shape.borderRadius,

            fontWeight: 600,

            textTransform: "none",

            fontSize: "0.95rem",

            [theme.breakpoints.down("sm")]: {
                width: "100%",
                alignSelf: "stretch",
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "1rem",
            },

            [theme.breakpoints.up("lg")]: {
                padding: `${theme.spacing(1.5)} ${theme.spacing(5)}`,
                fontSize: "1.05rem",
            },

            [theme.breakpoints.up("xl")]: {
                padding: `${theme.spacing(1.7)} ${theme.spacing(6)}`,
                fontSize: "1.1rem",
            },
        }),
    },
};

export default styles;