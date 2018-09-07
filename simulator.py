from Tkinter import *
from random import randint
from datetime import datetime
import time

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

#  Row 1
row0Text = StringVar()
row0TextLabel = Label(statsCollection, textvariable=row0Text, relief=RAISED, bd=10, width=4, height=2, bg="yellow", font=("Arial Bold", 50))
row0TextLabel.grid(row=0, column=0);

row0Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row0Graph.grid(row=0, column=1);

row1Text = StringVar()
row1TextLabel = Label(statsCollection, textvariable=row1Text, relief=RAISED, bd=10, width=4, height=2, bg="blue", font=("Arial Bold", 50))
row1TextLabel.grid(row=1, column=0);

row1Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row1Graph.grid(row=1, column=1);

row2Text = StringVar()
row2TextLabel = Label(statsCollection, textvariable=row2Text, relief=RAISED, bd=10, width=4, height=2, bg="red", font=("Arial Bold", 50))
row2TextLabel.grid(row=2, column=0);

row2Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row2Graph.grid(row=2, column=1);

row3Text = StringVar()
row3TextLabel = Label(statsCollection, textvariable=row3Text, relief=RAISED, bd=10, width=4, height=2, bg="pink", font=("Arial Bold", 50))
row3TextLabel.grid(row=3, column=0);

row3Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row3Graph.grid(row=3, column=1);


visualCollection = Frame(frame)
visualCollection.pack(side=LEFT)

visual = Canvas(visualCollection, relief=RAISED, width=474, height=712, bg="green")
visual.pack(side=LEFT);

# Bottom
bottom = Frame(main)
bottom.pack(side=TOP)

timeText = StringVar()
timeLabel = Label(bottom, textvariable=timeText, font=("Arial Bold", 36))
timeLabel.pack()



titleText.set("SUBJECT: SMITH, JOHN")
row0Text.set("54")
row1Text.set("99")
row2Text.set("12")
row3Text.set("63")
timeText.set("3:05 PM")

def getCurrentMilli():
    return int(round(time.time() * 1000))

def heartRateToMilli(heartRate):
    return 60000 / heartRate

# row0Graph 712x178
items = []
lastX = 0;
lastY = 89;

# row1Graph 712x178
items2 = []
lastBeat = getCurrentMilli()
heartRate = 48;
timeBetweenBeats = heartRateToMilli(heartRate)

def updateSimulation():
    # Random Graph
    global lastX
    global lastY
    nextX = lastX + 10
    if nextX > 712:
        nextX = 10
        lastX = 0
    nextY = randint(20, 158)
    items.append(row0Graph.create_line(lastX, lastY, nextX, nextY, fill="red"))
    lastX = nextX
    lastY = nextY

    row0Text.set(lastY)

    if len(items) > 65:
        row0Graph.delete(items.pop(0))

    # heart rate
    global lastBeat
    global heartRate
    currentMilli = getCurrentMilli()
    deltaTime = currentMilli - lastBeat
    if deltaTime > timeBetweenBeats:
        # do heart beat
        items2.append(row1Graph.create_line(lastX-10, 89, lastX-7, 89-60, fill="red"))
        items2.append(row1Graph.create_line(lastX-7, 89-60, lastX-3, 89+20, fill="red"))
        items2.append(row1Graph.create_line(lastX-3, 89+20, lastX, 89, fill="red"))
        lastBeat = currentMilli
    else:
        items2.append(row1Graph.create_line(lastX-10, 89, lastX, 89, fill="red"))

    while len(items2) > 85:
        row1Graph.delete(items2.pop(0))

    row1Text.set(heartRate)

    # Time box
    timeText.set(datetime.now().time())

    # reset tick
    main.after(200, updateSimulation)

updateSimulation()
main.mainloop()
