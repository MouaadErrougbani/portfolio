const styles = {
    left: {
        box: (theme) => ({
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            gap: theme.spacing(2),
            width: "100%",
            maxWidth: "650px",

            [theme.breakpoints.down("md")]: {
                maxWidth: "100%",
                alignItems: "center",
                textAlign: "center",
                gap: theme.spacing(2.5),
            },

            [theme.breakpoints.up("lg")]: {
                maxWidth: "700px",
                gap: theme.spacing(3),
            },

            [theme.breakpoints.up("xl")]: {
                maxWidth: "760px",
                gap: theme.spacing(3.5),
            },
        }),

        h5: (theme) => ({
            color: theme.palette.primary.main,
            fontWeight: 600,
            letterSpacing: 1,

            fontSize: "1rem",

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.1rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.25rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.4rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.5rem",
            },
        }),

        h6: (theme) => ({
            color: theme.palette.text.primary,
            fontWeight: 700,
            lineHeight: 1.35,

            fontSize: "1.4rem",

            [theme.breakpoints.up("sm")]: {
                fontSize: "1.6rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.9rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "2.2rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "2.5rem",
            },
        }),

        body1: (theme) => ({
            color: theme.palette.text.secondary,
            lineHeight: 1.8,
            textAlign: "justify",

            fontSize: "0.95rem",

            [theme.breakpoints.down("md")]: {
                textAlign: "center",
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "1rem",
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1.05rem",
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.1rem",
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.15rem",
                lineHeight: 1.9,
            },
        }),

        button: (theme) => ({
            marginTop: theme.spacing(2),
            width: "fit-content",
            padding: `${theme.spacing(1.2)} ${theme.spacing(3)}`,
            borderRadius: theme.shape.borderRadius,
            fontWeight: 600,
            fontSize: "0.9rem",

            "& .MuiSvgIcon-root": {
                fontSize: "1.2rem",
            },

            [theme.breakpoints.down("md")]: {
                alignSelf: "center",
            },

            [theme.breakpoints.up("sm")]: {
                fontSize: "1rem",
                padding: `${theme.spacing(1.3)} ${theme.spacing(3.5)}`,

                "& .MuiSvgIcon-root": {
                    fontSize: "1.3rem",
                },
            },

            [theme.breakpoints.up("md")]: {
                fontSize: "1rem",
                padding: `${theme.spacing(1.4)} ${theme.spacing(4)}`,
            },

            [theme.breakpoints.up("lg")]: {
                fontSize: "1.05rem",
                padding: `${theme.spacing(1.5)} ${theme.spacing(4.5)}`,

                "& .MuiSvgIcon-root": {
                    fontSize: "1.4rem",
                },
            },

            [theme.breakpoints.up("xl")]: {
                fontSize: "1.1rem",
                padding: `${theme.spacing(1.7)} ${theme.spacing(5)}`,
            },
        }),
    },
};

export default styles;