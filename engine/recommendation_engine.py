class RecommendationEngine:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def generate(self, profile, courses):
        return self._strategy.generate_recommendations(profile, courses)