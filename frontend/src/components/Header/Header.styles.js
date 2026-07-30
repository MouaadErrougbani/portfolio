const styles = {
    header: (theme) => ({
        position: "sticky",

        top: 0,

        zIndex: theme.zIndex.appBar,

        backdropFilter: "blur(18px)",

        WebkitBackdropFilter: "blur(18px)",

        backgroundColor:
            theme.palette.mode === "dark"
                ? "rgba(30,30,30,.82)"
                : "rgba(255,255,255,.82)",

        borderBottom: `1px solid ${theme.palette.divider}`,

        transition: "all .3s ease",
    }),

    container: (theme) => ({
        display: "flex",

        alignItems: "center",

        justifyContent: "space-between",

        minHeight: 60,

        paddingTop: theme.spacing(1),

        paddingBottom: theme.spacing(1),

        [theme.breakpoints.up("sm")]: {
            minHeight: 68,
            paddingTop: theme.spacing(1.5),
            paddingBottom: theme.spacing(1.5),
        },

        [theme.breakpoints.up("md")]: {
            minHeight: 74,
        },

        [theme.breakpoints.up("lg")]: {
            minHeight: 82,
        },

        [theme.breakpoints.up("xl")]: {
            minHeight: 90,
        },
    }),
};

export default styles;