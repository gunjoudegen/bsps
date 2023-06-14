import sqlite3
import datetime

from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage, Image
from tkinter import filedialog

from PIL import ImageTk, Image

root = Tk()

def control_panel():

    def scoreadd():

        if team1player.get() == 'TEAM 1 PLAYERS *':
            pass

        else:
            player_to_score.delete(0, END)
            s1 = team1player.get()

            player_to_score.insert(0, s1)            

        if team2player.get() == 'TEAM 2 PLAYERS *':
            pass

        else:

            player_to_score.delete(0, END)
            s2 = team2player.get()

            player_to_score.insert(0, s2)

    def escape(event):
        if event.keysym == "Escape":
            controlpanel.destroy()


    controlpanel = Toplevel(root)
    controlpanel.geometry('1080x720+120+0')
    controlpanel.title('control panel')
    controlpanel.resizable(False, False)
    root.bind('<KeyPress>', escape)


    team1player = StringVar()
    team1player.set('TEAM 1 PLAYERS *')

    team1option = ['player 1',
                   'player 2',
                   'player 3',
                   'player 4',
                   'player 5',
                   'sub 1',
                   'sub 2',
                   'sub 3',
                   'sub 4',
                   'sub 5']
    team1_players = OptionMenu(controlpanel, team1player, *team1option)
    team1_players.config(font=('Consolas', 10), relief=FLAT, indicatoron=0, borderwidth=0)
    team1_players.place(x=50, y=50)

    team2player = StringVar()
    team2player.set('TEAM 2 PLAYERS *')

    team2option = ['player 1',
                   'player 2',
                   'player 3',
                   'player 4',
                   'player 5',
                   'sub 1',
                   'sub 2',
                   'sub 3',
                   'sub 4',
                   'sub 5']
    team2_players = OptionMenu(controlpanel, team2player, *team2option)
    team2_players.config(font=('Consolas', 10), relief=FLAT, indicatoron=0, borderwidth=0)
    team2_players.place(x=250, y=50)

    score = StringVar()
    score.set('score <')

    optionscore = ['foul',
                   '1',
                   '2',
                   '3']
    score_to_add = OptionMenu(controlpanel, score, *optionscore)
    score_to_add.config(font=('Consolas', 10), relief=FLAT, indicatoron=0, borderwidth=0)
    score_to_add.place(x=750, y=80)

    player_to_score = Entry(controlpanel, width=30, font=('Consolas', 13), relief=FLAT, borderwidth=1)
    player_to_score.place(x=750, y=50)

    confirm_player = Button(controlpanel, text='confirm player to score', font=('Consolas', 10), relief=FLAT, borderwidth=0, command=scoreadd)
    confirm_player.place(x=755, y=110)




def returnclick(event):
    if event.keysym == "Control_L":
       
        control_panel()

def scoring():
    pass

team1_scoredisplay = Label(root, text='000', font=('Consolas', 70))
team1_scoredisplay.place(x=150, y=200)
team2_scoredisplay = Label(root, text='000', font=('Consolas', 70))
team2_scoredisplay.place(x=750, y=200)


add_scoreBUTTON = Button(root, text='score [ctrl]', font=('Consolas', 12), relief=FLAT, borderwidth=0)
root.bind('<KeyPress>', returnclick)
add_scoreBUTTON.place(x=950, y=680)

root.geometry('1080x720+120+0')
root.resizable(False, False)
root.title('test scoreboard and control panel')
root.mainloop()