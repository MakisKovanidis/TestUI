from tkinter import *


class MyLabelFrame:
    def __init__(self, master=None, label='MyFrame'):
        self.frame = LabelFrame(master, text=label)
        self.frame.pack()
        self.value = StringVar()
        self.value.set("20.0")
        self.label = Label(self.frame, textvariable=self.value,font=("Courier 20 bold")).pack()

    def updateLabelTextValue(self, textValue):
        self.value.set(textValue)
