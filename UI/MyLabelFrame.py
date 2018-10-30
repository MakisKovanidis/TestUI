from tkinter import *

from UI.SingleSensorSettings import SingleSensorSettings


class MyLabelFrame:
    def __init__(self, sensorArg, master=None, label='MyFrame'):
        self.frame = LabelFrame(master, text=label)
        self.frame.grid(sticky=E)
        self.value = StringVar()
        self.value.set("20.0")
        self.label = Label(self.frame, textvariable=self.value, font=("Courier 20 bold")).pack()
        self.detailsButton = Button(self.frame, text="Ρυθμισεις", width=10, command=lambda: self.openSettingsWindow(sensorArg))
        self.detailsButton.pack()

    def updateLabelTextValue(self, textValue):
        self.value.set(textValue)

    def openSettingsWindow(self, sensorArg):
        SingleSensorSettings(sensorArg)
