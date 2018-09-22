import random

class Sensor:
    def __init__(self, id, name, value, upperLimit, lowLimit):
        self.id = id
        self.name = name
        self.value = value
        self.upperLimit = upperLimit
        self.lowLimit = lowLimit

    # def setLimits(self, newUpperLimit, newLowLimit):
    #     self.upperLimit = newUpperLimit
    #     self.lowLimit = newLowLimit

    def update(self):
        randValue = random.randrange(-25, 20)
        self.value = randValue
        print(randValue)
        return self.value
