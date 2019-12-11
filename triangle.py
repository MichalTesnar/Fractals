from constants import *

class TriangleFractal:

    def __init__(self, size, startPoint, iterable):
        self.size = size
        self.startPoint = startPoint
        self.iterable = iterable

    def draw(self):
        pygame.draw.polygon(DISPLAY, BLUE, ([self.startPoint[0], self.startPoint[1]],
                                            [self.startPoint[0] + self.size, self.startPoint[1]],
                                            [self.startPoint[0] + self.size / 2,
                                            self.startPoint[1] - math.sqrt(3) / 2 * self.size]), 0)
        pygame.draw.polygon(DISPLAY, WHITE, ([self.startPoint[0] + self.size/2, self.startPoint[1]],
                                             [self.startPoint[0] + self.size/4, self.startPoint[1]- math.sqrt(3) /2/2 * self.size],
                                             [self.startPoint[0] + self.size/4*3, self.startPoint[1]- math.sqrt(3) /2/2 * self.size]),0)

    def replicate(self):
        self.iterable = 0
        arrayOfTriangleFractals.append(TriangleFractal(self.size/2, [self.startPoint[0], self.startPoint[1]], 1))
        arrayOfTriangleFractals.append(TriangleFractal(self.size/2, [self.startPoint[0]+self.size/2, self.startPoint[1]], 1))
        arrayOfTriangleFractals.append(TriangleFractal(self.size / 2, [self.startPoint[0] + self.size / 4, self.startPoint[1]- math.sqrt(3) /2/2 * self.size], 1))

arrayOfTriangleFractals = []

arrayOfTriangleFractals.append(TriangleFractal(BASE_WIDTH, [0, BASE_HEIGHT], 1))

for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfTriangleFractals)):
        if arrayOfTriangleFractals[p].iterable:
            arrayOfTriangleFractals[p].replicate()

    for p in range(len(arrayOfTriangleFractals)):
        arrayOfTriangleFractals[p].draw()