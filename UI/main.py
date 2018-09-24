from UI.MyGUI import MyGUI
from UI.Sensor import Sensor

myGui = MyGUI()

sensor1 = Sensor(1, "sensorName", 45.0, -10, 55)

while True:
    val = sensor1.update()
    myGui.update(val)

