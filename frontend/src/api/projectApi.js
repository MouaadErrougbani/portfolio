import apiClient from "./client"


const getProjects = () => {
    return apiClient("/projects/with-details");
};

export default getProjects;