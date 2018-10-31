import os
from tkinter import *
from tkinter import messagebox

from Settings import globalSettings
from UI.MyLabelFrame import MyLabelFrame
from Models.Sensor import Sensor
from UI.SensorSettingsWindow import SensorsSettingsWindow
import _pickle as pickle

# Open a file
path = globalSettings.laptopBaseDir
pathData = globalSettings.laptopDataDir
dirs = os.listdir(path)
counter = 1


class MainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.sensorListImportedFromFile = []
        self.sensorList = []
        self.labelFrameList = []

        menu = Menu(self)
        self.config(menu=menu)
        subMenu = Menu(menu)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="Settings",
                            command=lambda: self.create_window())
        subMenu.add_command(label="Exit",
                            command=lambda: self.saveSensorList())

        # Read the number of files which represent the number odf sensor
        self.readAllSensors()

        # Create dynamically the label frames for each sensor
        self.createTheLabelFrames()

    # Read the number of files which represent the number odf sensor
    def readTheInstalledSensors(self):
        tempListInstalledSensors = []
        for file in dirs:
            global counter
            sensorName = "Sensor" + str(counter)
            deviceFile = path + file
            tempListInstalledSensors.append(Sensor(counter, sensorName, 20.0, -10, 30, deviceFile))
            counter = counter + 1
            print(deviceFile)

        return tempListInstalledSensors

    def createTheLabelFrames(self, choosedList=0):
        for i in range(len(self.sensorList)):
            labelText = StringVar()
            labelText.set(self.sensorList[i].getName())
            self.labelFrameList.append(MyLabelFrame(self.sensorList[i], self, labelText.get()))

    # Read the sensor periodically after 10 secs
    def read_sensor(self):
        self.after(10000, self.read_sensor)
        self.labelFrameList
        self.sensorList

        for j in range(len(self.sensorList)):
            vall = self.sensorList[j].read_temp()
            self.labelFrameList[j].updateLabelTextValue(vall)
            print(vall)

    def create_window(self):
        SensorsSettingsWindow(self.sensorList)

    def saveSensorList(self):
        with open("bin.dat", "wb") as f:
            pickle.dump(self.sensorList, f)

        exit()

    def load_data(self):
        tempSensorList = []
        try:
            with open(pathData + 'bin.dat', "rb") as f:
                tempSensorList = pickle.load(f)
        except:
            messagebox.showerror("Error", "problem with reading file")

        return tempSensorList

    def readAllSensors(self):
        # Read the file if exists previous data
        exists = os.path.isfile(pathData + 'bin.dat')
        print(str(exists))
        if (exists):
            self.sensorList = self.load_data()

        # Append new Sensors if installed last time
        newinstalledSensors = self.readTheInstalledSensors()
        for i in range(len(newinstalledSensors)):
            tempSensor = newinstalledSensors[i]
            # print(str(tempSensor.id)+ "#####"+tempSensor.name)
            if (self.findIfTheSensorExist(tempSensor) == False):
                self.sensorList.append(tempSensor)

        self.sensorList.sort(key=lambda x: str(x.id))

    def findIfTheSensorExist(self, sensorArg):
        find = False
        for Sensor in self.sensorList:
            if (Sensor.id == sensorArg.id):
                find = True
                break

        return find



root = MainWindow()
root.state('zoomed')
root.after(1000, root.read_sensor)
root.mainloop()
