from tkinter import *
from random import randint

root=Tk()
root.title('NUMBER GUESSING ')
root.geometry("500x550")


num_label=Label(root,text="Guess the number \nfrom 1 to 10!",font=("Brush Script MT",32))
num_label.pack(pady=20)

def guesser():
    if guess_box.get().isdigit():
        #Reset our label
        num_label.config(text="Guess the number \nfrom 1 to 10!")
        #find out how far away our pick was from our actual number
        dif =abs(num-int(guess_box.get()))
        #check to see if correct
        if int(guess_box.get())==num:
            bc="SystemButtonFace"
            num_label.config(text="Correct!!")
        elif dif==5:
            #set background colout to white
            bc="white"
        elif dif<5:
            bc=f'#ff{dif}{dif}{dif}{dif}'
        else:
            bc=f'#{dif}{dif}{dif}{dif}ff'
        #change the background of an app
        root.config(bg=bc)
        #change bg of label
        num_label.config(bg=bc)

    else:
        #Delete entry and tnrow error message
        guess_box.delete(0,END)
        num_label.config(text="Hey! That's Not A Number")

def rando():
    global num
    num=randint(1,10)
    #clear the guess_box
    guess_box.delete(0,END)
    #change the colors back to normal
    num_label.config(bg="SystemButtonFace",text="Guess the number \nfrom 1 to 10!")
    root.config(bg="SystemButtonFace")
    


guess_box=Entry(root,font=("Helvetica",50),width=2)
guess_box.pack(pady=20)

guess_button=Button(root,text="SUBMIT",command=guesser)
guess_button.pack(pady=20)

rand_button=Button(root,text="New Number",command=rando)
rand_button.pack(pady=20)

#generate a random number on start 
rando()

root.mainloop()

