import { Autocomplete, Box, Container, Stack, TextField, Typography } from "@mui/material";
import Section from "../Section";
import getProjects, {getDomains, getProjectsByDomain, getSubDomainsByDomain,
    getSubDomainsByDomains, getLanguagesByDomain, getFrameworksByLanguage} 
    from "../../../config/projects";
import Cart from "./Cart";
import styles from "./Projets.styles";
import { useEffect, useState } from "react";
import CheckBoxOutlineBlankIcon from '@mui/icons-material/CheckBoxOutlineBlank';
import CheckBoxIcon from '@mui/icons-material/CheckBox';



function Filter({
        list,
        label,
        value,
        onChange,
    }) {

    return(
        <Autocomplete
            multiple
            options={list}
            value={value}
            onChange={(event, newValue) => onChange(newValue)}
            disableCloseOnSelect
            getOptionLabel={(option) => option}
 
            renderOption={(props, option, { selected }) => {
                const { key, ...optionProps } = props;
                const SelectionIcon = selected ? CheckBoxIcon : CheckBoxOutlineBlankIcon
                return (
                <li key={key} {...optionProps}>
                    <SelectionIcon
                    fontSize="small"
                    style={{ marginRight: 8, padding: 9, boxSizing: 'content-box' }}
                    />
                    {option}
                </li>
                );
            }}
            sx={styles.projects.autocomplete}
            renderInput={(params) => (
                <TextField {...params} label={label} />
            )}
        />
    )
}


function Projets(){
    const [domains, setDomains] = useState([])
    const [subDomains, setSubDomains] = useState([])
    const [languages, setLanguages] = useState([])
    const [frameWorks, setFrameWorks] = useState([])
    const [projects, setProjects] = useState([])
    const [selectedDomains, setSelectedDomains] = useState([]);
    const [selectedSubDomains, setSelectedSubDomains] = useState([]);
    const [selectedLanguages, setSelectedLanguages] = useState([]);
    const [selectedFrameworks, setSelectedFrameworks] = useState([]);


    useEffect(() => {
        const tempDomains = getDomains();
        const tempLanguages = getLanguagesByDomain(tempDomains[1])
        setProjects(getProjects())
        setDomains(tempDomains);
        setSubDomains(getSubDomainsByDomains(tempDomains));
        setLanguages(tempLanguages)
        setFrameWorks(getFrameworksByLanguage(tempLanguages[0]))
        
    }, []);

    const filteredProjects = projects.filter((project) => {

        if (
            selectedDomains.length > 0 &&
            !selectedDomains.includes(project.domain)
        ) {
            return false;
        }

        if (
            selectedSubDomains.length > 0 &&
            !project.subDomain.some(sub =>
                selectedSubDomains.includes(sub)
            )
        ) {
            return false;
        }

        if (
            selectedLanguages.length > 0 &&
            !project.languages.some(language =>
                selectedLanguages.includes(language)
            )
        ) {
            return false;
        }

        if (
            selectedFrameworks.length > 0 &&
            !project.frameworks.some(framework =>
                selectedFrameworks.includes(framework)
            )
        ) {
            return false;
        }

        return true;
    });

    const groupedProjects = domains.map((domain) => ({
        [domain]: filteredProjects.filter(
            (project) => project.domain === domain
        ),
    }));

    return (
        <Box component="section" sx={styles.projects.box}>
            <Container maxWidth="lg" >
                <Section label="Projets"/>
                <Box
                    sx={{
                        display: "flex",
                        flexWrap: "wrap",
                        gap: 2,
                        mt: 4,
                        mb: 5,
                        justifyContent: "center",

                        "& > *": {
                            flex: {
                                xs: "1 1 100%",
                                sm: "1 1 calc(50% - 8px)",
                                md: "1 1 calc(50% - 8px)",
                                lg: "0 0 auto",
                            },
                        },
                    }}
                >
                    <Filter
                        list={domains}
                        label="Domains"
                        value={selectedDomains}
                        onChange={setSelectedDomains}
                    />

                    <Filter
                        list={subDomains}
                        label="SubDomains"
                        value={selectedSubDomains}
                        onChange={setSelectedSubDomains}
                    />

                    <Filter
                        list={languages}
                        label="Languages"
                        value={selectedLanguages}
                        onChange={setSelectedLanguages}
                    />

                    <Filter
                        list={frameWorks}
                        label="Frameworks"
                        value={selectedFrameworks}
                        onChange={setSelectedFrameworks}
                    />
                </Box>
                {
                    groupedProjects.map((item) => {
                        const [[domain, projectsList]] = Object.entries(item);

                        return (
                            <Box key={domain}>
                                {
                                    projectsList.length > 0 &&
                                    <Typography sx={styles.projects.h5} component="h5" variant="h5">
                                        {domain}
                                    </Typography>
                                }

                                <Box sx={styles.projects.slider}>
                                    <Stack sx={styles.projects.stack}>
                                        {[...projectsList, ...projectsList].map((project, index) => (
                                            <Cart
                                                key={`${project.id}-${index}`}
                                                project={project}
                                            />
                                        ))}
                                    </Stack>
                                </Box>
                            </Box>
                        );
                    })
                }
            </Container>
        </Box>
    )
}

export default Projets;