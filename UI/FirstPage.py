import tkinter as tk
import time

root = tk.Tk()

# labelFrame1 = LabelFrame
labelFrame1 = tk.LabelFrame(root, text="hello")
labelFrame1.grid(column=1, row=0, padx=20, pady=40 )

tk.Label(labelFrame1, text="label_1").grid(column=0, row=0, sticky=tk.W)
tk.Label(labelFrame1, text="label_2").grid(column=1, row=0, sticky=tk.W)
tk.Label(labelFrame1, text="label_3").grid(column=4, row=4, sticky=tk.W)

labelFrame2 = tk.LabelFrame(root, text="hello2")
labelFrame2.grid(column=1, row=1, padx=20, pady=40 )

w = tk.Label(labelFrame2, text="label_4", font="Courier 20").grid(column=0, row=0, pady=5, sticky=tk.W)

tk.Label(labelFrame2, text="label_5").grid(column=1, row=0, sticky=tk.W)
tk.Label(labelFrame2, text="label_6").grid(column=4, row=4, pady=5, sticky=tk.W)

time.sleep(2)

w['text'] = "New text"

root.state('zoomed')
root.resizable(False, False)
root.mainloop()
