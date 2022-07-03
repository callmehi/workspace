#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter as tk
 
root = tk.Tk()
root.title('my window')
root.geometry('200x150')

var = tk.StringVar()
var.set('apple')
myoptionmenu = tk.OptionMenu(root, var, 'apple','banana','orange')
myoptionmenu.pack(pady=10)

root.mainloop()