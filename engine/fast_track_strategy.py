from engine.recommendation_strategy import RecommendationStrategy
from models.course_recommendation import CourseRecommendation


class FastTrackStrategy(RecommendationStrategy):
    def generate_recommendations(self, profile, courses):
        recommendations = []

        for course in courses:
            score = 0
            reasons = []

            if course._duration_hours <= 10:
                score = score + 40
                reasons.append("Short course")
            elif course._duration_hours <= 20:
                score = score + 20
                reasons.append("Medium length course")
            else:
                score = score + 5
                reasons.append("Long course")

            if course._difficulty == "beginner":
                score = score + 30
                reasons.append("Easy to start")
            elif course._difficulty == "intermediate":
                score = score + 15
                reasons.append("More challenging")

            if course._price <= 20:
                score = score + 20
                reasons.append("Affordable course")
            elif course._price <= 50:
                score = score + 10
                reasons.append("Acceptable price")

            reason_text = ", ".join(reasons)

            recommendation = CourseRecommendation(course, score, reason_text)
            recommendations.append(recommendation)

        recommendations.sort(key=lambda recommendation: recommendation._score, reverse=True)

        return recommendations