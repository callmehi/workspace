import tkinter as tk

def button_event():
    print(myentry.get())
    if myentry.get() != '':
        mybutton['text'] = myentry.get()

root = tk.Tk()
root.title('my window')
root.geometry('200x150')

myentry = tk.Entry(root)
myentry.pack()

mybutton = tk.Button(root, text='button', command=button_event)
mybutton.pack()

root.mainloop()