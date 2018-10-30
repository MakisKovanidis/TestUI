import os
from tkinter import *
from Settings import globalSettings
from UI.MyLabelFrame import MyLabelFrame
from Models.Sensor import Sensor
from UI.SensorSettingsWindow import SensorsSettingsWindow

sensorList = []
labelFrameList = []

# Open a file
path = globalSettings.baseDir
dirs = os.listdir(path)
counter = 1

class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        menu = Menu(self)
        self.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Settings",
                            command=lambda: self.create_window())
        subMenu.add_command(label="Exit",
                             command=lambda: self.create_window2())

        # Read the number of files which represent the number odf sensor
        for file in dirs:
            global counter
            sensorName = "Sensor" + str(counter)
            deviceFile = path + file
            sensorList.append(Sensor(counter, sensorName, 20.0, -10, 30, deviceFile))
            counter = counter + 1
            print(deviceFile)

        # Create dynamically the label frames for each sensor
        for i in range(len(sensorList)):
            labelText = StringVar()
            labelText.set(sensorList[i].getName())
            labelFrameList.append(MyLabelFrame(sensorList[i], self, labelText.get()))


    # Read the sensor periodically after 10 secs
    def read_sensor(self):
        self.after(10000, self.read_sensor)
        global labelFrameList
        global sensorList

        for j in range(len(sensorList)):
            vall = sensorList[j].read_temp()
            labelFrameList[j].updateLabelTextValue(vall)
            print(vall)

    def create_window(self):
        global sensorList
        SensorsSettingsWindow(sensorList)

    def saveSensorList(self):
        global sensorList
        #edfdfsdfasdfsdfsdfdsdfkvp[sda[fpsdfas



root = MainWindow()
root.state('zoomed')
root.after(1000, root.read_sensor)
root.mainloop()
