from tkinter import *

root = Tk()

# # basic layout pack()
# Label(root, text="Red Sun",bg="red",fg="white").pack()
# Label(root, text="Green Grass",bg="green",fg="black").pack()
# Label(root, text="Blue Sky",bg="blue",fg="white").pack()

# layout pack(fill=X)
# w = Label(root, text="Red Sun",bg="red",fg="white")
# w.pack(fill=X)
# w = Label(root, text="Green Grass",bg="green",fg="black")
# w.pack(fill=X)
# w = Label(root, text="Blue Sky",bg="blue",fg="white")
# w.pack(fill=X)

# # layout pack(fill=X,padx=10)
# w = Label(root, text="Red Sun",bg="red",fg="white")
# w.pack(fill=X,padx=10)
# w = Label(root, text="Green Grass",bg="green",fg="black")
# w.pack(fill=X,padx=10)
# w = Label(root, text="Blue Sky",bg="blue",fg="white")
# w.pack(fill=X,padx=10)

# layout pack(fill=X,pady=10)
# w = Label(root, text="Red Sun",bg="red",fg="white")
# w.pack(fill=X,pady=10)
# w = Label(root, text="Green Grass",bg="green",fg="black")
# w.pack(fill=X,pady=10)
# w = Label(root, text="Blue Sky",bg="blue",fg="white")
# w.pack(fill=X,pady=10)

# layout pack(padx=5,pady=10, side=LEFT)
# w = Label(root, text="Red Sun",bg="red",fg="white")
# w.pack(padx=5,pady=10, side=LEFT)
# w = Label(root, text="Green Grass",bg="green",fg="black")
# w.pack(padx=5,pady=20, side=LEFT)
# w = Label(root, text="Blue Sky",bg="blue",fg="white")
# w.pack(padx=5,pady=20, side=LEFT)

# layout pack(padx=5,pady=10, side=RIGHT)
w = Label(root, text="Red Sun",bg="red",fg="white")
w.pack(padx=5,pady=10, side=RIGHT)
w = Label(root, text="Green Grass",bg="green",fg="black")
w.pack(padx=5,pady=20, side=RIGHT)
w = Label(root, text="Blue Sky",bg="blue",fg="white")
w.pack(padx=5,pady=20, side=RIGHT)

mainloop()



