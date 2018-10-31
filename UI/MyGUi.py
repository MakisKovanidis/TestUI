import os
from tkinter import *
from tkinter import messagebox

from Controller.MainContoller import MainController
from Settings import globalSettings
from UI.MyLabelFrame import MyLabelFrame
from Models.Sensor import Sensor
from UI.SensorSettingsWindow import SensorsSettingsWindow
import _pickle as pickle




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
                            command=lambda: self.saveSensorList())

        self.appController=MainController()

        # Create dynamically the label frames for each sensor
        self.createTheLabelFrames(MainController.sensorList)



    def createTheLabelFrames(self, choosedList):
        for i in range(len(choosedList)):
            labelText = StringVar()
            labelText.set(self.sensorList[i].getName())
            self.labelFrameList.append(MyLabelFrame(self.sensorList[i], self, labelText.get()))

    # Read the sensor periodically after 10 secs
    def read_sensor(self):
        self.after(10000, self.read_sensor)
        # self.labelFrameList
        # self.sensorList

        for j in range(len(self.sensorList)):
            vall = self.sensorList[j].read_temp()
            self.labelFrameList[j].updateLabelTextValue(vall)
            print(vall)

    def create_window(self):
        SensorsSettingsWindow(self.sensorList)


root = MainWindow()
root.state('zoomed')
root.after(1000, root.read_sensor)
root.mainloop()
