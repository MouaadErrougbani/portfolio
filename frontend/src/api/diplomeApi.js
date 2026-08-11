import apiClient from "./client";

const getDiplomes = () => {
    return apiClient('/diplomas/');
}

export default getDiplomes;