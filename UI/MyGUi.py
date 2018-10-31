import os
from tkinter import *

from Controller.MainContoller import MainController
from Settings import globalSettings
from UI.MyLabelFrame import MyLabelFrame
from Models.Sensor import Sensor
from UI.SensorSettingsWindow import SensorsSettingsWindow


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.labelFrameList = []

        menu = Menu(self)
        self.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Settings",
                            command=lambda: self.create_window())
        subMenu.add_command(label="Exit",
                            command=lambda: self.appController.saveSensorList())

        self.appController = MainController()

        # Create dynamically the label frames for each sensor
        self.createTheLabelFrames(self.appController.getSensorList())



    def createTheLabelFrames(self, choosedList):
        for i in range(len(choosedList)):
            labelText = StringVar()
            labelText.set(choosedList[i].getName())
            self.labelFrameList.append(MyLabelFrame(choosedList[i], self, labelText.get()))

    # Read the sensor periodically after 10 secs
    def read_sensor(self):
        self.after(10000, self.read_sensor)
        tempCounter=0
        for Sensor in self.appController.getSensorList():
            vall = Sensor.read_temp()
            self.labelFrameList[tempCounter].updateLabelTextValue(vall)
            print(vall)
            tempCounter=tempCounter+1

    def create_window(self):
        SensorsSettingsWindow(self.sensorList)


root = MainWindow()
root.state('zoomed')
root.after(1000, root.read_sensor)
root.mainloop()
