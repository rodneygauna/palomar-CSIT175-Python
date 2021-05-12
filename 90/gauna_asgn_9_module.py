"""
This module is for Assignement 9.
There is a primary class of Car and two child class of the Car as Model_1 and Model_2
"""

class Car():
    """Represents the car"""
    
    def __init__(self):
        self.horn = "beep beep"
        self.distance = "2"
        self.color = ""
        self.line = "-"

    def soundHorn(self):
        """Prints the value of the horn style"""
        print(self.horn)

    
    def getColor(self):
        """Returns the color of the car"""
        return self.color
    
    def showLine(self, number):
        """Receives the distance value"""
        self.distance = int(self.distance) + number
        self.line = self.distance * "-"

class Model_1(Car):
    """Represents aspects of the car, specific for Model_1"""

    def __init__(self):
        super().__init__()
        self.color = "blue"

class Model_2(Car):
    """Represents aspects of the car, specific for Model_2"""

    def __init__(self):
        super().__init__()
        self.horn = "honk honk"
        self.color = "red"