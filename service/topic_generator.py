def generate_topics(interest):

    topics = {
        "python": [
            "Python Projects",
            "Flask Development",
            "Automation",
            "Data Analysis",
            "Career in Python"
        ],
        "ai": [
            "Artificial Intelligence",
            "Machine Learning",
            "Generative AI",
            "Deep Learning",
            "AI Career Opportunities"
        ],
        "data": [
            "Data Analytics",
            "Power BI",
            "SQL",
            "Data Visualization",
            "Business Intelligence"
        ]
    }

    interest = interest.lower()

    for key in topics:
        if key in interest:
            return topics[key]

    return [
        "Professional Networking",
        "Career Development",
        "Resume Building",
        "Interview Preparation",
        "Latest Technology Trends"
    ]