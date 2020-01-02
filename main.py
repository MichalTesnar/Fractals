# Importování konstant z constants.py
from constants import *


# Hlavní funkce pro spuštění dalších skriptů pro tvorbu fraktálů
def main():
    # Iniciace prostředí knihovny Pygame
    pygame.init()
    DISPLAY.fill(WHITE)

    # Výběr skriptu, který chceme pustit a jeho spuštění
    print("Který fraktál byste rád?" "\n"
          "1: Čtverec;" "\n"
          "2: Strom;" "\n"
          "3: Trojúhelník;" "\n"
          "4: Vločka;" "\n"
          "5: Kantorovo diskontiuum;")
    import snowflake
    '''
    choice = int(input())
    print(choice)

    
    if choice == 1:
        import square
    if choice == 2:
        import tree
    if choice == 3:
        import triangle
    if choice == 4:
        import snowflake
    if choice == 5:
        import CantorLine
    '''

    # Životní cyklus knihovny Pygame s vytvořením screenshotu právě zobrazeného snímku
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.image.save(DISPLAY, "screenshot.jpg")
                pygame.quit()
                sys.exit()
        pygame.display.update()

# Spuštění vlastního souboru
if __name__ == "__main__":
    main()
