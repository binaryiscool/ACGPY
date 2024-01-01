import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import sys
import game
import random
import math

print("Thank you for playing A Clicker Gaem! :), This project is using: pygame 2.5.2, Python 3.11.2, and cx_Freeze 16.15.12!")

# Welcome Message

# Set up the screen dimensions
screen_width = 1280  
screen_height = 720

# Variables
State = "game"
clock = pygame.time.Clock()
frames = 0
devmode = 0
ShapeScale = 200
Grow = 0
FrameRateLimit = 555
ploopy = 70

# Initialize Pygame
pygame.init()

# Set background colour
background_color = (85, 124, 217)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ACG")

# Load the icon image
icon = pygame.image.load("Assests/icon.png")

# Set the icon
pygame.display.set_icon(icon)

# Main game loop
while True:

    # Get the mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if State == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and game.ShapeArea.collidepoint(mouse_x, mouse_y):
                    game.Money = game.Money + game.Level
                    ShapeScale = 150
                    Grow = 1
                if event.button == 1 and game.UpArea.collidepoint(mouse_x, mouse_y):
                    if game.Money >= game.Cost:
                        game.Money = game.Money - game.Cost
                        game.Level = game.Level + 1
                        game.Cost =  math.floor((game.Cost + 50) * game.CostMultiplier)
                        game.CostMultiplier = game.CostMultiplier + 0.35
        
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_b:
                if devmode == 1:
                    devmode = 0
                else:
                    devmode = 1
            if event.key == pygame.K_SPACE:
                    game.Money = game.Money + game.Level
                    ShapeScale = 150
                    Grow = 1

    # Clear the screen
    screen.fill(background_color)  # White background color

    if State == "game":
        game.Game()

    # Update the display
    pygame.display.flip()

    # Frames
    fps = clock.get_fps()
    clock.tick(FrameRateLimit)
    elapsed_time = clock.tick(FrameRateLimit) / 1000.0
    frames = frames + 1

    # Print
    if devmode == 1:
        print("current frame: " + str(frames), "fps: " + str(fps), "state: " + str(State))
    
    # Change size
    if Grow == 1:
        game.Scale = (ShapeScale, ShapeScale)
        ShapeScale *=  ploopy ** elapsed_time
        ploopy = ploopy + (ploopy/20    )
        if ShapeScale > 200:
            Grow = 0
            ShapeScale = 200
            ploopy = 70