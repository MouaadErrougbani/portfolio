import apiClient from "./client"


const getLanguages = () => {
    return apiClient("/languages/")
}

export default getLanguages;