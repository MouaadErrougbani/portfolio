import {
    Autocomplete,
    Box,
    Container,
    Stack,
    TextField,
    Typography,
} from "@mui/material";

import CheckBoxOutlineBlankIcon from "@mui/icons-material/CheckBoxOutlineBlank";
import CheckBoxIcon from "@mui/icons-material/CheckBox";

import { useMemo, useState } from "react";

import Section from "../Section";
import Cart from "./Cart";
import styles from "./Projets.styles";

import useProjects from "../../../hooks/useProjects";



function Filter({
    list,
    label,
    value,
    onChange,
}) {

    return (
        <Autocomplete
            multiple
            options={list}
            value={value}
            onChange={(event, newValue) => onChange(newValue)}
            disableCloseOnSelect
            getOptionLabel={(option) => option}

            renderOption={(props, option, { selected }) => {

                const { key, ...optionProps } = props;

                const SelectionIcon = selected
                    ? CheckBoxIcon
                    : CheckBoxOutlineBlankIcon;

                return (
                    <li key={key} {...optionProps}>

                        <SelectionIcon
                            fontSize="small"
                            style={{
                                marginRight: 8,
                                padding: 9,
                                boxSizing: "content-box",
                            }}
                        />

                        {option}

                    </li>
                );
            }}

            sx={styles.projects.autocomplete}

            renderInput={(params) => (
                <TextField
                    {...params}
                    label={label}
                />
            )}
        />
    );
}



