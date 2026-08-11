import apiClient from "./client"


const getMyInfos = () => {
    return apiClient("/infos/")
}

export default getMyInfos;