#This project contains data from an API called "NBA Player Individual Stats" created by Kaylan on RapidAPI
import tkinter as tk
import requests
from tkinter import font

h=600
w=600

#Allows stats to appear on GUI
def GUI_format(stats):
    try:
        points = (stats['careerPoints'])
        assists = (stats['carrerAssists'])
        rebounds = (stats['careerRebounds'])
        threePoint = (stats['careerPercentageThree'])
        freeThrow = (stats['careerPercentageFreethrow'])
        fieldGoal = (stats['careerPercentageFieldGoal'])

        formatstr = 'Points Per Game: %s \nAssists Per Game: %s \nRebounds Per Game: %s \n3pt Shot Percentage: %s \nFree Throw Percentage: %s \nField Goal Percentage: %s \n' %(points, assists, rebounds, threePoint, freeThrow, fieldGoal) 
    except:
        formatstr = 'Information on that player could not be found'

    return formatstr

#Modified code snippet from API
def get_stats(name):

    url = "https://nba-player-individual-stats.p.rapidapi.com/players/fullname"

    querystring = {"name":name}

    headers = {
        'x-rapidapi-host': "nba-player-individual-stats.p.rapidapi.com",
        'x-rapidapi-key': "ec51f06a65msh7a39c0eaef9c8c0p1a6354jsn717acefbac3e"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    stats = response.json()

    stat_label['text'] = GUI_format(stats)

#Design of GUI
root = tk.Tk()

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

frame = tk.Frame(root, bg='#CFC6BE')
frame.place(relx=0.1, rely=0.1, relwidth=.8, relheight=.8)

label = tk.Label(frame, text="FIND CURRENT NBA PLAYER'S CAREER STATS!", font=('Lucida Sans', 15), bg='#CFC6BE')
label.place(relx = 0.5, rely = 0.1, anchor = 'center')

secondlabel = tk.Label(frame, text="Typing format example: julius_randle",font=('Lucida Sans', 11), bg='#CFC6BE')
secondlabel.place(relx = 0.5, rely = 0.225, anchor = 'center')

entry = tk.Entry(frame, bg='white')
entry.place(relx=.15, rely=.15, relheight=.05, relwidth=.7)

button = tk.Button(frame, text ="Get Stats", bg='white', command=lambda: get_stats(entry.get()))
button.place(relx=.4, rely=.4, relheight=.1, relwidth=.2)

pictureFrame = tk.Label(frame, bg='white')
pictureFrame.place(relx=.075, rely=.30, relwidth=.25, relheight=.25)

background_image2 = tk.PhotoImage(file='MJ6.png')
backround_label2 = tk.Label(pictureFrame, image=background_image2)
backround_label2.place(x=0, y=0, relheight=1, relwidth=1)

pictureFrame2 = tk.Label(frame, bg='white')
pictureFrame2.place(relx=.675, rely=.30, relwidth=.25, relheight=.25)

background_image = tk.PhotoImage(file='MJ6.png')
backround_label = tk.Label(pictureFrame2, image=background_image)
backround_label.place(x=0, y=0, relheight=1, relwidth=1)

low_frame = tk.Label(frame, bg='white')
low_frame.place(relx=.075, rely=.6, relwidth=.85, relheight=.35)

stat_label = tk.Label(low_frame, font=('Lucida Sans', 12))
stat_label.place(relwidth=1,relheight=1)

root.mainloop()