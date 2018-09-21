import tkinter as tk

root = tk.Tk()

# topFrame = tk.Frame(root)
# topFrame.pack()
#
# bottomFrame = tk.Frame(root)
# bottomFrame.pack(side=tk.BOTTOM)
#
# button1 = tk.Button(topFrame, text="Button 1", fg="red")
# button2 = tk.Button(topFrame, text="Button 2", fg="blue")
# button3 = tk.Button(topFrame, text="Button 3", fg="green")
# button4 = tk.Button(bottomFrame, text="Button 4", fg="red")
#
# button1.pack()
# button2.pack()
# button3.pack()
# button4.pack()

# labelFrame1 = LabelFrame
labelFrame1 = tk.LabelFrame(root, text="hello")
labelFrame1.grid(column=1, row=0, padx=20, pady=40 )

tk.Label(labelFrame1, text="label_1").grid(column=0, row=0, sticky=tk.W)
tk.Label(labelFrame1, text="label_2").grid(column=1, row=0, sticky=tk.W)
tk.Label(labelFrame1, text="label_3").grid(column=4, row=4, sticky=tk.W)

labelFrame2 = tk.LabelFrame(root, text="hello2")
labelFrame2.grid(column=1, row=1, padx=20, pady=40 )

tk.Label(labelFrame2, text="label_4").grid(column=0, row=0, sticky=tk.W)
tk.Label(labelFrame2, text="label_5").grid(column=1, row=0, sticky=tk.W)
tk.Label(labelFrame2, text="label_6").grid(column=4, row=4, sticky=tk.W)



root.state('zoomed')
root.resizable(False, False)
root.mainloop()
