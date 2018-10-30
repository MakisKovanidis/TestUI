from tkinter import *
from tkinter import messagebox


class SingleSensorSettings(Toplevel):
    def __init__(self, sensorArg):
        self.topWindow = Toplevel()
        # Prevent to minimize the top level window
        self.topWindow.attributes('-topmost', 1)

        # Prevent to do actions from lower level windows and don't allow to open other top level window
        self.topWindow.focus_set()
        self.topWindow.grab_set()

        self.topWindow.wm_title("Ρυθμισεις Αισθητήρα")
        self.listFrame = LabelFrame(self.topWindow, text="Λιστα Αισθητηρων")
        self.listFrame.grid(row=0, column=0, sticky=W + N + E + S)

        self.frame = LabelFrame(self.topWindow, text="Λεπτομερειες Αισθητήρα")
        self.frame.grid(row=0, column=1, sticky=N, padx=10)
        # Name of the Sensor
        self.nameLabel = Label(self.frame, text="Σημείο Ψύξης")
        self.nameLabel.grid(row=0, column=0, sticky=W)

        stringNameEntry = StringVar()
        stringNameEntry.set(sensorArg.name)
        self.nameEntry = Entry(self.frame, width=50, textvariable=stringNameEntry)
        self.nameEntry.grid(row=1, column=0, sticky=W)

        # Lower Limit of the sensor
        self.lowerLimit = Label(self.frame, text="Κατωτερη Θερμοκρασια")
        self.lowerLimit.grid(row=2, column=0, sticky=W)
        stringLowerLimitEntry = StringVar()
        stringLowerLimitEntry.set(sensorArg.lowLimit)
        self.lowerLimitEntry = Entry(self.frame, width=50, textvariable=stringLowerLimitEntry)
        self.lowerLimitEntry.grid(row=3, column=0, sticky=W)

        # Upper Limit of th sensor
        self.upperLimit = Label(self.frame, text="Ανωτατη θερμοκρασια")
        self.upperLimit.grid(row=4, column=0, sticky=W)
        stringUpperEntry = StringVar()
        stringUpperEntry.set(sensorArg.upperLimit)
        self.upperLimitEntry = Entry(self.frame, width=50, textvariable=stringUpperEntry)
        self.upperLimitEntry.grid(row=5, column=0, sticky=W)

        # Save button
        self.saveButton = Button(self.frame, text="Aποθήκευση", width=10, command=lambda: self.saveChanges(sensorArg))
        self.saveButton.grid(row=6, column=0, pady=10, padx=10)

        # Exit button
        self.exitButton = Button(self.frame, text="Εξοδος", width=10, command=lambda: self.exitWithoutSaving(sensorArg))
        self.exitButton.grid(row=6, column=0, sticky=E, pady=10, padx=10)

    def saveChanges(self, sensorArg):
        try:
            sensorArg.save(self.nameEntry.get(), int(self.lowerLimitEntry.get()), int(self.upperLimitEntry.get()))
            self.topWindow.destroy()
        except ValueError:
            messagebox.showerror("error","invslid limits")


    def exitWithoutSaving(self, sensorArg):
        try:
            if (self.nameEntry.get() == sensorArg.name) and (
                    int(self.lowerLimitEntry.get()) == sensorArg.lowLimit) and (
                    int(self.upperLimitEntry.get()) == sensorArg.upperLimit):
                self.topWindow.destroy()
            else:
                result = messagebox.askokcancel("Close", "Exit without saving")
                if (result):
                    self.topWindow.destroy()
        except ValueError:
            result = messagebox.askokcancel("Close", "Exit without saving")
            if (result):
                self.topWindow.destroy()


