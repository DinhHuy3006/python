from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

# Create a window
root = Tk()
root.title('Google dalat')
root.geometry("500x630")
root.iconbitmap('vjp.png')

# Load and display an image
# Add a label
load=Image.open('background.png') 
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)

name = Label(root, text="translator", fg="#FFFFFF",bd=0,bg="#000")
name.config(font=("translator Movie",30))
name.pack(pady=10)


box=Text(root,width=28,height=8,font=("ROBOTO",16))
box.pack(pady=20)

button_frame=Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    INPUT = box.get(1.0,END)
    t = Translator()
    a = t.translate(INPUT, src='vi')
    b=  a.text
    print(INPUT)
    box1.insert(END,b)
clear_button=Button(button_frame,text="clear text",font=(("Arial"),10,'bold'),bg="#FFFFFF",fg="#303030",command=clear)
clear_button.place(x=100,y=310)
trans_button=Button(button_frame,text="Translate",font=(("Arial"),10,'bold'),bg="#FFFFFF",fg="#303030",command=translate)
trans_button.place(x=300,y=310)
history_button=Button(button_frame,text="history text",font=(("Arial"),10,'bold'),bg="#FFFFFF",fg="#303030")
history_button.place(x=200,y=310)
box1=Text(root,width=28,height=8,font=("ROBOTO",16))
box1.pack(pady=50)
# Start the main loop
root.mainloop()


