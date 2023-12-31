import pygame
import sys
import game

# Set up the screen dimensions
screen_width = 1280  
screen_height = 720

# Variables
State = "game"
clock = pygame.time.Clock()
frames = 0

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game.ShapeArea.collidepoint(mouse_x, mouse_y):
                game.Money = game.Money + game.Level

    # Clear the screen
    screen.fill(background_color)  # White background color

    if State == "game":
        game.Game()

    # Update the display
    pygame.display.flip()

    # frames
    fps = clock.get_fps()
    clock.tick(240)
    frames = frames + 1

    #print
    print(frames, fps)