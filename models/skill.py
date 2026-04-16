class Skill:
    def __init__(self, name, level):
        self._name = name
        self._level = level

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def display_info(self):
        print("Skill name:", self._name)
        print("Skill level:", self._level)