class Course:
    def __init__(self, title, difficulty, duration_hours, price, skill_name):
        self._title = title
        self._difficulty = difficulty
        self._duration_hours = duration_hours
        self._price = price
        self._skill_name = skill_name
    
    def display_info(self):
        print("Title:", self._title)
        print("Difficulty:", self._difficulty)
        print("Duration:", self._duration_hours, "hours")
        print("Price:", self._price, "$")
        print("Skill to acquire:", self._skill_name)

    def matches_skill(self, skill_name):
        if self._skill_name == skill_name:
            return True
        else:
            return False
    