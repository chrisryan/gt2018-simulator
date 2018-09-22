from Tkinter import *
from PIL import Image, ImageTk
from random import randint

# Classes
class Visuals:
    visualsWidth = 474
    visualsHeight = 712
    sourceImages = []

    def __init__(self, parentWidget):
        visualCollection = Frame(parentWidget)
        visualCollection.pack(side=LEFT)

        self.visual = Canvas(visualCollection, relief=RAISED, width=474, height=712, bg="green")
        self.visual.pack(side=LEFT);

        self.loadImage("images/person_background.png", 0, 0)

        self.brain = BrainVisual(self)
        self.heart = HeartVisual(self)
        self.bars = BarGroupVisual(self, self.visualsHeight - 50)

    def loadImage(self, filename, x, y):
        image = Image.open(filename)
        imageP = ImageTk.PhotoImage(image)
        self.sourceImages.append(imageP)
        return self.visual.create_image(x, y, anchor=NW, image=imageP)

    def update(self):
        self.brain.update()
        self.heart.update()
        self.bars.update()

class BrainVisual:
    brainSectors = []

    def __init__(self, visuals):
        self.visuals = visuals

        visuals.loadImage("images/brain_background.png", 10, 20)

        self.brainSectors.append(visuals.loadImage("images/brain_blue.png", 10, 20))
        self.brainSectors.append(visuals.loadImage("images/brain_green.png", 10, 20))
        self.brainSectors.append(visuals.loadImage("images/brain_red.png", 10, 20))
        self.brainSectors.append(visuals.loadImage("images/brain_yellow.png", 10, 20))
        self.brainSectors.append(visuals.loadImage("images/brain_purple.png", 10, 20))

        visuals.loadImage("images/brain_foreground.png", 10, 20)

    def update(self):
        # brain sectors
        sector = self.brainSectors[randint(0, 4)]
        if randint(1, 3) == 1:
            self.visuals.visual.itemconfig(sector, state=HIDDEN)
        else:
            self.visuals.visual.itemconfig(sector, state=NORMAL)

class HeartVisual:
    tick = 0

    def __init__(self, visuals):
        self.visuals = visuals
        visuals.loadImage("images/heart.png", 20, 240)
        self.text = visuals.visual.create_text(130, 330, text="123", fill="yellow", font=("Arial Bold", 36))

    def update(self):
        self.tick = self.tick + 1
        if self.tick >= 10:
            self.tick = 0
        self.visuals.visual.itemconfig(self.text, font=("Arial Bold", 40 - self.tick))

class BarGroupVisual:
    bars = []

    def __init__(self, visuals, baseY):
        self.bars.append(BarVisual(visuals, 20, baseY))
        self.bars.append(BarVisual(visuals, 70, baseY))
        self.bars.append(BarVisual(visuals, 120, baseY))
        self.bars.append(BarVisual(visuals, 170, baseY))
        self.bars.append(BarVisual(visuals, 220, baseY))

    def update(self):
        for bar in self.bars:
            bar.update()

class BarVisual:
    maxHeight = 150
    width = 30
    tick = 0
    tickReset = 10
    goal = 60

    def __init__(self, visuals, x, y):
        self.visuals = visuals

        self.bar = visuals.visual.create_rectangle(x, y, x + self.width, y - self.maxHeight, fill="cyan")

    def update(self):
        x0, y0, x1, y1 = self.visuals.visual.coords(self.bar)
        delta = randint(0, 5)
        if (y1 - y0) > self.goal:
            delta = delta * -1;
        self.visuals.visual.coords(self.bar, x0, y0 - delta, x1, y1)

        self.tick = self.tick + 1;
        if self.tick > self.tickReset:
            self.tick = 0
            self.tickReset = randint(5, 15)

            self.goal = randint(0, self.maxHeight)
