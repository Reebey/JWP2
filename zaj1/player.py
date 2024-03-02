class Player:

    def __init__(self, mark):
        self.mark = mark

    def __str__(self):
        return f"{self.mark}"
    
    def __eq__(self, p):
        if type(p) is type(self):
            return self.__str__() == p.__str__()
        if type(p) is str:
            return self.__str__() == p
        return False

    def __add__(self, p):
        return self.__str__() + p

    def __hash__(self):
        return hash(self.__members())