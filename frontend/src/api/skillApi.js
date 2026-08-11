import apiClient from "./client"


const getSkills = () => {
    return apiClient("/categories/with-skills");
};

export default getSkills;