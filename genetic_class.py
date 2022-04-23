class Individual:
    __genom = None
    __evaluation = None
    __volume = None

    def __init__(self, genom, evaluation, volume):
        self.__genom = genom
        self.__evaluation = evaluation
        self.__volume = volume

    def get_genom(self):
        return self.__genom

    def get_evaluation(self):
        return self.__evaluation

    def get_volume(self):
        return self.__volume

    def set_genom(self, genom):
        self.__genom = genom

    def set_evaluation(self, evaluation):
        self.__evaluation = evaluation

    def set_volume(self, volume):
        self.__volume = volume
