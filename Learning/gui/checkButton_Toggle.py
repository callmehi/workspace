#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
root = tk.Tk()
root.title('my window')
root.geometry('200x150')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

mycheckbutton1 = tk.Checkbutton(root, text='apple',
                                variable=var1,
                                onvalue=1, offvalue=0)
mycheckbutton1.pack()
mycheckbutton2 = tk.Checkbutton(root, text='banana',
                                variable=var2,
                                onvalue=1, offvalue=0)
mycheckbutton2.pack()
mycheckbutton3 = tk.Checkbutton(root, text='orange',
                                variable=var3,
                                onvalue=1, offvalue=0)
mycheckbutton3.pack()

mycheckbutton1.select()
mycheckbutton1.deselect()
mycheckbutton2.select()
mycheckbutton3.toggle()

root.mainloop()