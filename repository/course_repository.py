import json
from models.course import Course


class CourseRepository:
    def __init__(self, file_name):
        self._file_name = file_name

    def load_courses(self):
        with open(self._file_name, "r") as file:
            data = json.load(file)

        courses_list = []

        for item in data:
            course = Course(
                item["title"],
                item["difficulty"],
                item["duration_hours"],
                item["price"],
                item["skill_name"]
            )
            courses_list.append(course)

        return courses_list