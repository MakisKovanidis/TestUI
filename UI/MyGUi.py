import os
from tkinter import *

from UI.MyLabelFrame import MyLabelFrame
from UI.Sensor import Sensor

sensorList = []
labelFrameList = []
mainWindow = Tk()

# Open a file
path = "c:/test/"
dirs = os.listdir(path)
counter = 1
# This would print all the files and directories

for file in dirs:
    sensorName = "Sensor" + str(counter)
    deviceFile = path + file
    sensorList.append(Sensor(counter, sensorName, 20.0, -10, 30, deviceFile))
    counter = counter + 1
    print(deviceFile)

for i in range(len(sensorList)):
    labelText = StringVar()
    labelText.set(sensorList[i].getName())
    labelFrameList.append(MyLabelFrame(mainWindow, labelText.get()))


def read_sensor():
    mainWindow.after(10000, read_sensor)
    global labelFrameList
    global sensorList

    for j in range(len(sensorList)):
        vall = sensorList[j].read_temp()
        labelFrameList[j].updateLabelTextValue(vall)
        print(vall)


mainWindow.after(1000, read_sensor)
mainWindow.mainloop()
