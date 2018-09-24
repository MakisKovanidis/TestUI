import random
import time


def read_temp_raw(filePath):
    f = open(filePath, 'r')
    lines = f.readlines()
    f.close()
    return lines


class Sensor:
    def __init__(self, id, name, value, upperLimit, lowLimit, filePath="SS"):
        self.id = id
        self.name = name
        self.value = value
        self.upperLimit = upperLimit
        self.lowLimit = lowLimit
        self.filePath = filePath

    # def setLimits(self, newUpperLimit, newLowLimit):
    #     self.upperLimit = newUpperLimit
    #     self.lowLimit = newLowLimit

    def update(self):
        randValue = random.randrange(-25, 20)
        self.value = randValue
        # print(randValue)
        return self.value

    def read_temp(self):
        lines = read_temp_raw(self.filePath)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2:]
            self.value = float(temp_string) / 1000.0
        return "{:.2f}".format(self.value)

    def getName(self):
        return self.name