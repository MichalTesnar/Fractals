from constants import *


class LinePeace:

    def __init__(self, size, startPoint, iterable):
        self.size = size
        self.startPoint = startPoint
        self.iterable = iterable

    def draw(self):
        pygame.draw.line(DISPLAY, BLUE, (self.startPoint[0], self.startPoint[1]),
                         (self.startPoint[0] + self.size, self.startPoint[1]), 3)

    def replicate(self):
        self.iterable = 0
        arrayOfLinePeaces.append(LinePeace(self.size / 3, [self.startPoint[0], self.startPoint[1] + 10], 1))
        arrayOfLinePeaces.append(
            LinePeace(self.size / 3, [self.startPoint[0] + self.size * 2 / 3, self.startPoint[1] + 10], 1))


arrayOfLinePeaces = []

arrayOfLinePeaces.append(LinePeace(BASE_WIDTH, [0, 0], 1))

for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfLinePeaces)):
        if arrayOfLinePeaces[p].iterable:
            arrayOfLinePeaces[p].replicate()

    for p in range(len(arrayOfLinePeaces)):
        arrayOfLinePeaces[p].draw()
