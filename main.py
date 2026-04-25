from models.skill import Skill
from models.learning_profile import LearningProfile
from repository.course_repository import CourseRepository
from engine.basic_rule_strategy import BasicRuleStrategy
from engine.recommendation_engine import RecommendationEngine
from repository.profile_repository import ProfileRepository
from engine.skill_gap_strategy import SkillGapStrategy


print("Welcome to the Course Recommendation System")
print("Choose recommendation strategy:")
print("1 - Basic rule strategy")
print("2 - Skill gap strategy")

strategy_choice = input("Enter your choice: ")

if strategy_choice == "2":
    strategy = SkillGapStrategy()
else:
    strategy = BasicRuleStrategy()
print()

target_role = input("Enter your target role: ")
budget_level = input("Enter your budget level (low / medium / high): ")
weekly_hours = int(input("Enter weekly study hours: "))
skill_name = input("Enter one current skill: ")
skill_level = input("Enter your level for this skill: ")

skill = Skill(skill_name, skill_level)
profile = LearningProfile(target_role, budget_level, weekly_hours, [skill])

profile_repo = ProfileRepository("data/profiles.json")
profile_repo.save_profile(profile)

loaded_profile = profile_repo.load_profile()

print()
print("=== Loaded Profile ===")
loaded_profile.display_info()

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