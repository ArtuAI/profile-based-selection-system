class CourseRecommendation:
    def __init__(self, course, score, reason):
        self._course = course
        self._score = score
        self._reason = reason

    def display_info(self):
        print("Course", self._course)
        print("Score", self._score)
        print("Reason", self._reason)
        