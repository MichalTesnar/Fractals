from constants import *

def main():
    pygame.init()

    DISPLAY.fill(WHITE)

    # import square

    # import snowflake

    import tree

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
main()