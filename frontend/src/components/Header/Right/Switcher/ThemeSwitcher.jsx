import { Brightness4, Brightness7 } from "@mui/icons-material";
import { FormControl, IconButton, MenuItem, Select } from "@mui/material";
import useAppTheme from '../../../../context/useAppTheme'
import getTypeThemes from "../../../../config/typeThemes";
import { useEffect } from "react";


function ThemeSwitcher(){
    const {mode, setMode, toggleTheme} = useAppTheme()

    const typeThemes = getTypeThemes()

    return(
        <>
            { typeThemes.length <= 2 ?

                <IconButton 
                onClick={toggleTheme}
                >
                    {mode === "dark" ?
                        <Brightness7/> :
                        <Brightness4/>
                    } 
                </IconButton> 
                :
                <FormControl size="small">
                    <Select
                        value={mode}
                        onChange={(e)=> setMode(e.target.value.toLowerCase())}
                    >
                        {
                            typeThemes.map((item, index) => (<MenuItem key={index} value={item.toLowerCase()}>{item}</MenuItem> ))
                        }
                    </Select>
                </FormControl> 
            }
        </>
    )
}

export default ThemeSwitcher;