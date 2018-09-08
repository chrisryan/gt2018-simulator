from Tkinter import *
from random import randint
from datetime import datetime
import time

# Classes
class GraphRow:
    graphWidth = 712
    graphHeight = 178

    def __init__(self, parentWidget, rowNum):
        self.value = StringVar()
        self.label = Label(parentWidget, textvariable=self.value, relief=RAISED, bd=10, width=4, height=2, fg="yellow", bg="black", font=("Arial Bold", 50))
        self.graph = Canvas(parentWidget, relief=RAISED, width=self.graphWidth, height=self.graphHeight, bg="black")

        self.label.grid(row=rowNum, column=0)
        self.graph.grid(row=rowNum, column=1)

class GraphRandom(GraphRow):
    lastX = 0
    lastY = 0
    items = []
    def update(self):
        nextX = self.lastX + 10
        if nextX > self.graphWidth:
            nextX = 10
            self.lastX = 0
        nextY = randint(20, self.graphHeight - 20)
        self.items.append(self.graph.create_line(self.lastX, self.lastY, nextX, nextY, fill="red"))

        self.lastX = nextX
        self.lastY = nextY

        self.value.set(self.lastY)

        if len(self.items) > 65:
            self.graph.delete(self.items.pop(0))

class GraphHeartRate(GraphRow):
    lastX = 0
    baseY = 60
    items = []
    def __init__(parentWidget, rowNum, heartRate):
        GraphRow.__init__(self, parentWidget, rowNum)
        self.setHeartRate(heartRate)
        self.lastBeat = getCurrentMilli()

    def update(self):
        self.lastX = self.lastX + 10

        currentMilli = getCurrentMilli()
        deltaTime = currentMilli - lastBeat
        if deltaTime > self.timeBetweenBeats:
            # do heart beat
            items2.append(self.graph.create_line(self.lastX-10, self.baseY, self.lastX-7, self.baseY-60, fill="red"))
            items2.append(self.graph.create_line(self.lastX-7, self.baseY-60, self.lastX-3, self.baseY+20, fill="red"))
            items2.append(self.graph.create_line(self.lastX-3, self.baseY+20, self.lastX, self.baseY, fill="red"))
            self.lastBeat = currentMilli
        else:
            items2.append(self.graph.create_line(self.lastX-10, 89, self.lastX, 89, fill="red"))

        while len(items2) > 85:
            self.graph.delete(items2.pop(0))

    def setHeartRate(heartRate):
        self.heartRate = heartRate
        self.value.set(heartRate)
        self.timeBetweenBeats = heartRateToMilli(heartRate)


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
randomGraph = GraphRandom(statsCollection, 0)

# Row 1
row1Text = StringVar()
row1TextLabel = Label(statsCollection, textvariable=row1Text, relief=RAISED, bd=10, width=4, height=2, bg="blue", font=("Arial Bold", 50))
row1TextLabel.grid(row=1, column=0);

row1Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row1Graph.grid(row=1, column=1);

# Row 2
row2Text = StringVar()
row2TextLabel = Label(statsCollection, textvariable=row2Text, relief=RAISED, bd=10, width=4, height=2, bg="red", font=("Arial Bold", 50))
row2TextLabel.grid(row=2, column=0);

row2Graph = Canvas(statsCollection, relief=RAISED, width=712, height=178, bg="black")
row2Graph.grid(row=2, column=1);

# Row 3
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
row1Text.set("99")
row2Text.set("12")
row3Text.set("63")
timeText.set("3:05 PM")

def getCurrentMilli():
    return int(round(time.time() * 1000))

def heartRateToMilli(heartRate):
    return 60000 / heartRate

# row0Graph 712x178
lastX = 0;

# row1Graph 712x178
items2 = []
lastBeat = getCurrentMilli()
heartRate = 48;
timeBetweenBeats = heartRateToMilli(heartRate)

def updateSimulation():
    global lastX
    nextX = lastX + 10
    if nextX > 712:
        nextX = 10
        lastX = 0
    lastX = nextX

    # random
    randomGraph.update()

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
