import unittest
from repository.course_repository import CourseRepository
from models.course import Course


class TestCourseRepository(unittest.TestCase):
    def test_load_courses_returns_non_empty_list(self):
        repo = CourseRepository("data/items.json")
        courses = repo.load_courses()

        self.assertGreater(len(courses), 0)

    def test_load_courses_returns_course_objects(self):
        repo = CourseRepository("data/items.json")
        courses = repo.load_courses()

        first_course = courses[0]

        self.assertIsInstance(first_course, Course)


if __name__ == "__main__":
    unittest.main()