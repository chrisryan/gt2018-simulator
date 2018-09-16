from Tkinter import *
from PIL import Image, ImageTk
from random import randint

# Classes
class Visuals:
    visualsWidth = 474
    visualsHeight = 712
    sourceImages = []
    brainSectors = []

    def __init__(self, parentWidget):
        visualCollection = Frame(parentWidget)
        visualCollection.pack(side=LEFT)

        self.visual = Canvas(visualCollection, relief=RAISED, width=474, height=712, bg="green")
        self.visual.pack(side=LEFT);

        self.loadImage("images/person_background.png", 0, 0)

        self.loadImage("images/brain_background.png", 10, 20)

        self.brainSectors.append(self.loadImage("images/brain_blue.png", 10, 20))
        self.brainSectors.append(self.loadImage("images/brain_green.png", 10, 20))
        self.brainSectors.append(self.loadImage("images/brain_red.png", 10, 20))
        self.brainSectors.append(self.loadImage("images/brain_yellow.png", 10, 20))
        self.brainSectors.append(self.loadImage("images/brain_purple.png", 10, 20))

        self.loadImage("images/brain_foreground.png", 10, 20)


    def loadImage(self, filename, x, y):
        image = Image.open(filename)
        imageP = ImageTk.PhotoImage(image)
        self.sourceImages.append(imageP)
        return self.visual.create_image(x, y, anchor=NW, image=imageP)

    def update(self):
        # brain sectors
        sector = self.brainSectors[randint(0, 4)]
        if randint(1, 3) == 1:
            self.visual.itemconfig(sector, state=HIDDEN)
        else:
            self.visual.itemconfig(sector, state=NORMAL)
