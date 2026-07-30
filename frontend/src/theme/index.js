import { createTheme } from "@mui/material/styles";

import palette from "./palette";
import typography from "./typography";
import breakpoints from "./breakpoints";
import components from "./components";

const getTheme = (mode) =>
  createTheme({
    palette: palette(mode),
    typography,
    components,
    breakpoints,
  });

export default getTheme;