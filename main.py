import pygame
from Game import Main
import colors

#FOR SELF: whenever loading images, convert.

pygame.init()

#SetUp
screenWidth = 1280
screenHeight = 800
screenSize = (screenWidth,screenHeight)
screen = pygame.display.set_mode(screenSize)
ver = "Alpha V0.1"
running = True
state = "Game"
fps = 0
clock = pygame.time.Clock()
DisplayedGame = Main(screen,screenWidth,screenHeight,clock)
ClickToFunc = {
    "Game": DisplayedGame.Click
}

#Display options that aren't flags
pygame.display.set_caption("A Clicker Gaem. Version: " + ver + ". FPS: " + str(fps))

pygame.display.flip

#Loop of the Gaems
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            ClickToFunc[state]()

    clock.tick(240)

    screen.fill(colors.Primary)

    fps = clock.get_fps()
    pygame.display.set_caption("A Clicker Gaem. Version: " + ver + ". FPS: " + str(fps))

    if state == "Game":   
        DisplayedGame.Tick()

    pygame.display.update()

    