
class Plant:
    def __init__(self,color):
        self.__color = color


    def get_color(self):
        return self.__color

# put the super class in parentheses
class Flower(Plant):
    # put petals for the subclass to go further in depth
    def __init__(self,color, petals):
        Plant.__init__(self,color)

        self.__petals = petals

    def get_petals(self):
        return self.__petals
