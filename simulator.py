from Tkinter import *
from tkSimpleDialog import *
from datetime import datetime
import Graph
import Visuals
import Body

heart = Body.Heart()

main = Tk()

titleText = StringVar()

def updateName():
    newName = askstring("Input", "Patient Name:", parent=main)

    if newName is not None:
        titleText.set("SUBJECT: " + newName)

def updateHeartRate():
    newRate = askinteger("Input", "Heart Rate:", parent=main)

    if newRate is not None:
        heart.setHeartRate(newRate)

# Menu
menubar = Menu(main)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Name", command=updateName)
filemenu.add_command(label="Heart Rate", command=updateHeartRate)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

main.config(menu=menubar)

# Title
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
heartRateGraph = Graph.GraphHeartRate(statsCollection, 1, heart)

# Row 2
bpGraph = Graph.GraphBloodpressure(statsCollection, 2, heart)

# Row 3
waveGraph = Graph.GraphWave(statsCollection, 3)

# Visuals
visualsCollection = Visuals.Visuals(frame, heart)

# Bottom
bottom = Frame(main)
bottom.pack(side=TOP)

timeText = StringVar()
timeLabel = Label(bottom, textvariable=timeText, font=("Arial Bold", 36))
timeLabel.pack()


titleText.set("SUBJECT: SMITH, JOHN")
timeText.set("3:05 PM")

def updateSimulation():
    # heart
    heart.update()

    # random
    randomGraph.update()

    # heart rate
    heartRateGraph.update()

    # bp graph
    bpGraph.update()

    # wave
    waveGraph.update()

    # visuals
    visualsCollection.update()

    # Time box
    timeText.set(datetime.now().time())

    # reset tick
    main.after(200, updateSimulation)

updateSimulation()
main.mainloop()
