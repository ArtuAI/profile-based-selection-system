import unittest
import os

from models.skill import Skill
from models.learning_profile import LearningProfile
from repository.profile_repository import ProfileRepository


class TestProfileRepository(unittest.TestCase):
    def test_save_and_load_profile(self):
        test_file = "data/test_profiles.json"

        skill = Skill("Python", "beginner")
        profile = LearningProfile("Data Scientist", "low", 10, [skill])

        repo = ProfileRepository(test_file)
        repo.save_profile(profile)

        loaded_profile = repo.load_profile()

        self.assertEqual(loaded_profile._target_role, "Data Scientist")
        self.assertEqual(loaded_profile._budget_level, "low")
        self.assertEqual(loaded_profile._weekly_hours, 10)
        self.assertTrue(loaded_profile.has_skill("Python"))

        if os.path.exists(test_file):
            os.remove(test_file)


if __name__ == "__main__":
    unittest.main()