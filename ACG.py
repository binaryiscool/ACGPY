import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import sys
import game
import random
import math
import os
import colors
import text
import UI
import random_varibles
import shop
import time

# Welcome Message
print("Thank you for playing A Clicker Gaem! :), This project is using: pygame 2.5.2, Python 3.11.2, and cx_Freeze 16.15.12!")

# Set up the screen dimensions
screen_width = random_varibles.screen_width  
screen_height = random_varibles.screen_height

# Variables
State = "game"
wait = pygame.time.Clock()
frames = 0
ShapeScale = 200
Grow = 0
FrameRateLimit = 240
ploopy = 70
ubuntu = pygame.font.Font('Assests/fonts/font.ttf', 64)
fullscreen = 0

# Initialize Pygame and other stuff
pygame.init()
pygame.mixer.init()

# Music
pygame.mixer.music.set_volume(0.75)
music_directory = "Assests\Music"
music_files = [file for file in os.listdir(music_directory) if file.endswith(".ogg")]
ploop = random.randrange(1,5)
current_song = os.path.join(music_directory, music_files[ploop])
pygame.mixer.music.load(current_song)
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)
print("currently playing: " + str(current_song))

# Set background colour
background_color = colors.Primary

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ACG")

# Load the icon image
icon = pygame.image.load("Assests/icon.png")

# Set the icon
pygame.display.set_icon(icon)

def Click():
    game.Money = game.Money + game.Level
    game.Crunch.play()

def Upgrade():
    if game.Money >= game.Cost:
        game.Money = game.Money - game.Cost
        game.Level = game.Level + 1
        game.Cost =  math.floor((game.Cost + 50) * game.CostMultiplier)
        game.CostMultiplier = game.CostMultiplier + 0.35

def waitSeconds(waitTime):
    start_time = time.time()
    while time.time() - start_time < waitTime:
        pass

# Main game loop
while True:
    
    # update screen dimensions
    screen_width = random_varibles.screen_width  
    screen_height = random_varibles.screen_height

    # Clear the screen
    screen.fill(background_color)  # Background color

    # Get the mouse coordinates
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if State == "game":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if State == "game":
                    # Shape
                    if event.button == 1 and game.ShapeArea.collidepoint(mouse_x, mouse_y):
                        Click()
                        ShapeScale = 150
                        Grow = 1
                    # Level UP
                    if event.button == 1 and game.UpArea.collidepoint(mouse_x, mouse_y):
                        Upgrade()
                    # Shop
                    if event.button == 1 and game.woweyArea.collidepoint(mouse_x, mouse_y):
                        if random_varibles.Shop == 0:
                            random_varibles.Shop = 1
                        else:
                            random_varibles.Shop = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                pygame.display.toggle_fullscreen()
            if  event.key == pygame.K_b:
                if random_varibles.devmode == 1:
                    random_varibles.devmode = 0
                else:
                    random_varibles.devmode = 1
            if State == "game":
                if event.key == pygame.K_SPACE:
                        Click()
                        ShapeScale = 150
                        Grow = 1
                if event.key == pygame.K_UP:
                        Upgrade()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.USEREVENT:
            # Do Music Again
            ploop = (ploop + random.randrange(1,5)) % len(music_files)
            current_song = os.path.join(music_directory, music_files[ploop])
            pygame.mixer.music.load(current_song)
            pygame.mixer.music.play()
            print("currently playing: " + str(current_song))

    if State == "game":
        game.Game()
        if random_varibles.Shop == 1:
            shop.Shop()

    # Update the display
    pygame.display.flip()


    # Frames
    fps = wait.get_fps()
    wait.tick(FrameRateLimit)
    elapsed_time = wait.tick(FrameRateLimit) / 1000.0
    frames = frames + 1

    # Print
    if random_varibles.devmode == 1:
        print("current frame: " + str(frames), "fps: " + str(fps), "state: " + str(State))
        print(mouse_x, mouse_y)
        game.Money = 100000000 + game.Money
    
    # Change size
    if Grow == 1:
        game.Scale = (ShapeScale, ShapeScale)
        ShapeScale *=  ploopy ** elapsed_time
        ploopy = ploopy + (ploopy/20)
        if ShapeScale > 200:
            Grow = 0
            ShapeScale = 200
            ploopy = 70