function Projets() {

    /*
    |--------------------------------------------------------------------------
    | Projects
    |--------------------------------------------------------------------------
    */

    const {
        projects,
        loading,
        error,
        getDomains,
        getSubDomainsByDomains,
        getLanguagesByDomain,
        getFrameworksByLanguage,
    } = useProjects();


    /*
    |--------------------------------------------------------------------------
    | Selected filters
    |--------------------------------------------------------------------------
    */

    const [selectedDomains, setSelectedDomains] = useState([]);

    const [selectedSubDomains, setSelectedSubDomains] = useState([]);

    const [selectedLanguages, setSelectedLanguages] = useState([]);

    const [selectedFrameworks, setSelectedFrameworks] = useState([]);



    /*
    |--------------------------------------------------------------------------
    | Domains
    |--------------------------------------------------------------------------
    */

    const domains = useMemo(() => {

        return getDomains();

    }, [projects]);



    /*
    |--------------------------------------------------------------------------
    | SubDomains
    |--------------------------------------------------------------------------
    */

    const subDomains = useMemo(() => {

        return getSubDomainsByDomains(domains);

    }, [
        projects,
        domains,
    ]);



    /*
    |--------------------------------------------------------------------------
    | Languages
    |--------------------------------------------------------------------------
    */

    const languages = useMemo(() => {

        /*
        | No domain selected
        |
        | Show all languages
        */

        if (selectedDomains.length === 0) {

            return [
                ...new Set(
                    projects.flatMap(
                        (project) => project.languages
                    )
                ),
            ];
        }


        /*
        | Domains selected
        |
        | Show languages belonging
        | to the selected domains
        */

        return [
            ...new Set(
                selectedDomains.flatMap(
                    (domain) =>
                        getLanguagesByDomain(domain)
                )
            ),
        ];

    }, [
        projects,
        selectedDomains,
    ]);



    /*
    |--------------------------------------------------------------------------
    | Frameworks
    |--------------------------------------------------------------------------
    */

    const frameWorks = useMemo(() => {

        /*
        | No language selected
        |
        | Show all frameworks
        */

        if (selectedLanguages.length === 0) {

            return [
                ...new Set(
                    projects.flatMap(
                        (project) => project.frameworks
                    )
                ),
            ];
        }


        /*
        | Languages selected
        |
        | Show frameworks belonging
        | to the selected languages
        */

        return [
            ...new Set(
                selectedLanguages.flatMap(
                    (language) =>
                        getFrameworksByLanguage(language)
                )
            ),
        ];

    }, [
        projects,
        selectedLanguages,
    ]);



    /*
    |--------------------------------------------------------------------------
    | Filter Projects
    |--------------------------------------------------------------------------
    */

    const filteredProjects = useMemo(() => {

        return projects.filter((project) => {

            /*
            | Domain
            */

            const matchesDomain =
                selectedDomains.length === 0 ||
                selectedDomains.includes(project.domain);


            /*
            | SubDomain
            */

            const matchesSubDomain =
                selectedSubDomains.length === 0 ||
                project.subDomain.some(
                    (subDomain) =>
                        selectedSubDomains.includes(subDomain)
                );


            /*
            | Language
            */

            const matchesLanguage =
                selectedLanguages.length === 0 ||
                project.languages.some(
                    (language) =>
                        selectedLanguages.includes(language)
                );


            /*
            | Framework
            */

            const matchesFramework =
                selectedFrameworks.length === 0 ||
                project.frameworks.some(
                    (framework) =>
                        selectedFrameworks.includes(framework)
                );


            /*
            | Final result
            */

            return (
                matchesDomain &&
                matchesSubDomain &&
                matchesLanguage &&
                matchesFramework
            );

        });

    }, [
        projects,
        selectedDomains,
        selectedSubDomains,
        selectedLanguages,
        selectedFrameworks,
    ]);



    /*
    |--------------------------------------------------------------------------
    | Group Projects By Domain
    |--------------------------------------------------------------------------
    */

    const groupedProjects = useMemo(() => {

        return domains.map((domain) => ({

            domain,

            projects: filteredProjects.filter(
                (project) =>
                    project.domain === domain
            ),

        }));

    }, [
        domains,
        filteredProjects,
    ]);



    /*
    |--------------------------------------------------------------------------
    | Loading
    |--------------------------------------------------------------------------
    */

    if (loading) {

        return (
            <Box
                component="section"
                sx={styles.projects.box}
            >

                <Container maxWidth="lg">

                    <Section label="Projects" />

                    <Typography
                        sx={{
                            mt: 4,
                            textAlign: "center",
                        }}
                    >
                        Loading projects...
                    </Typography>

                </Container>

            </Box>
        );
    }



    /*
    |--------------------------------------------------------------------------
    | Error
    |--------------------------------------------------------------------------
    */

    if (error) {

        return (
            <Box
                component="section"
                sx={styles.projects.box}
            >

                <Container maxWidth="lg">

                    <Section label="Projects" />

                    <Typography
                        sx={{
                            mt: 4,
                            textAlign: "center",
                        }}
                    >
                        Failed to load projects.
                    </Typography>

                </Container>

            </Box>
        );
    }



    /*
    |--------------------------------------------------------------------------
    | Render
    |--------------------------------------------------------------------------
    */

    return (

        <Box
            component="section"
            sx={styles.projects.box}
        >

            <Container maxWidth="lg">

                <Section label="Projects" />



                {/* ==========================================================
                    Filters
                ========================================================== */}

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



                {/* ==========================================================
                    Projects
                ========================================================== */}

                {
                    groupedProjects.map(
                        ({ domain, projects: projectsList }) => {

                            /*
                            | Don't render empty domains
                            */

                            if (projectsList.length === 0) {
                                return null;
                            }


                            return (

                                <Box key={domain}>

                                    {/* --------------------------------------
                                        Domain title
                                    -------------------------------------- */}

                                    <Typography
                                        sx={styles.projects.h5}
                                        component="h5"
                                        variant="h5"
                                    >
                                        {domain}
                                    </Typography>



                                    {/* --------------------------------------
                                        Projects slider
                                    -------------------------------------- */}

                                    <Box
                                        sx={styles.projects.slider}
                                    >

                                        <Stack
                                            sx={styles.projects.stack}
                                        >

                                            {
                                                [
                                                    ...projectsList,
                                                    ...projectsList,
                                                ].map(
                                                    (project, index) => (

                                                        <Cart
                                                            key={`${project.id}-${index}`}
                                                            project={project}
                                                        />

                                                    )
                                                )
                                            }

                                        </Stack>

                                    </Box>

                                </Box>

                            );
                        }
                    )
                }

            </Container>

        </Box>

    );
}


export default Projets;

