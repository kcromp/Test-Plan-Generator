def getPath():
    global path 
    path = entry.get()
    print (path)

import tkinter as tk 
window = tk.Tk()
label = tk.Label(text="Test Plan Path")
entry = tk.Entry()
btn_click = tk.Button(master=window, text="Submit", command=getPath)
label.pack()
entry.pack()
btn_click.pack()
window.mainloop()