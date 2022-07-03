#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk

def checkbutton_event():
    print('checkbutton_event: ' + str(var1.get()) + ' '
          + str(var2.get()) + ' ' + str(var3.get()))

root = tk.Tk()
root.title('my window')
root.geometry('200x150')

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

mycheckbutton1 = tk.Checkbutton(root, text='apple',
                                variable=var1,
                                onvalue=1, offvalue=0,
                                command=checkbutton_event)
mycheckbutton1.pack()
mycheckbutton2 = tk.Checkbutton(root, text='banana',
                                variable=var2,
                                onvalue=1, offvalue=0,
                                command=checkbutton_event)
mycheckbutton2.pack()
mycheckbutton3 = tk.Checkbutton(root, text='orange',
                                variable=var3,
                                onvalue=1, offvalue=0,
                                command=checkbutton_event)
mycheckbutton3.pack()

var1.set(1)

root.mainloop()