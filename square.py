# Import nutných konstant
from constants import *

# Objekt části fraktálu
class SquareFractal:

    # Iniciační funkce s parametry pro tvorbu čtverce - pozice odkud se má tvořit,
    # parametry a jestli je objekt replikovatelný (iterovatelný)
    def __init__(self, size, startPoint, iterable):
        self.size = size
        self.startPoint = startPoint
        self.iterable = iterable

    # Zobrazovaní částí pomocí parametrů
    def draw(self):
        pygame.draw.rect(DISPLAY, BLUE,
                         (self.startPoint[0], self.startPoint[1], self.size, self.size))
        pygame.draw.rect(DISPLAY, WHITE, (
            self.startPoint[0] + self.size / 3, self.startPoint[1] + self.size / 3, self.size / 3, self.size / 3))

    # Replikační funkce pro tvorbu nových podčástí
    def replicate(self):
        self.iterable = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if {i, j} != {1, 1}:
                    arrayOfSquareFractals.append(SquareFractal(self.size / 3, [self.startPoint[0] + i * self.size / 3,
                                                                               self.startPoint[1] + j * self.size / 3],
                                                               1))


# Tvorba pole a přidání první části fraktálu
arrayOfSquareFractals = []
arrayOfSquareFractals.append(SquareFractal(BASE_WIDTH, [0, 0], 1))

# Replikační cyklus pro rekurzivní tvorbu fraktálu
for k in range(RECURSION_DEPTH):
    for p in range(len(arrayOfSquareFractals)):
        if arrayOfSquareFractals[p].iterable:
            arrayOfSquareFractals[p].replicate()

    for p in range(len(arrayOfSquareFractals)):
        arrayOfSquareFractals[p].draw()
