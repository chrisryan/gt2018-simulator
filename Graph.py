from Tkinter import *
from random import randint
from time import time
import math

# help functions
def getCurrentMilli():
    return int(round(time() * 1000))

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
    baseY = 100
    items = []
    def __init__(self, parentWidget, rowNum, heartRate):
        GraphRow.__init__(self, parentWidget, rowNum)
        self.setHeartRate(heartRate)
        self.lastBeat = getCurrentMilli()

    def update(self):
        self.lastX = self.lastX + 10
        if self.lastX > self.graphWidth:
            self.lastX = 10

        currentMilli = getCurrentMilli()
        deltaTime = currentMilli - self.lastBeat
        if deltaTime > self.timeBetweenBeats:
            # do heart beat
            xy = [
                self.lastX-10, self.baseY, self.lastX-7, self.baseY-60,
                self.lastX-7, self.baseY-60, self.lastX-3, self.baseY+20,
                self.lastX-3, self.baseY+20, self.lastX, self.baseY
            ]
            self.items.append(self.graph.create_line(xy, fill="red"))
            self.lastBeat = currentMilli
        else:
            self.items.append(self.graph.create_line(self.lastX-10, self.baseY, self.lastX, self.baseY, fill="red"))

        while len(self.items) > 65:
            self.graph.delete(self.items.pop(0))

    def setHeartRate(self, heartRate):
        self.heartRate = heartRate
        self.value.set(heartRate)
        self.timeBetweenBeats = self.heartRateToMilli(heartRate)

    def heartRateToMilli(self, heartRate):
        return 60000 / heartRate

class GraphWave(GraphRow):
    items = []
    frequency = 6
    amplitude = 50
    speed = 1

    def __init__(self, parentWidget, rowNum):
        GraphRow.__init__(self, parentWidget, rowNum)
        self.graph.create_line(0, self.graphHeight/2, self.graphWidth, self.graphHeight/2, fill="gray")
    def update(self):
        xy = []
        for x in range(0, self.graphWidth):
            y = 39 + int(self.amplitude + self.amplitude*math.sin(self.frequency*((float(x)/self.graphWidth)*(2*math.pi) + (self.speed*time()))))
            xy.append(x)
            xy.append(y)

        self.items.append(self.graph.create_line(xy, fill="yellow"))

        while len(self.items) > 1:
            self.graph.delete(self.items.pop(0))

        moveToward = (self.frequency - randint(4, 8)) / 10.0
        self.frequency -= moveToward

        self.value.set(int(self.frequency * 100) / 10.0)
