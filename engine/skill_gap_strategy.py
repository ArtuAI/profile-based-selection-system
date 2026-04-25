from engine.recommendation_strategy import RecommendationStrategy
from models.course_recommendation import CourseRecommendation


class SkillGapStrategy(RecommendationStrategy):
    def generate_recommendations(self, profile, courses):
        recommendations = []

        role_to_skills = {
            "data scientist": ["Python", "Statistics", "Machine Learning", "SQL", "Data Analysis"],
            "data analyst": ["Excel", "SQL", "Statistics", "Data Visualization", "Data Analysis"],
            "web developer": ["HTML/CSS", "JavaScript", "Frontend Development", "Backend Development", "APIs"],
            "python developer": ["Python", "OOP", "Git", "Algorithms"],
            "cybersecurity": ["Cybersecurity", "Network Security", "Linux", "Ethical Hacking"],
            "cyber security": ["Cybersecurity", "Network Security", "Linux", "Ethical Hacking"],
            "devops": ["Linux", "Docker", "Cloud Computing", "DevOps"],
            "ui designer": ["UI Design", "UX Research"],
            "ux designer": ["UI Design", "UX Research"],
            "project manager": ["Project Management", "Business Analysis", "Technical Writing"]
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