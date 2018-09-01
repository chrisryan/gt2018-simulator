from Tkinter import *

main = Tk()

# Title
titleText = StringVar()
title = Label(main, textvariable=titleText, relief=RAISED, width=100, justify=LEFT)
title.pack()

# Center
frame = Frame(main)
frame.pack(side=BOTTOM)

statsCollection = Frame(frame)
statsCollection.pack(side=LEFT)

#  Row 1
row1 = Frame(statsCollection)
row1.pack(side=LEFT)

row1Text = StringVar()
row1TextLabel = Label(row1, textvariable=row1Text,relief=RAISED, width=5, bg="yellow")
row1TextLabel.pack(side=LEFT);

row1Graph = Canvas(row1, relief=RAISED, width=600, height=200, bg="black")
row1Graph.pack(side=LEFT);


visualCollection = Frame(frame)
visualCollection.pack(side=LEFT)

visual = Canvas(visualCollection, relief=RAISED, width=300, height=600, bg="green")
visual.pack(side=LEFT);

# Bottom


titleText.set("SUBJECT: SMITH, JOHN")
row1Text.set("54")

main.mainloop()
