import unittest
from models.skill import Skill
from models.learning_profile import LearningProfile


class TestLearningProfile(unittest.TestCase):
    def test_add_skill_adds_new_skill(self):
        profile = LearningProfile("Data Scientist", "low", 5, [])
        skill = Skill("Python", "beginner")

        profile.add_skill(skill)

        self.assertEqual(len(profile._current_skills), 1)

    def test_has_skill_returns_true_when_skill_exists(self):
        skill = Skill("Python", "beginner")
        profile = LearningProfile("Data Scientist", "low", 5, [skill])

        result = profile.has_skill("Python")

        self.assertTrue(result)

    def test_has_skill_returns_false_when_skill_does_not_exist(self):
        skill = Skill("Python", "beginner")
        profile = LearningProfile("Data Scientist", "low", 5, [skill])

        result = profile.has_skill("Java")

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()