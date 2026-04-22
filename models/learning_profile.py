class LearningProfile:
    def __init__(self, target_role, budget_level, weekly_hours, current_skills):
        self._target_role = target_role
        self._budget_level = budget_level
        self._weekly_hours = weekly_hours
        self._current_skills = current_skills

    def display_info(self):
        print("Target role:", self._target_role)
        print("Budget level:", self._budget_level)
        print("Weekly hours:", self._weekly_hours)
        print("Current skills:")

        for skill in self._current_skills:
            skill.display_info()

    def add_skill(self, skill):
        self._current_skills.append(skill)
        
    
    def has_skill(self, skill_name):
        for skill in self._current_skills:
            if skill._name == skill_name:
                return True
        return False
            