from Tkinter import *
from tkSimpleDialog import *
from PIL import Image, ImageTk
from datetime import datetime
import Graph
import Visuals
import Body

heart = Body.Heart()
heart.enableRandom(True)
alertDelay = 10000

main = Tk()

wImage = Image.open("images/warning.png")
wImageP = ImageTk.PhotoImage(wImage)

titleText = StringVar()

def updateName():
    newName = askstring("Input", "Patient Name:", parent=main)

    if newName is not None:
        titleText.set("SUBJECT: " + newName)

def updateHeartRate():
    newRate = askinteger("Input", "Heart Rate:", parent=main)

    if newRate is not None:
        heart.setHeartRate(newRate)
        heart.setRandomRange(newRate - 2, newRate + 2)

def toggleHeartRate():
    heart.enableRandom(not heart.getRandom())

def showAlert():
    warningW = Toplevel()
    warningW.title("Critical Alert")
    warningL = Label(warningW, image=wImageP)
    warningL.pack()

    main.update()

    m = re.match("(\d+)x(\d+).?([-+]\d+)([-+]\d+)", main.geometry())
    m = map(int, m.groups())

    x = m[0] / 2 + m[2];
    y = m[1] / 2 + m[3];

    w = re.match("(\d+)x(\d+).?([-+]\d+)([-+]\d+)", warningW.geometry())
    w = map(int, w.groups())

    size = (w[0], w[1])
    x = x - size[0] / 2
    y = y - size[1] / 2
    warningW.geometry("%dx%d+%d+%d" % (size + (x, y)))

def updateAlertDelay():
    global alertDelay;

    newDelay = askinteger("Input", "Alert Delay (Seconds):", parent=main)

    if newDelay is not None:
        alertDelay = newDelay * 1000;

def delayedAlert():
    global alertDelay;

    main.after(alertDelay, showAlert)

# Menu
menubar = Menu(main)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Name", command=updateName)
filemenu.add_command(label="Heart Rate", command=updateHeartRate)
filemenu.add_command(label="Toggle Random Rate", command=toggleHeartRate)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=main.quit)
menubar.add_cascade(label="File", menu=filemenu)

windowmenu = Menu(menubar, tearoff=0)
windowmenu.add_command(label="Alert", command=showAlert)
windowmenu.add_command(label="Alert Delay", command=updateAlertDelay)
menubar.add_cascade(label="Windows", menu=windowmenu)

main.config(menu=menubar)

# Title
title = Label(main, textvariable=titleText, relief=RAISED, justify=LEFT, font=("Arial Bold", 24))
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

startButton = Button(bottom, text="Start Simulation", command=delayedAlert)
startButton.pack(side=LEFT)

timeText = StringVar()
timeLabel = Label(bottom, textvariable=timeText, font=("Arial Bold", 24))
timeLabel.pack(side=LEFT)



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
