import json
from models.learning_profile import LearningProfile
from models.skill import Skill


class ProfileRepository:
    def __init__(self, file_name):
        self._file_name = file_name

    def save_profile(self, profile):
        skills_data = []

        for skill in profile._current_skills:
            skill_data = {
                "name": skill._name,
                "level": skill._level
            }
            skills_data.append(skill_data)

        profile_data = {
            "target_role": profile._target_role,
            "budget_level": profile._budget_level,
            "weekly_hours": profile._weekly_hours,
            "current_skills": skills_data
        }

        with open(self._file_name, "w") as file:
            json.dump(profile_data, file, indent=4)

    def load_profile(self):
        with open(self._file_name, "r") as file:
            data = json.load(file)

        skills = []

        for skill_data in data["current_skills"]:
            skill = Skill(skill_data["name"], skill_data["level"])
            skills.append(skill)

        profile = LearningProfile(
            data["target_role"],
            data["budget_level"],
            data["weekly_hours"],
            skills
        )

        return profile