import random 
import tkinter as tk
import time
from tkinter import PhotoImage
import mysql.connector
from tkinter import *
from tkinter import messagebox
import os 

mydb = mysql.connector.connect(host="localhost",user="root",password="",database="program")
cursor = mydb.cursor()
window=tk.Tk()
window.geometry("1200x800")
window.title("Muthu's Rock paper scissor game")
USER_SCORE=0
COMP_SCORE=0
USER_CHOICE=""
COMP_CHOICE=""
reg = Label(window, text="Rock paper scissor game ",width=20,font=("bold",20),background='yellow')
reg.grid(column=8,row=1)
def choice_to_num(choice):
    rps={'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def num_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'} 
    return rps[number]
def random_com_choice():
    return random.choice(['rock','paper','scissor'])
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_num(human_choice)
    comp=choice_to_num(comp_choice)
    if(user==comp):
        sql="INSERT INTO game VALUES('Game tied',%s,%s)"
        usc = USER_CHOICE
        csc = COMP_CHOICE
        cursor.execute(sql,(usc,csc))
        mydb.commit()
    elif((user-comp)%3==1):
        sql="INSERT INTO game VALUES('Human wins',%s,%s)"
        usc = USER_CHOICE
        csc = COMP_CHOICE
        cursor.execute(sql,(usc,csc))
        mydb.commit()
        USER_SCORE+=1
    else:
        COMP_SCORE+=1
        sql="INSERT INTO game VALUES('Computer wins',%s,%s)"
        usc = USER_CHOICE
        csc = COMP_CHOICE
        cursor.execute(sql,(usc,csc))
        mydb.commit()
    text_area=tk.Text(master=window,height=12,width=30,bg="skyblue")
    text_area.grid(column=8,row=7)
    answer="Your choice:{uc} \nComputer's Choice:{cc}\n Your score:{u}\nComputer Score:{c}".format(uc=USER_CHOICE,cc=COMP_CHOICE,c=COMP_SCORE,u=USER_SCORE)
    text_area.insert(tk.END,answer)
    if USER_SCORE >= 5:
        messagebox.showinfo("Result", "Human have won 5 matches")
        USER_SCORE=0
        COMP_SCORE=0
    if COMP_SCORE >= 5:
        messagebox.showinfo("Result", "Computer have won 5 matches")
        USER_SCORE=0
        COMP_SCORE=0

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_com_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_com_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_com_choice()
    result(USER_CHOICE,COMP_CHOICE)
def quit():
    window.destroy()

def animate():
    animation_window_width=800
    animation_window_height=600
    animation_ball_start_xpos = 50
    animation_ball_start_ypos = 50
    animation_ball_radius = 30
    animation_ball_min_movement = 5
    animation_refresh_seconds = 0.01
    def create_animation_window():
        window = tk.Tk()
        window.title("Tkinter Animation Demo")
        window.geometry(f'{animation_window_width}x{animation_window_height}')
        return window

    def create_animation_canvas(window):
        canvas = tk.Canvas(window)
        canvas.configure(bg="black")
        canvas.pack(fill="both", expand=True)
        return canvas

    def animate_ball(window, canvas,xinc,yinc):
        ball = canvas.create_oval(animation_ball_start_xpos-animation_ball_radius,
        animation_ball_start_ypos-animation_ball_radius,
        animation_ball_start_xpos+animation_ball_radius,
        animation_ball_start_ypos+animation_ball_radius,
        fill="blue", outline="white", width=4)
        while True:
            canvas.move(ball,xinc,yinc)
            window.update()
            time.sleep(animation_refresh_seconds)
            ball_pos = canvas.coords(ball)
            xl,yl,xr,yr = ball_pos
            if xl < abs(xinc) or xr > animation_window_width-abs(xinc):
                xinc = -xinc
            if yl < abs(yinc) or yr > animation_window_height-abs(yinc):
                yinc = -yinc
    animation_window = create_animation_window()a
    animation_canvas = create_animation_canvas(animation_window)
    animate_ball(animation_window,animation_canvas, animation_ball_min_movement, animation_ball_min_movement)

def popupmsg():
    messagebox.showinfo("Information","Points is given based on the rules\n1.rock crushes scissors or sometimes blunts scissors\n2.paper covers rock\n3.scissors cuts paper")
    

roc = PhotoImage(file=r"stone.png")
roc= roc.subsample(20,16) 
pap = PhotoImage(file=r"pap.gif")
pap= pap.subsample(2,2) 
sic = PhotoImage(file=r"sci.gif")
sic=sic.subsample(5,5)
side=Label()
side.grid(column=4,row=5)
button1=tk.Button(text="Rock",bg="skyblue",image=roc,command=rock)
button1.grid(column=6,row=5)
button2=tk.Button(text="Paper",bg="white",image=pap,command=paper)
button2.grid(column=8,row=5)
button3=tk.Button(text="Scissor",bg="brown",image=sic,command=scissor)
button3.grid(column=10,row=5)
button4=tk.Button(text="Stop",command=quit,height=2,width=15,activebackground="red",bg="green")
button4.grid(column=10,row=10)
button5=tk.Button(text="Rules of the game",command=popupmsg,height=2,width=15,activebackground="red",bg="green")
button5.grid(column=6,row=10)
button6=tk.Button(text="Animate",command=animate,height=2,width=15,activebackground="red",bg="green")
button6.grid(column=8,row=12)
pic = PhotoImage(file=r"all.gif")
label = tk.Label(image = pic)
label.grid(column=8,row=10)


window.mainloop() 
