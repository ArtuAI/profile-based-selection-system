from engine.recommendation_strategy import RecommendationStrategy
from models.course_recommendation import CourseRecommendation


class BasicRuleStrategy(RecommendationStrategy):
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
        wanted_skills = []

        for role in role_to_skills:
            if role in target_role:
                wanted_skills = role_to_skills[role]

        if len(wanted_skills) == 0:
            wanted_skills.append(profile._target_role)

        for course in courses:
            score = 0
            reasons = []
            course_skill = course._skill_name.lower()
            is_related = False

            for skill in wanted_skills:
                skill_lower = skill.lower()

                if skill_lower in course_skill or course_skill in skill_lower:
                    is_related = True
                    score = score + 50
                    reasons.append("Related to your target role")

            if is_related == False:
                continue

            if profile._budget_level == "low":
                if course._price <= 20:
                    score = score + 30
                    reasons.append("Fits low budget")
                elif course._price <= 50:
                    score = score + 10
                    reasons.append("Slightly above low budget")

            elif profile._budget_level == "medium":
                if course._price <= 50:
                    score = score + 20
                    reasons.append("Fits medium budget")
                else:
                    score = score + 5
                    reasons.append("More expensive than medium budget")

            elif profile._budget_level == "high":
                score = score + 20
                reasons.append("Budget is not a problem")

            if profile._weekly_hours <= 5:
                if course._duration_hours <= 10:
                    score = score + 20
                    reasons.append("Good for limited weekly time")
                else:
                    score = score + 5
                    reasons.append("May take more time")
            else:
                if course._duration_hours <= 25:
                    score = score + 10
                    reasons.append("Duration is acceptable")

            if course._difficulty == "beginner":
                score = score + 10
                reasons.append("Beginner friendly")

            reason_text = ", ".join(reasons)

            recommendation = CourseRecommendation(course, score, reason_text)
            recommendations.append(recommendation)

        recommendations.sort(key=lambda recommendation: recommendation._score, reverse=True)

        return recommendations[:5]