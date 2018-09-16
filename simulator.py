from Tkinter import *
from datetime import datetime
import Graph
import Visuals

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

# Visuals
visualsCollection = Visuals.Visuals(frame)

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

    # visuals
    visualsCollection.update()

    # Time box
    timeText.set(datetime.now().time())

    # reset tick
    main.after(200, updateSimulation)

updateSimulation()
main.mainloop()
