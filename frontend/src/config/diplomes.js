const diplomes = [
    {
        id: 1,

        name: "Bachelor's Degree in Computer Science",

        establishment: "Sidi Mohamed Ben Abdellah University",

        startDate: "2023-09",

        endDate: "2026-06",
    },

    {
        id: 2,

        name: "Diploma in Software Development",

        establishment: "Specialized Institute of Applied Technology",

        startDate: "2021-09",

        endDate: "2023-06",
    },

    {
        id: 3,

        name: "Baccalaureate in Physical Sciences",

        establishment: "Ibn Al Khatib High School",

        startDate: "2020-09",

        endDate: "2021-06",
    },

    {
        id: 4,

        name: "Professional Certificate in Data Science",

        establishment: "Coursera",

        startDate: "2025-02",

        endDate: "2025-08",
    },
];

function getDiplomes() {
    return [...diplomes].sort(
        (a, b) => new Date(b.endDate) - new Date(a.endDate)
    );
}

export default getDiplomes;