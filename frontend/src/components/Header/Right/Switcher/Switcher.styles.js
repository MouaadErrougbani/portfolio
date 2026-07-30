const styles = {
    box: (theme) => ({
        display: "flex",
        alignItems: "center",
        gap: theme.spacing(1),

        "& .MuiFormControl-root": {
            minWidth: 95,
        },

        "& .MuiOutlinedInput-root": {
            height: 40,
        },

        "& .MuiSelect-select": {
            display: "flex",
            alignItems: "center",

            padding: "8px 12px !important",
        },

        "& .MuiSvgIcon-root": {
            fontSize: 20,
        },

        "& .MuiIconButton-root": {
            width: 40,
            height: 40,
        },

        [theme.breakpoints.down("sm")]: {
            "& .MuiFormControl-root": {
                minWidth: 80,
            },

            "& .MuiOutlinedInput-root": {
                height: 36,
            },

            "& .MuiIconButton-root": {
                width: 36,
                height: 36,
            },
        },
    }),
};

export default styles;