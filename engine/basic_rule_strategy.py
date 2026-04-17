# dummy
from engine.recommendation_strategy import RecommendationStrategy
from models.course_recommendation import CourseRecommendation


class BasicRuleStrategy(RecommendationStrategy):
    def generate_recommendations(self, profile, courses):
        recommendations = []

        for course in courses:
            score = 0
            reasons = []

            # 1. Skill taisyklė
            if not profile.has_skill(course._skill_name):
                score = score + 40
                reasons.append("Teaches a new skill")
            else:
                score = score + 10
                reasons.append("Matches an existing skill")

            # 2. Biudžeto taisyklė
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

            # 3. Laiko taisyklė
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

            # 4. Sudėtingumo taisyklė
            if course._difficulty == "beginner":
                score = score + 10
                reasons.append("Beginner friendly")

            reason_text = ", ".join(reasons)

            recommendation = CourseRecommendation(course, score, reason_text)
            recommendations.append(recommendation)

        recommendations.sort(key=lambda recommendation: recommendation._score, reverse=True)

        return recommendations