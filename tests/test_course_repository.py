import unittest
from repository.course_repository import CourseRepository


class TestCourseRepository(unittest.TestCase):
    def test_load_courses_returns_non_empty_list(self):
        repo = CourseRepository("data/items.json")
        courses = repo.load_courses()

        self.assertGreater(len(courses), 0)


if __name__ == "__main__":
    unittest.main()