# Import nutných knihoven
import pygame, sys, math

# Konstanty pro vznik zobrazovacího okna a konstanta samotné obrazovky
BASE_WIDTH = 1000
BASE_HEIGHT = 1000
DISPLAY = pygame.display.set_mode((BASE_WIDTH, BASE_HEIGHT), 0, 32)

# Barvy
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Hloubka rekurze fraktálu
RECURSION_DEPTH = 2

