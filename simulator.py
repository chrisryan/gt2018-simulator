from Tkinter import *
from PIL import Image, ImageTk
from datetime import datetime
from random import randint
import Graph

main = Tk()

# Title
titleText = StringVar()
title = Label(main, textvariable=titleText, relief=RAISED, justify=LEFT, font=("Arial Bold", 18))
title.pack(fill="x", side=TOP)

# Center
frame = Frame(main)
frame.pack(side=TOP)

statsCollection = Frame(frame)
statsCollection.pack(side=LEFT)

#  Row 0
randomGraph = Graph.GraphRandom(statsCollection, 0)

# Row 1
heartRateGraph = Graph.GraphHeartRate(statsCollection, 1, 48)

# Row 2
bpGraph = Graph.GraphBloodpressure(statsCollection, 2, 48)

# Row 3
waveGraph = Graph.GraphWave(statsCollection, 3)


visualCollection = Frame(frame)
visualCollection.pack(side=LEFT)

visual = Canvas(visualCollection, relief=RAISED, width=474, height=712, bg="green")
visual.pack(side=LEFT);

body = Image.open("images/person_background.png")
bodyP = ImageTk.PhotoImage(body)
visual.create_image(0, 0, anchor=NW, image=bodyP)

brainBack = Image.open("images/brain_background.png")
brainBackP = ImageTk.PhotoImage(brainBack)
visual.create_image(10, 20, anchor=NW, image=brainBackP)

brainSectors = []

brainBlue = Image.open("images/brain_blue.png")
brainBlueP = ImageTk.PhotoImage(brainBlue)
brainSectors.append(visual.create_image(10, 20, anchor=NW, image=brainBlueP))

brainPurple = Image.open("images/brain_purple.png")
brainPurpleP = ImageTk.PhotoImage(brainPurple)
brainSectors.append(visual.create_image(10, 20, anchor=NW, image=brainPurpleP))

brainGreen = Image.open("images/brain_green.png")
brainGreenP = ImageTk.PhotoImage(brainGreen)
brainSectors.append(visual.create_image(10, 20, anchor=NW, image=brainGreenP))

brainRed = Image.open("images/brain_red.png")
brainRedP = ImageTk.PhotoImage(brainRed)
brainSectors.append(visual.create_image(10, 20, anchor=NW, image=brainRedP))

brainYellow = Image.open("images/brain_yellow.png")
brainYellowP = ImageTk.PhotoImage(brainYellow)
brainSectors.append(visual.create_image(10, 20, anchor=NW, image=brainYellowP))

brainFront = Image.open("images/brain_foreground.png")
brainFrontP = ImageTk.PhotoImage(brainFront)
visual.create_image(10, 20, anchor=NW, image=brainFrontP)

# Bottom
bottom = Frame(main)
bottom.pack(side=TOP)

timeText = StringVar()
timeLabel = Label(bottom, textvariable=timeText, font=("Arial Bold", 36))
timeLabel.pack()


titleText.set("SUBJECT: SMITH, JOHN")
timeText.set("3:05 PM")

def updateSimulation():
    # random
    randomGraph.update()

    # heart rate
    heartRateGraph.update()

    # bp graph
    bpGraph.update()

    # wave
    waveGraph.update()

    # brain sectors
    sector = brainSectors[randint(0, 4)]
    if randint(1, 3) == 1:
        visual.itemconfig(sector, state=HIDDEN)
    else:
        visual.itemconfig(sector, state=NORMAL)

    # Time box
    timeText.set(datetime.now().time())

    # reset tick
    main.after(200, updateSimulation)

updateSimulation()
main.mainloop()
