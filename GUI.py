#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
from library import *

#Create Main window
root = Tk()
#Name window Macro Pad
root.title("Macro Pad")
frm = ttk.Frame(root, padding=10)
#Initiate Grid
frm.grid()
button = ttk.Button

#row 1 buttons
button(frm, text="Chrome", command=chrome).grid(column=0, row=0)
button(frm, text="Discord", command=discord).grid(column=0, row=1)
button(frm, text="Lutris", command=lutris).grid(column=0, row=2)

#row 2 buttons
button(frm, text="OBS", command=OBS).grid(column=1, row=0)
button(frm, text="Spotify", command=spotify).grid(column=1, row=1)
button(frm, text="Steam", command=steam).grid(column=1, row=2)

#quit/shutdown
button(frm, text="quit", command=quit).grid(column=2, row=4)
button(frm, text="shutdown", command=shutdown).grid(column=3, row=5)

root.mainloop()