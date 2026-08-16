#Modules
import random
import time
from tkinter import *
import customtkinter as ctk
Master = Tk()
#Window Title
Master.title("Uping simulator V0.5 Beta release")
#Window resize setting
Master.resizable(FALSE, FALSE)
#Function that checks if buttons been pressed
def Jump_down():
    D.place(x=200, y=800)

def Button_on():
    B.configure(state="normal")

def Button_press():
    B.configure(state="disabled")

    D.place(x=200, y=750),
    Master.after(1000, Jump_down)

    B.after(1000, Button_on)

#Eye color list
Player_eyes_list = ["red", "blue", "cyan", "purple", "pink", "green", "brown", "grey"]
random.shuffle(Player_eyes_list)
#Window size and color
Master.geometry("1000x1000")
Master.configure(background="Lightblue")
#Player model
D = Canvas(
    Master,
    width=50,
    height=100,
    background="tan"
)
#Player model placement
D.place(x=200, y=800)

#Player mouth
Player_mouth = D.create_arc(
        10, 45,
        45, 45,
    fill="grey"
)
#Player eyes
Player_eyes = D.create_oval(
    5, 15,
    15, 25,
    fill=Player_eyes_list[1]
)
#Player clothes
Player_clothes = D.create_rectangle(
     60, 60,
    -5, 100,
    fill="Turquoise"


)



#Jumping button
B = ctk.CTkButton(
                 Master,
                 text="Up",
                 corner_radius=75,
                 height=40,
                 width=60,
                 fg_color="grey",
                 command=Button_press
)
#Grass
C = Canvas(
    Master,
    width=1000,
    height=200,
    background="green"
)

#Placement of button and grass
B.place(x=490, y=700)
C.place(x=-1, y=900)

#Part that makes the window actually open
mainloop()
