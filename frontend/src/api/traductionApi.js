import apiClient from './client';

export const getTraductions = () => {
    return apiClient('/traductions/');
};

export const getTraductionByLabel = (label) => {
    return apiClient(`/traductions/${label}`);
};
