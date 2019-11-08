from constants import *

class TreeChunk:

    def __init__(self, lenght, width, startPoint, iterable, angle, level):
        self.lenght = lenght
        self.width = width
        self.startPoint = startPoint
        self.iterable = iterable
        self.angle = angle
        self.endPoint = [startPoint[0]+self.angle, startPoint[1]-lenght]
        self.level= level
        if self.level==1:
            self.endPoint = [startPoint[0], startPoint[1] - lenght]

    def draw(self):
        pygame.draw.line(DISPLAY, BLUE, self.startPoint, self.endPoint, int(self.width))

    def replicate(self):
        arrayOfTreeChunks.append(TreeChunk(self.lenght/2, self.width*4/7, [self.endPoint[0], self.endPoint[1]], 1, self.angle, self.level+1))
        arrayOfTreeChunks.append(TreeChunk(self.lenght / 2, self.width*4/7, [self.endPoint[0], self.endPoint[1]], 1, -self.angle, self.level+1))

arrayOfTreeChunks = []

arrayOfTreeChunks.append(TreeChunk(BASE_HEIGHT/2, BASE_WIDTH / 10, [BASE_WIDTH / 2, BASE_HEIGHT], 1, 50, 1))

arrayOfTreeChunks[0].replicate()

for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfTreeChunks)):
        if arrayOfTreeChunks[p].iterable:
            arrayOfTreeChunks[p].replicate()

    for p in range(len(arrayOfTreeChunks)):
        arrayOfTreeChunks[p].draw()