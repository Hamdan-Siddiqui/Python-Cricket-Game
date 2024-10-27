from tkinter import *
import random
import os

root=Tk()
root.title("Python Cricket Game")
current_directory = os.path.dirname(os.path.abspath(__file__))

print(current_directory)

single = PhotoImage(file=(f"{current_directory}/single.gif"))
double = PhotoImage(file=(f"{current_directory}/double.gif"))
triple = PhotoImage(file=(f"{current_directory}/triple.gif"))
four = PhotoImage(file=(f"{current_directory}/four.gif"))
five = PhotoImage(file=(f"{current_directory}/five.gif"))
six = PhotoImage(file=(f"{current_directory}/six.gif"))
player_out = PhotoImage(file=(f"{current_directory}/player_out.gif"))
comp_out = PhotoImage(file=(f"{current_directory}/comp_out.gif"))
won = PhotoImage(file=(f"{current_directory}/won.gif"))
lost = PhotoImage(file=(f"{current_directory}/lost.gif"))
draw = PhotoImage(file=(f"{current_directory}/draw.gif"))

bat_score = 0
ball_score = 0
bat_turn = 0
ball_turn = 0
comp_bat = 0
comp_ball = 0
status = []
def bat_score_addendum(number):
    global bat_score
    global bat_turn
    global comp_ball
    global status
    comp_ball = random.randint(1,6)
    bat_turn = number
    bat_score += number
    
    if bat_turn == comp_ball:
        clear_frame()
        out_text = Label(root,text=("You're out"))
        out_text.grid(row=1,column=1)
        status.append("batting done")
        player_out_gif = Label(root, image=player_out)
        player_out_gif.grid(row=0,column=1)
        button_shift_bat = Button(root, text="Continue",padx=60,pady=30,command=lambda:inning_shift(),bg="black",fg="white")
        button_shift_bat.grid(row=2,column=1)
    else:
        clear_frame()
        player_bat()
    if bat_turn != comp_ball:    
        gif_get()

def gif_get():
    global bat_turn
    global ball_turn
    global single, double, triple, four, five, six
    
    # Dictionary mapping turns to images
    images = {
        1: single,
        2: double,
        3: triple,
        4: four,
        5: five,
        6: six
    }
    
    current_turn = bat_turn if bat_turn in images else ball_turn
    
    if current_turn in images:
        print(f"Printing {images[current_turn]}")
        gif_label = Label(root, image=images[current_turn])
        gif_label.grid(row=0, column=1)
        print(f"Displaying gif for turn {current_turn}")



def ball_score_addendum(number):
    global ball_score
    global ball_turn
    global comp_bat
    global status
    comp_bat = random.randint(1,6)
    ball_turn = number
    ball_score += number
    
    if comp_bat == ball_turn:
        clear_frame()
        out_text = Label(root,text=("The computer is out"))
        out_text.grid(row=1,column=1)
        status.append("balling done")
        comp_out_gif = Label(root, image=comp_out)
        comp_out_gif.grid(row=0,column=1)
        button_shift_ball = Button(root, text="Continue",padx=60,pady=30,command=lambda:inning_shift(),bg="black",fg="white")
        button_shift_ball.grid(row=2,column=1)
    else:
        clear_frame()
        player_ball()
    if ball_turn != comp_bat:    
        gif_get()
    
    
def clear_frame(): 
    print("Clearing Frame")
    for widget in root.winfo_children():
        widget.destroy()
    
def play_page():
    clear_frame()
    play_title = Label(root,text="Python Cricket Game")
    play_title.grid(row=0,column=0)
    button_play = Button(root, text="New Game",padx=60,pady=30,command=toss_page,bg="black",fg="white")
    button_kill = Button(root, text="Exit",padx=60,pady=30,command=root.quit,bg="black",fg="white")
    button_play.grid(row=1,column=0)
    button_kill.grid(row=2,column=0)

def toss_page():
    clear_frame()
    toss_title = Label(root,text="The coin is in the air, what's your call")
    toss_title.grid(row=0,column=0)
    button_heads = Button(root, text="Heads",padx=60,pady=30,command=lambda:toss_choice("Heads"),bg="black",fg="white")
    button_tails = Button(root, text="Tails",padx=60,pady=30,command=lambda:toss_choice("Tails"),bg="black",fg="white")
    button_heads.grid(row=1,column=0)
    button_tails.grid(row=2,column=0)
    
