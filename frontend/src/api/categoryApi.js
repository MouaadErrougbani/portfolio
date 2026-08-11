import apiClient from "./client"


const getCategories = () => {

    return apiClient("/categories/");
};

export default getCategories;