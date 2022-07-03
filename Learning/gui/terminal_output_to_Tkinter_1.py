import sys
 
from tkinter import *
 
def TimesTable():
    print("\n")
    result = "Result"
    for x in range(1,13):
        m = int(EnterTable.get())
        print('\t\t', (x), ' x ',(m), ' = ', (x * m),)
        result = result + '\t\t' + str(x) + ' x ' + str(m)+  ' = ' + str(x * m) + "\n"
    result=Label(Multiply, text=result, justify='left').grid(row=9, column=6)
 
 
Multiply = Tk()
Multiply.geometry('250x500+700+200')
Multiply.title('Multiplication Table')
 
EnterTable = StringVar()
 
label1=Label(Multiply, text='Multiplication Times Table', font=30, fg='Black').grid(row=1, column=6)
label1=Label(Multiply,text='                                         ').grid(row=2,column=6)
entry5=Entry(Multiply, textvariable=EnterTable, justify='center').grid(row=3, column=6)
label1=Label(Multiply,text='                                         ').grid(row=4,column=6)            
 
button1=Button(Multiply, text='Times Table', command=TimesTable).grid(row=5,column=6)
label1=Label(Multiply,text='                                         ').grid(row=6,column=6)        
QUIT=Button(Multiply,text='Quit', fg='Red', command=Multiply.destroy).grid(row=7,column=6)
label1=Label(Multiply,text='                                         ').grid(row=8,column=6)        
result=Label(Multiply, text="Show result by insert a value", justify='left').grid(row=9, column=6)
label1=Label(Multiply,text='                                         ').grid(row=10,column=6)        
 
 
Multiply.mainloop()