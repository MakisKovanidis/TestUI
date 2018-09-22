from tkinter import *

from UI.MyLabelFrame import MyLabelFrame
from UI.Sensor import Sensor

sensorList = []
labelFrameList = []
mainWindow = Tk()

sensorList.append(Sensor(1, "Sensor1", 20.0, -10, 30))
sensorList.append(Sensor(2, "Sensor2", 30.0, -10, 30))
sensorList.append(Sensor(3, "Sensor3", 20.0, -10, 30))

for i in range(len(sensorList)):
    labelText = StringVar()
    labelText.set("Sensor"+str(i))
    labelFrameList.append(MyLabelFrame(mainWindow, labelText.get()))





# def readSensor():
#     mainWindow.after(1000, readSensor)
#     global temperature1
#     global temperature2
#     global temperature3
#
#     temperature1.set(sensorList[0].update())
#     temperature2.set(sensorList[1].update())
#     temperature3.set(sensorList[2].update())
#
#
# mainWindow.after(1000, readSensor)
mainWindow.mainloop()
