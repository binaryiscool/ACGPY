import pygame

# init
pygame.init()

# Set up the screen dimensions
screen_width = 1280  
screen_height = 720

# Screen
screen = pygame.display.set_mode((screen_width, screen_height))

# func
def Text(font, text: str, color, x: int, y: int, centered: str):
    Rendertext = font.render(text, True, color)
    RendertextRect = Rendertext.get_rect()
    if centered == "center" or centered == None:
        RendertextRect.center = (x,y)
    elif centered == "topleft":
        RendertextRect.topleft = (x,y)

    screen.blit(Rendertext, RendertextRect)