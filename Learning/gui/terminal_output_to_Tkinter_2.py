import tkinter as tk
import sys
import subprocess
import threading 

# --- classes ---

class Redirect():

    def __init__(self, widget, autoscroll=True):
        self.widget = widget
        self.autoscroll = autoscroll

    def write(self, text):
        self.widget.insert('end', text)
        if self.autoscroll:
            self.widget.see("end")  # autoscroll
        
    #def flush(self):
    #    pass

# --- functions ---

def run():
    threading.Thread(target=test).start()

def test():
    print("Thread: start")

    p = subprocess.Popen("ping stackoverflow.com".split(), stdout=subprocess.PIPE, bufsize=1, text=True)
    while p.poll() is None:
        msg = p.stdout.readline().strip() # read a line from the process output
        if msg:
            print(msg)

    print("Thread: end")

# --- main ---    

mainWin = tk.Tk()

# - Frame with Text and Scrollbar -

frame = tk.Frame(mainWin)
frame.pack(expand=True, fill='both')

text = tk.Text(frame)
text.pack(side='left', fill='both', expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

text['yscrollcommand'] = scrollbar.set
scrollbar['command'] = text.yview

old_stdout = sys.stdout    
sys.stdout = Redirect(text)

# - rest -

button = tk.Button(mainWin, text='TEST', command=run)
button.pack()

mainWin.mainloop()

# - after close window -

sys.stdout = old_stdout