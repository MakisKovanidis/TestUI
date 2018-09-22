from tkinter import *

class MyLabelFrame:
    def __init__(self, master=None, label='MyFrame'):
        self.frame = LabelFrame(master, text=label)
        #self.frame.grid(row=row,column=col, sticky=(N,S,E,W))
        self.frame.pack()
        self.value = StringVar()
        self.value.set("20.0")
        self.label = Label(self.frame, textvariable=self.value).pack()

        #self.value.set("Yes")

