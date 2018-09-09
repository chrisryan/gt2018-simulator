from Tkinter import *
from datetime import datetime
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
waveGraph = Graph.GraphWave(statsCollection, 2)

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
row3Text.set("63")
timeText.set("3:05 PM")


def updateSimulation():
    # random
    randomGraph.update()

    # heart rate
    heartRateGraph.update()

    # wave
    waveGraph.update()

    # Time box
    timeText.set(datetime.now().time())

    # reset tick
    main.after(200, updateSimulation)

updateSimulation()
main.mainloop()
