const projects = [
    {
        id: 1,

        name: "Personal Portfolio",

        description:
            "A modern and responsive portfolio website showcasing my projects, skills, education, and contact information.",

        tags: [
            "Portfolio",
            "Responsive",
            "Dark Mode"
        ],

        githubLink: "https://github.com/username/portfolio",

        productionLink: "https://portfolio.example.com",

        realizationDate: "2026-07-15",

        domain: "Web Development",

        subDomain: [
            "Frontend"
        ],

        keywords: [
            "Portfolio",
            "Personal Website",
            "Responsive Design",
            "Dark Mode"
        ],

        languages: [
            "JavaScript"
        ],

        frameworks: [
            "React",
            "Material UI",
            "React Router",
            "i18next"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },

    {
        id: 2,

        name: "Weather Forecast App",

        description:
            "A responsive weather application that provides real-time weather information and forecasts using a REST API.",

        tags: [
            "Weather",
            "API",
            "Responsive"
        ],

        githubLink: "https://github.com/username/weather-app",

        productionLink: "https://weather.example.com",

        realizationDate: "2026-06-20",

        domain: "Web Development",

        subDomain: [
            "Frontend"
        ],

        keywords: [
            "Weather",
            "Forecast",
            "REST API",
            "Geolocation"
        ],

        languages: [
            "JavaScript"
        ],

        frameworks: [
            "React",
            "Material UI",
            "Axios"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },

    {
        id: 3,

        name: "Task Management API",

        description:
            "A RESTful backend API for managing tasks with authentication, authorization, and CRUD operations.",

        tags: [
            "REST API",
            "Authentication",
            "Backend"
        ],

        githubLink: "https://github.com/username/task-api",

        productionLink: "https://api.example.com",

        realizationDate: "2026-05-12",

        domain: "Web Development",

        subDomain: [
            "Backend"
        ],

        keywords: [
            "REST",
            "JWT",
            "CRUD",
            "Authentication"
        ],

        languages: [
            "JavaScript"
        ],

        frameworks: [
            "Node.js",
            "Express.js",
            "PostgreSQL"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },

    {
        id: 4,

        name: "House Price Prediction",

        description:
            "A machine learning project that predicts house prices using real estate data collected through web scraping.",

        tags: [
            "Machine Learning",
            "Regression",
            "Data Science"
        ],

        githubLink: "https://github.com/username/house-price-prediction",

        productionLink: "",

        realizationDate: "2026-04-18",

        domain: "Artificial Intelligence",

        subDomain: [
            "Machine Learning"
        ],

        keywords: [
            "Regression",
            "Prediction",
            "Feature Engineering",
            "EDA"
        ],

        languages: [
            "Python"
        ],

        frameworks: [
            "Pandas",
            "NumPy",
            "Scikit-learn",
            "Matplotlib"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },

    {
        id: 5,

        name: "Customer Sentiment Analysis",

        description:
            "A Natural Language Processing project that classifies customer reviews into positive, negative, or neutral sentiments.",

        tags: [
            "NLP",
            "Deep Learning",
            "Text Classification"
        ],

        githubLink: "https://github.com/username/sentiment-analysis",

        productionLink: "",

        realizationDate: "2026-03-08",

        domain: "Artificial Intelligence",

        subDomain: [
            "Natural Language Processing",
            "Deep Learning"
        ],

        keywords: [
            "Sentiment Analysis",
            "Text Classification",
            "Transformer",
            "BERT"
        ],

        languages: [
            "Python"
        ],

        frameworks: [
            "PyTorch",
            "Transformers",
            "NLTK"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    },

    {
        id: 6,

        name: "Image Classification",

        description:
            "A deep learning application for classifying images into multiple categories using convolutional neural networks.",

        tags: [
            "Computer Vision",
            "Deep Learning",
            "CNN"
        ],

        githubLink: "https://github.com/username/image-classification",

        productionLink: "",

        realizationDate: "2026-02-14",

        domain: "Artificial Intelligence",

        subDomain: [
            "Computer Vision",
            "Deep Learning"
        ],

        keywords: [
            "CNN",
            "Image Classification",
            "Computer Vision",
            "Neural Networks"
        ],

        languages: [
            "Python"
        ],

        frameworks: [
            "TensorFlow",
            "Keras",
            "OpenCV"
        ],
        image : "https://images.unsplash.com/photo-1764352104218-2d3a899ce36c?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

    }
];

export function getProjectsByDomain(domain){
    return projects.filter((project)=> project.domain === domain)
}

export function getDomains() {
    return [...new Set(projects.map((project) => project.domain))];
}

export function getSubDomainsByDomain(domain) {
    return [
        ...new Set(
            getProjectsByDomain(domain).flatMap(
                (project) => project.subDomain
            )
        ),
    ];
}

export function getSubDomainsByDomains(domains) {
    return [
        ...new Set(domains.flatMap((domain) => getSubDomainsByDomain(domain) )),
    ];
}

export function getLanguagesByDomain(domain){
    return [
        ...new Set(
            getProjectsByDomain(domain).flatMap(
                (project) => project.languages
            )
        ),
    ];
}

export function getFrameworksByLanguage(language) {
    return [
        ...new Set(
            projects
                .filter((project) => project.languages.includes(language))
                .flatMap((project) => project.frameworks)
        ),
    ];
}

function getProjects(){
    return projects;
}

export default getProjects;