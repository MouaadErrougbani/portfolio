const styles = {
    projects: {
        box: (theme) => ({
            backgroundColor: theme.palette.background.default,
            overflow: "hidden",

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

        stack: (theme) => ({
            display: "flex",
            flexDirection: "row",

            gap: theme.spacing(2),

            // Mobile : scroll manuel au lieu de l'animation auto
            [theme.breakpoints.down("sm")]: {
                overflowX: "auto",
                scrollSnapType: "x mandatory",
                WebkitOverflowScrolling: "touch",
                paddingBottom: theme.spacing(1),

                "& > *": {
                    scrollSnapAlign: "start",
                },

                "&::-webkit-scrollbar": {
                    display: "none",
                },
                scrollbarWidth: "none",
            },

            // Desktop / tablette : garde le marquee automatique
            [theme.breakpoints.up("sm")]: {
                animation: "projects-slider 40s linear infinite",
                gap: theme.spacing(3),

                "&:hover": {
                    animationPlayState: "paused",
                },
            },

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(4),
            },

            "@keyframes projects-slider": {
                from: {
                    transform: "translateX(0)",
                },

                to: {
                    transform: "translateX(-50%)",
                },
            },

            // Respect de l'accessibilité (motion réduite)
            "@media (prefers-reduced-motion: reduce)": {
                animation: "none",
            },
        }),

        autocomplete: (theme) => ({
            width: "100%",

            [theme.breakpoints.up("sm")]: {
                width: 280,
            },

            [theme.breakpoints.up("md")]: {
                width: 300,
            },

            [theme.breakpoints.up("xl")]: {
                width: 330,
            },
        }),

        h5: (theme) => ({
            marginTop: theme.spacing(5),
            marginBottom: theme.spacing(3),

            paddingLeft: theme.spacing(2),

            color: theme.palette.text.primary,

            fontWeight: 700,

            fontSize: "1.3rem",

            borderLeft: `5px solid ${theme.palette.primary.main}`,

            letterSpacing: 1,

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.5rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.7rem",
            },

            [theme.breakpoints.up("lg")]: {
                marginTop: theme.spacing(6),
                fontSize: "1.9rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "2.1rem",
            },
        }),
    },

    cart: {
        box: (theme) => ({
            width: 240,

            flexShrink: 0,

            display: "flex",
            flexDirection: "column",

            backgroundColor: theme.palette.background.paper,

            borderRadius: theme.shape.borderRadius * 2,

            overflow: "hidden",

            boxShadow: theme.shadows[3],

            transition: "all .3s ease",

            "&:hover": {
                transform: "translateY(-8px)",
                boxShadow: theme.shadows[8],
            },

            [theme.breakpoints.up("sm")]: {
                width: 320,
            },

            [theme.breakpoints.up("md")]: {
                width: 340,
            },

            [theme.breakpoints.up("lg")]: {
                width: 360,
            },

            [theme.breakpoints.up("xl")]: {
                width: 390,
            },
        }),

        image: (theme) => ({
            width: "100%",

            height: 170,

            objectFit: "cover",

            cursor: "pointer",

            [theme.breakpoints.up("sm")]: {
                height: 190,
            },

            [theme.breakpoints.up("md")]: {
                height: 210,
            },

            [theme.breakpoints.up("lg")]: {
                height: 220,
            },

            [theme.breakpoints.up("xl")]: {
                height: 240,
            },
        }),

        pName: (theme) => ({
            padding: theme.spacing(2, 2, 1),

            color: theme.palette.text.primary,

            fontWeight: 700,

            fontSize: "1.1rem",

            [theme.breakpoints.up("md")]: {
                fontSize: "1.2rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.3rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.4rem",
            },
        }),

        pDesc: (theme) => ({
            paddingInline: theme.spacing(2),

            color: theme.palette.text.secondary,

            lineHeight: 1.7,

            fontSize: "0.9rem",

            flexGrow: 1,

            [theme.breakpoints.up("sm")]: {
                fontSize: "0.95rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.05rem",
            },
        }),

        stack: (theme) => ({
            display: "flex",

            flexDirection: "row",

            justifyContent: "space-between",

            alignItems: "center",

            padding: theme.spacing(2),

            gap: theme.spacing(1),

            "& > button": {
                minWidth: 0,
            },
        }),

        button: (theme) => ({
            textTransform: "none",

            fontWeight: 600,

            borderRadius: theme.shape.borderRadius,

            fontSize: "0.9rem",

            overflow: "hidden",

            whiteSpace: "nowrap",

            "& span": {
                overflow: "hidden",
                textOverflow: "ellipsis",
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "0.95rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1rem",
            },

            "& svg": {
                fontSize: 20,
            },

            [theme.breakpoints.up("lg")]: {
                "& svg": {
                    fontSize: 22,
                },
            },
        }),
    },

    tags: {
        stack: (theme) => ({
            display: "flex",

            flexDirection: "row",

            flexWrap: "wrap",

            gap: theme.spacing(1),

            paddingInline: theme.spacing(2),

            marginTop: theme.spacing(2),
        }),

        p: (theme) => ({
            padding: theme.spacing(0.6, 1.5),

            borderRadius: 999,

            backgroundColor: theme.palette.primary.main,

            color: "#fff",

            fontWeight: 600,

            fontSize: "0.75rem",

            [theme.breakpoints.up("sm")]: {
                fontSize: "0.8rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "0.85rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "0.9rem",
            },
        }),
    },
};

export default styles;