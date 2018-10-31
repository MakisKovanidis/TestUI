import os
import pickle
from tkinter import messagebox

from Models.Sensor import Sensor
from Settings import globalSettings

# Open a file
path = globalSettings.laptopBaseDir
pathData = globalSettings.laptopDataDir
dirs = os.listdir(path)
counter = 1

class MainController:

    def __init__(self):
        self.sensorList = []
        # Read the number of files which represent the number odf sensor
        self.readAllSensors()



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