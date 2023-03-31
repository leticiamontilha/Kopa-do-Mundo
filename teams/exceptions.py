class NegativeTitlesError(Exception):
    def __init__(self, message: dict):
        self.message = message


class InvalidYearCupError(Exception):
    def __init__(self, message: dict):
        self.message = message


class ImpossibleTitlesError(Exception):
    def __init__(self, message: dict):
        self.message = message
