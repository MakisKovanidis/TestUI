from tkinter import *
from UI.Sensor import Sensor


class SensorsSettingsWindow(Toplevel):
    def __init__(self, par2):
        self.topWindow = Toplevel()
        self.topWindow.wm_title("hello1")
        self.listFrame = LabelFrame(self.topWindow, text="Λιστα Αισθητηρων")
        self.sensorList = Listbox(self.listFrame, selectmode=EXTENDED, width=40)
        self.sensorList.pack()
        self.listFrame.grid(row=0, column=0, sticky=W + N + E + S)

        # Load the Name of Sensor in ListBox
        for Sensor in par2:
            self.sensorList.insert(Sensor.getID(), Sensor.getName())

        self.sensorList.grid(row=0, column=0)
        # Select the first element of the list
        self.sensorList.select_set(0)

        self.sensorList.bind('<<ListboxSelect>>', lambda event: self.get_element(event, 'another value'))

        self.frame = LabelFrame(self.topWindow, text="Λεπτομερειες Αισθητήρα")
        self.frame.grid(row=0, column=1, sticky=N, padx=10)
        # Name of the Sensor
        self.nameLabel = Label(self.frame, text="Σημείο Ψύξης")
        self.nameLabel.grid(row=0, column=0, sticky=W)

        stringNameEntry = StringVar()
        stringNameEntry.set(par2[0].name)
        self.nameEntry = Entry(self.frame, width=50, textvariable=stringNameEntry)
        self.nameEntry.grid(row=1, column=0, sticky=W)

        # Lower Limit of the sensor
        self.lowerLimit = Label(self.frame, text="Κατωτερη Θερμοκρασια")
        self.lowerLimit.grid(row=2, column=0, sticky=W)
        stringLowerLimitEntry = StringVar()
        stringLowerLimitEntry.set(par2[0].lowLimit)
        self.lowerLimitEntry = Entry(self.frame, width=50, textvariable=stringLowerLimitEntry)
        self.lowerLimitEntry.grid(row=3, column=0, sticky=W)

        # Upper Limit of th sensor
        self.upperLimit = Label(self.frame, text="Ανωτατη θερμοκρασια")
        self.upperLimit.grid(row=4, column=0, sticky=W)
        stringUpperEntry = StringVar()
        stringUpperEntry.set(par2[0].upperLimit)
        self.upperLimitEntry = Entry(self.frame, width=50, textvariable=stringUpperEntry)
        self.upperLimitEntry.grid(row=5, column=0, sticky=W)

        self.okButton = Button(self.frame, text="Aποθήκευση")
        self.okButton.grid(row=6, column=0, sticky=E, pady=10, padx=10)

    def get_element(self, event, arg):
        lb = event.widget
        idx = lb.curselection()
        # item = lb.get(idx)
        # print(str(idx))
        # value = self.sensorList.curselection()
        print(self.sensorList.get(idx))
