from models.skill import Skill
from models.learning_profile import LearningProfile
from repository.course_repository import CourseRepository
from engine.basic_rule_strategy import BasicRuleStrategy
from engine.recommendation_engine import RecommendationEngine

print("Welcome to the Course Recommendation System")
print()

target_role = input("Enter your target role: ")
budget_level = input("Enter your budget level (low / medium / high): ")
weekly_hours = int(input("Enter weekly study hours: "))
skill_name = input("Enter one current skill: ")
skill_level = input("Enter your level for this skill: ")

skill = Skill(skill_name, skill_level)
profile = LearningProfile(target_role, budget_level, weekly_hours, [skill])

print()
print("=== Your Learning Profile ===")
profile.display_info()

print()
repo = CourseRepository("data/items.json")
courses = repo.load_courses()

strategy = BasicRuleStrategy()
engine = RecommendationEngine(strategy)

recommendations = engine.generate(profile, courses)

print()
print("=== Recommended Courses ===")
for recommendation in recommendations:
    recommendation.display_info()
    print()