def toss_choice(call):
    comp_choice = random.choice(["Heads","Tails"])
    # Computer wins the toss
    if comp_choice == call:
        clear_frame()
        global comp_choice2
        comp_choice2 = random.choice(["bat","bowl"])
        result = Label(root,text=("The computer won the toss. It has chosen to " + comp_choice2))
        result.grid(row=0,column=0)
        if comp_choice2 == "bat":
            button_continue = Button(root, text="Continue",padx=60,pady=30,command=lambda:player_ball(),bg="black",fg="white")
            button_continue.grid(row=1,column=0)
        else:
            button_continue = Button(root, text="Continue",padx=60,pady=30,command=lambda:player_bat(),bg="black",fg="white")
            button_continue.grid(row=1,column=0)
    else:
        clear_frame()
        result = Label(root,text="You've won the toss. What'll you choose ?")
        result.grid(row=0,column=0)
        button_bat = Button(root, text="Bat",padx=60,pady=30,command=lambda:player_bat(),bg="black",fg="white")
        button_ball = Button(root, text="Bowl",padx=60,pady=30,command=lambda:player_ball(),bg="black",fg="white")
        button_bat.grid(row=1,column=0) 
        button_ball.grid(row=2,column=0)
 
def player_bat():
    clear_frame()
    global bat_turn
    global bat_score
    global comp_ball
    global choice
    
    choice = "innings"
    display_ball_comp = Label(root, text=("Computer Input: " ,comp_ball))
    display_ball_comp.grid(row=1,column=2)  
    display_score_bat = Label(root,text=(bat_score))
    display_score_bat.grid(row=1,column=1)  
                
    button_1 = Button(root, text="1",padx=60,pady=30,command=lambda:bat_score_addendum(1),bg="black",fg="white")
    button_2 = Button(root, text="2",padx=60,pady=30,command=lambda:bat_score_addendum(2),bg="black",fg="white")
    button_3 = Button(root, text="3",padx=60,pady=30,command=lambda:bat_score_addendum(3),bg="black",fg="white")
    button_4 = Button(root, text="4",padx=60,pady=30,command=lambda:bat_score_addendum(4),bg="black",fg="white")
    button_5 = Button(root, text="5",padx=60,pady=30,command=lambda:bat_score_addendum(5),bg="black",fg="white")
    button_6 = Button(root, text="6",padx=60,pady=30,command=lambda:bat_score_addendum(6),bg="black",fg="white")

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=3,column=0)
    button_5.grid(row=3,column=1)
    button_6.grid(row=3,column=2)

def player_ball():
    global ball_turn
    global ball_score
    global comp_bat
            
    display_ball_comp = Label(root, text=("Computer Input: " ,comp_bat))
    display_ball_comp.grid(row=1,column=2)  
    display_score_bat = Label(root,text=(ball_score))
    display_score_bat.grid(row=1,column=1)  
                
    button_1 = Button(root, text="1",padx=60,pady=30,command=lambda:ball_score_addendum(1),bg="black",fg="white")
    button_2 = Button(root, text="2",padx=60,pady=30,command=lambda:ball_score_addendum(2),bg="black",fg="white")
    button_3 = Button(root, text="3",padx=60,pady=30,command=lambda:ball_score_addendum(3),bg="black",fg="white")
    button_4 = Button(root, text="4",padx=60,pady=30,command=lambda:ball_score_addendum(4),bg="black",fg="white")
    button_5 = Button(root, text="5",padx=60,pady=30,command=lambda:ball_score_addendum(5),bg="black",fg="white")
    button_6 = Button(root, text="6",padx=60,pady=30,command=lambda:ball_score_addendum(6),bg="black",fg="white")

    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)
    button_4.grid(row=3,column=0)
    button_5.grid(row=3,column=1)
    button_6.grid(row=3,column=2)

def inning_shift(): 
    global won, draw, lost   
    if status == ["batting done"] and not status == ["balling done"]:
        clear_frame()
        player_ball()
    elif status == ["balling done"] and not status == ["batting done"]:
        clear_frame()
        player_bat()
    elif status == ["batting done","balling done"] or status == ["balling done", "batting done"]:
        if bat_score > ball_score:
            clear_frame()
            won_gif = Label(root, image=won)
            won_gif.grid(row=0, column=1)
            won = Label(root,text=("You've won!!!"))
            won.grid(row=1,column=1)
            button_return = Button(root, text="Return to Homepage",padx=60,pady=30,command=lambda:play_page(),bg="black",fg="white")
            button_return.grid(row=2,column=1)
            status.clear()
        elif bat_score == ball_score:
            clear_frame()
            draw_gif = Label(root, image=draw)
            draw_gif.grid(row=0, column=1)
            draw = Label(root,text=("It's a draw"))
            draw.grid(row=1,column=1)
            button_return = Button(root, text="Return to Homepage",padx=60,pady=30,command=lambda:play_page(),bg="black",fg="white")
            button_return.grid(row=2,column=1)
            status.clear()
        else:
            clear_frame()
            lost_gif = Label(root, image=lost)
            lost_gif.grid(row=0, column=1)
            lost = Label(root,text=("You've lost the game"))
            lost.grid(row=1,column=1)
            button_return = Button(root, text="Return to Homepage",padx=60,pady=30,command=lambda:play_page(),bg="black",fg="white")
            button_return.grid(row=2,column=1)
            status.clear()

play_page()

root.mainloop()