const styles = {
    formation: {
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

        container: (theme) => ({
            display: "flex",
            flexDirection: "column",

            gap: theme.spacing(3),

            [theme.breakpoints.up("sm")]: {
                gap: theme.spacing(4),
            },

            [theme.breakpoints.up("lg")]: {
                gap: theme.spacing(5),
            },

            [theme.breakpoints.up("xl")]: {
                gap: theme.spacing(6),
            },
        }),
    },

    diplome: {
        box: (theme) => ({
            position: "relative",

            marginLeft: theme.spacing(3),

            padding: theme.spacing(2),

            backgroundColor: theme.palette.background.default,

            borderRadius: theme.shape.borderRadius * 2,

            border: `1px solid ${theme.palette.divider}`,

            boxShadow: theme.shadows[2],

            transition: "all .3s ease",

            "&:hover": {
                transform: "translateY(-6px)",
                boxShadow: theme.shadows[6],
                borderColor: theme.palette.primary.main,
            },

            "&::before": {
                content: '""',
                position: "absolute",

                top: 0,
                bottom: 0,

                left: "-20px",

                width: "3px",

                backgroundColor: theme.palette.primary.main,
            },

            "&::after": {
                content: '""',

                position: "absolute",

                left: "-28px",
                top: "28px",

                width: "16px",
                height: "16px",

                borderRadius: "50%",

                backgroundColor: theme.palette.primary.main,

                border: `3px solid ${theme.palette.background.default}`,
            },

            [theme.breakpoints.up("sm")]: {
                marginLeft: theme.spacing(4),
                padding: theme.spacing(2.5),

                "&::before": {
                    left: "-25px",
                },

                "&::after": {
                    left: "-33px",
                },
            },

            [theme.breakpoints.up("md")]: {
                marginLeft: theme.spacing(5),
                padding: theme.spacing(3),

                "&::before": {
                    left: "-30px",
                },

                "&::after": {
                    left: "-38px",
                    width: "18px",
                    height: "18px",
                },
            },

            [theme.breakpoints.up("lg")]: {
                padding: theme.spacing(3.5),
            },

            [theme.breakpoints.up("xl")]: {
                marginLeft: theme.spacing(6),
                padding: theme.spacing(4),
            },
        }),

        h3: (theme) => ({
            color: theme.palette.text.primary,

            fontWeight: 700,

            fontSize: "1.2rem",

            marginBottom: theme.spacing(1),

            lineHeight: 1.4,

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.35rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.5rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.7rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.9rem",
            },
        }),

        h4: (theme) => ({
            color: theme.palette.primary.main,

            fontWeight: 600,

            fontSize: "1rem",

            marginBottom: theme.spacing(1),

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.05rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.15rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.25rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.35rem",
            },
        }),

        h5: (theme) => ({
            color: theme.palette.text.secondary,

            fontWeight: 500,

            fontSize: "0.9rem",

            [theme.breakpoints.up("sm")]: {
                fontSize: "0.95rem",
            },

            [theme.breakpoints.up("md")]: {
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
};

export default styles;