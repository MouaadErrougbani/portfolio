import apiClient from "./client"


const getNavigations = () => {
    return apiClient('/navigations/')
}

export default getNavigations;