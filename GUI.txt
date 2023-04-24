import sys
import os
from tkinter import *
window=Tk()
window.title('Mini Game Simulator')
window.geometry("300x200+10+10")
def fun():
    os.system('prgrm1.py')
def fun2():
    os.system('prgrm2.py')
def fun3():
    os.system('prgrm3.py')
btn1=Button(window,activebackground="black",activeforeground="white",text="Game 1", fg='blue',command=fun)
btn1.pack(fill=BOTH, expand=1)
btn2=Button(window,activebackground="black",activeforeground="yellow", text="Game 2", fg='black',command=fun2)
btn2.pack(fill=BOTH, expand=1)
btn3=Button(window,activebackground="black",activeforeground="#58CD36", text="Game 3", fg='green',command=fun3)
btn3.pack(fill=BOTH, expand=1)
window.mainloop()
