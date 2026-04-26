import unittest
from models.skill import Skill
from models.learning_profile import LearningProfile


class TestLearningProfile(unittest.TestCase):
    def test_add_skill(self):
        profile = LearningProfile("Data Scientist", "low", 5, [])
        skill = Skill("Python", "beginner")

        profile.add_skill(skill)

        self.assertEqual(len(profile._current_skills), 1)

    def test_has_skill(self):
        skill = Skill("Python", "beginner")
        profile = LearningProfile("Data Scientist", "low", 5, [skill])

        self.assertTrue(profile.has_skill("Python"))


if __name__ == "__main__":
    unittest.main()