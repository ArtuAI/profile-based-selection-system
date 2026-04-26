from engine.recommendation_strategy import RecommendationStrategy
from models.course_recommendation import CourseRecommendation


class SkillGapStrategy(RecommendationStrategy):
    def generate_recommendations(self, profile, courses):
        recommendations = []

        role_to_skills = {
            "data scientist": [
                "Python", "Statistics", "Machine Learning", "SQL",
                "Data Analysis", "Data Cleaning", "Model Evaluation",
                "Deep Learning", "NLP"
    ],

            "data analyst": [
                "Excel", "SQL", "Statistics", "Data Visualization",
                "Data Analysis", "Power BI", "Tableau"
    ],

            "machine learning engineer": [
                "Python", "Machine Learning", "Deep Learning",
                "Model Evaluation", "MLOps", "NLP"
    ],

            "ai engineer": [
                "Python", "Machine Learning", "Deep Learning",
                "NLP", "MLOps"
    ],

            "python developer": [
                "Python", "OOP", "Git", "Algorithms",
                "Django", "Databases"
    ],

            "software developer": [
                "Python", "OOP", "Git", "Algorithms",
                "Databases", "APIs"
    ],

            "web developer": [
                "HTML/CSS", "JavaScript", "Frontend Development",
                "Backend Development", "APIs", "React",
                "TypeScript", "Node.js", "Databases"
    ],

            "frontend developer": [
                "HTML/CSS", "JavaScript", "Frontend Development",
                "React", "TypeScript", "UI Design"
    ],

            "backend developer": [
                "Backend Development", "Python", "APIs",
                "Databases", "Django", "Node.js"
    ],

            "cybersecurity": [
                "Cybersecurity", "Network Security", "Linux",
                "Ethical Hacking", "Security Monitoring",
                "Incident Response", "Cryptography"
    ],

            "cyber security": [
                "Cybersecurity", "Network Security", "Linux",
                "Ethical Hacking", "Security Monitoring",
                "Incident Response", "Cryptography"
    ],

            "security analyst": [
                "Cybersecurity", "Network Security", "Linux",
                "Security Monitoring", "Incident Response"
    ],

            "devops": [
                "Linux", "Docker", "Cloud Computing", "DevOps",
                "AWS", "Kubernetes", "CI/CD"
    ],

            "cloud engineer": [
                "Cloud Computing", "AWS", "Linux",
                "Docker", "Kubernetes", "DevOps"
    ],

            "ui designer": [
                "UI Design", "UX Research", "Product Design"
    ],

            "ux designer": [
                "UI Design", "UX Research", "Product Design"
    ],

            "product designer": [
                "UI Design", "UX Research", "Product Design",
                "Product Strategy"
    ],

            "project manager": [
                "Project Management", "Business Analysis",
                "Technical Writing", "Agile", "Scrum",
                "Risk Management"
    ],

            "product manager": [
                "Product Management", "Product Strategy",
                "Product Analytics", "Roadmap Planning",
                "Business Analysis"
    ],

            "business analyst": [
                "Business Analysis", "Requirements Gathering",
                "Business Process Modelling", "SQL", "Excel"
    ],

            "technical writer": [
                "Technical Writing", "Documentation",
                "Documentation for Software Teams"
    ],

            "embedded engineer": [
                "Electronics", "Embedded Systems",
                "Computer Architecture", "FPGA",
                "Signal Processing"
    ],

            "electronics engineer": [
                "Electronics", "Embedded Systems",
                "Computer Architecture", "Signal Processing"
    ],

            "fpga engineer": [
                "FPGA", "Computer Architecture",
                "Electronics", "Signal Processing"
    ]
}

        target_role = profile._target_role.lower()
        needed_skills = []

        for role in role_to_skills:
            if role in target_role:
                needed_skills = role_to_skills[role]

        if len(needed_skills) == 0:
            needed_skills.append(profile._target_role)

        missing_skills = []

        for skill in needed_skills:
            if not profile.has_skill(skill):
                missing_skills.append(skill)

        for course in courses:
            score = 0
            reasons = []
            course_skill = course._skill_name.lower()

            is_missing_skill_course = False

            for missing_skill in missing_skills:
                missing_skill_lower = missing_skill.lower()

                if missing_skill_lower in course_skill or course_skill in missing_skill_lower:
                    is_missing_skill_course = True
                    score = score + 70
                    reasons.append("This course covers a missing skill")

            if is_missing_skill_course == False:
                continue

            if course._difficulty == "beginner":
                score = score + 20
                reasons.append("Good starting point")
            elif course._difficulty == "intermediate":
                score = score + 10
                reasons.append("Useful next step")

            if profile._budget_level == "low" and course._price <= 20:
                score = score + 10
                reasons.append("Fits low budget")
            elif profile._budget_level == "medium" and course._price <= 50:
                score = score + 10
                reasons.append("Fits medium budget")
            elif profile._budget_level == "high":
                score = score + 10
                reasons.append("Budget is acceptable")

            reason_text = ", ".join(reasons)

            recommendation = CourseRecommendation(course, score, reason_text)
            recommendations.append(recommendation)

        recommendations.sort(key=lambda recommendation: recommendation._score, reverse=True)

        return recommendations[:3]