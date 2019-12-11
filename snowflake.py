from constants import *


class Snowflake:

    def __init__(self, size, startPoint, endPoint, iterable, isLeft):
        self.size = size
        self.isLeft = isLeft
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.iterable = iterable
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0
        self.pointOfTriangleX = 0
        self.pointOfTriangleY = 0

        if self.startPoint[0] >= self.endPoint[0]:
            self.lowerPointX = self.startPoint[0]
            self.highPointX = self.endPoint[0]
        else:
            self.lowerPointX = self.endPoint[0]
            self.highPointX = self.startPoint[0]

        if self.startPoint[1] >= self.endPoint[1]:
            self.lowerPointY = self.startPoint[1]
            self.highPointY = self.endPoint[1]
        else:
            self.lowerPointY = self.endPoint[1]
            self.highPointY = self.startPoint[1]

        if self.startPoint[1] < self.endPoint[1]:
            self.x1 = self.lowerPointX + (self.highPointX - self.lowerPointX) / 3
            self.y1 = self.lowerPointY + (self.highPointY - self.lowerPointY) / 3
            self.x2 = self.lowerPointX + (self.highPointX - self.lowerPointX) * 2 / 3
            self.y2 = self.lowerPointY + (self.highPointY - self.lowerPointY) * 2 / 3
            self.pointOfTriangleX = (self.x1 + self.x2 + math.sqrt(3) * (self.y1 - self.y2)) / 2
            self.pointOfTriangleY = (self.y1 + self.y2 - math.sqrt(3) * (self.x1 - self.x2)) / 2

        else:
            self.x1 = self.lowerPointX + (self.highPointX - self.lowerPointX) / 3
            self.y1 = self.lowerPointY + (self.highPointY - self.lowerPointY) * 2 / 3
            self.x2 = self.lowerPointX + (self.highPointX - self.lowerPointX) * 2 / 3
            self.y2 = self.lowerPointY + (self.highPointY - self.lowerPointY) / 3
            self.pointOfTriangleX = (self.x1 + self.x2 - math.sqrt(3) * (self.y1 - self.y2)) / 2
            self.pointOfTriangleY = (self.y1 + self.y2 + math.sqrt(3) * (self.x1 - self.x2)) / 2

    def draw(self):
        pygame.draw.line(DISPLAY, BLUE, [self.startPoint[0], self.startPoint[1]], [self.endPoint[0], self.endPoint[1]],
                         self.size)
        pygame.draw.line(DISPLAY, WHITE, [self.x1, self.y1], [self.x2, self.y2], self.size + 3)
        self.pointOfTriangle = [self.pointOfTriangleX, self.pointOfTriangleY]
        pygame.draw.line(DISPLAY, BLUE, [self.x1, self.y1], self.pointOfTriangle, self.size)
        pygame.draw.line(DISPLAY, BLUE, [self.x2, self.y2], self.pointOfTriangle, self.size)

        self.pointOfTriangle = [BASE_WIDTH-self.pointOfTriangleX, self.pointOfTriangleY]
        pygame.draw.line(DISPLAY, BLUE, [BASE_WIDTH-self.startPoint[0], self.startPoint[1]],
                         [BASE_WIDTH-self.endPoint[0], self.endPoint[1]],self.size)
        pygame.draw.line(DISPLAY, WHITE, [BASE_WIDTH-self.x1, self.y1], [BASE_WIDTH-self.x2, self.y2], self.size + 3)
        pygame.draw.line(DISPLAY, BLUE, [BASE_WIDTH-self.x1, self.y1], self.pointOfTriangle, self.size)
        pygame.draw.line(DISPLAY, BLUE, [BASE_WIDTH-self.x2, self.y2], self.pointOfTriangle, self.size)

    def replicate(self):
        self.iterable = 0

        arrayOfSnowflakes.append(Snowflake(self.size, self.startPoint, [self.x2, self.y2], 1,0))
        arrayOfSnowflakes.append(Snowflake(self.size, [self.x1, self.y1], self.endPoint, 1,0))

        #arrayOfSnowflakes.append(Snowflake(self.size, [self.pointOfTriangleX, self.pointOfTriangleY],[self.x2, self.y2], 1,0))
        '''
        if self.x1 < self.pointOfTriangleX:
            arrayOfSnowflakes.append(Snowflake(self.size, [self.x1, self.y1], [self.pointOfTriangleX, self.pointOfTriangleY], 1,0))
        else:
            arrayOfSnowflakes.append(Snowflake(self.size, [self.pointOfTriangleX, self.pointOfTriangleY], [self.x1, self.y1], 1,0))
        '''

arrayOfSnowflakes = []

arrayOfSnowflakes.append(Snowflake(3, [0, BASE_HEIGHT/2], [BASE_WIDTH, BASE_WIDTH/2], 1, 0))

for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfSnowflakes)):
        if arrayOfSnowflakes[p].iterable:
            arrayOfSnowflakes[p].replicate()

    for p in range(len(arrayOfSnowflakes)):
        arrayOfSnowflakes[p].draw()
