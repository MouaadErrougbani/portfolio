import apiClient from "./client"

const getContacts = () => {
    return apiClient("/contacts/")
}

export default getContacts;