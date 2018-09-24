from tkinter import *

class MyGUI:
    def __init__(self):
        self.__mainWindow = Tk()
        self.labelFrame1 = LabelFrame(self.__mainWindow, text="Sensor1")
        self.sensorValue1 = Label(self.labelFrame1, text="20.0", font="Courier 20 bold")
        # self.depositEntry = Entry(self.labelFrame1, width=10)
        # self.depositEntry.bind('<Return>', self.depositCallBack)
        self.labelFrame1.pack()
        self.sensorValue1.pack()
        self.sensorValue1.bind('<Return>', self.update)
        # self.depositEntry.pack()
        self.__mainWindow.state('zoomed')
        mainloop()

    def update(self, passValue):
        self.sensorValue1.config(text=passValue)
       # print(self.labelText)





# root = Tk()
#
# # labelFrame1 = LabelFrame
# labelFrame1 = LabelFrame(root, text="hello")
# labelFrame1.grid(column=1, row=0, padx=20, pady=40 )
#
# label_1 = Label(labelFrame1, text="label_1").grid(column=0, row=0, sticky=W)
# label_2 = Label(labelFrame1, text="label_2").grid(column=1, row=0, sticky=W)
# label_3 = Label(labelFrame1, text="label_3").grid(column=4, row=4, sticky=W)
#
# labelFrame2 = LabelFrame(root, text="hello2")
# labelFrame2.grid(column=1, row=1, padx=20, pady=40 )
# label_4 = Label(labelFrame2, text="label_4", font="Courier 20").grid(column=0, row=0, pady=5, sticky=W)
#
# label_5 = Label(labelFrame2, text="label_5")
# label_6 = Label(labelFrame2, text="label_6").grid(column=4, row=4, pady=5, sticky=W)
#
# label_5.grid(column=1, row=0, sticky=W)
# root.state('zoomed')
# root.resizable(False, False)
# root.mainloop()
