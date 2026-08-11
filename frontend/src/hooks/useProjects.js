import { useEffect, useState } from "react";

import getProjectsApi from "../api/projectApi";


function useProjects() {

    const [projects, setProjects] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);


    useEffect(() => {

        const loadProjects = async () => {

            try {

                const data = await getProjectsApi();

                setProjects(data);

            } catch (error) {

                setError(error);

            } finally {

                setLoading(false);

            }

        };

        loadProjects();

    }, []);


    const getProjectsByDomain = (domain) => {

        return projects.filter(
            (project) => project.domain === domain
        );

    };


    const getDomains = () => {

        return [
            ...new Set(
                projects.map(
                    (project) => project.domain
                )
            )
        ];

    };


    const getSubDomainsByDomain = (domain) => {

        return [
            ...new Set(
                getProjectsByDomain(domain).flatMap(
                    (project) => project.subDomain
                )
            )
        ];

    };


    const getSubDomainsByDomains = (domains) => {

        return [
            ...new Set(
                domains.flatMap(
                    (domain) =>
                        getSubDomainsByDomain(domain)
                )
            )
        ];

    };


    const getLanguagesByDomain = (domain) => {

        return [
            ...new Set(
                getProjectsByDomain(domain).flatMap(
                    (project) => project.languages
                )
            )
        ];

    };


    const getFrameworksByLanguage = (language) => {

        return [
            ...new Set(
                projects
                    .filter(
                        (project) =>
                            project.languages.includes(language)
                    )
                    .flatMap(
                        (project) => project.frameworks
                    )
            )
        ];

    };


    return {
        projects,
        loading,
        error,

        getProjectsByDomain,
        getDomains,
        getSubDomainsByDomain,
        getSubDomainsByDomains,
        getLanguagesByDomain,
        getFrameworksByLanguage,
    };
}


export default useProjects;