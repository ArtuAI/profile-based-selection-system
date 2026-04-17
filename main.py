from repository.course_repository import CourseRepository

repo = CourseRepository("data/items.json")
courses = repo.load_courses()

for course in courses:
    course.display_info()
    print()