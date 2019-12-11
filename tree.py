from constants import *

class TreeChunk:

    def __init__(self, lenght, width, startPoint, iterable, angle, level):
        self.lenght = lenght
        self.width = width
        self.startPoint = startPoint
        self.iterable = iterable
        self.angle = angle
        self.level = level
        self.endPoint = [startPoint[0]+self.lenght*math.sin(self.angle), startPoint[1]-lenght*math.cos(self.angle)]
        if self.level==0:
            self.endPoint = [startPoint[0], startPoint[1] - lenght]

    def draw(self):
        pygame.draw.line(DISPLAY, BLUE, self.startPoint, self.endPoint, int(self.width))

    def replicate(self):
        self.iterable = 0
        arrayOfTreeChunks.append(TreeChunk(self.lenght/2, self.width*5/7, [self.endPoint[0], self.endPoint[1]], 1, self.angle, self.level+1))
        arrayOfTreeChunks.append(TreeChunk(self.lenght/2, self.width*5/7, [self.endPoint[0], self.endPoint[1]], 1, -self.angle, self.level+1))

arrayOfTreeChunks = []

arrayOfTreeChunks.append(TreeChunk(BASE_HEIGHT/2, BASE_WIDTH / 20, [BASE_WIDTH / 2, BASE_HEIGHT], 1, math.pi/180*30, 0))

arrayOfTreeChunks[0].replicate()

for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfTreeChunks)):
        if arrayOfTreeChunks[p].iterable:
            arrayOfTreeChunks[p].replicate()

    for p in range(len(arrayOfTreeChunks)):
        arrayOfTreeChunks[p].draw()