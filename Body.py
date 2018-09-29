from random import randint
from time import time

# help functions
def getCurrentMilli():
    return int(round(time() * 1000))

class Heart:
    heartRate = 48
    isOnBeat = False
    isPostBeat = False
    isRandom = False
    randLow = 47
    randHigh = 49
    def __init__(self):
        self.lastBeat = getCurrentMilli()
        self.setHeartRate(self.heartRate)

    def update(self):
        if self.isPostBeat:
            self.isPostBeat = False

        if self.isOnBeat:
            self.isOnBeat = False
            self.isPostBeat = True

        currentMilli = getCurrentMilli()
        self.deltaTime = currentMilli - self.lastBeat
        if self.deltaTime > self.timeBetweenBeats:
            self.isOnBeat = True
            self.lastBeat = currentMilli

            if self.isRandom and randint(1, 6) == 1:
                adjust = randint(-1, 1)

                if self.heartRate > self.randHigh:
                    adjust = -1

                if self.heartRate < self.randLow:
                    adjust = 1

                self.setHeartRate(self.heartRate + adjust)

    def onBeat(self):
        return self.isOnBeat

    def postBeat(self):
        return self.isPostBeat

    def getHeartRate(self):
        return self.heartRate

    def getDelta(self):
        return self.deltaTime

    def setHeartRate(self, heartRate):
        self.heartRate = heartRate
        self.timeBetweenBeats = self.heartRateToMilli(heartRate)

    def heartRateToMilli(self, heartRate):
        return 60000 / heartRate

    def setRandomRange(self, low, high):
        self.randLow = low
        self.randHigh = high

    def enableRandom(self, enable=True):
        self.isRandom = enable

    def getRandom(self):
        return self.isRandom
