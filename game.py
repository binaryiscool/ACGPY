import pygame
import sys
import math
import colors
import random_varibles
import text
import UI

pygame.init()
pygame.mixer.init()

# Set up the screen dimensions
screen_width = random_varibles.screen_width  
screen_height = random_varibles.screen_height

# Screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Variables
Money = 0
Level = 1
Cost = 50

Scale = (200, 200)
ShapeImageImage = pygame.image.load("Assests/cube.png")
ShapeImage = pygame.transform.scale(ShapeImageImage, Scale)
ShapeRect = ShapeImage.get_rect()
ShapeRect.center = (screen_width // 2, screen_height // 2 - 20)
ShapeArea = pygame.Rect(ShapeRect.topleft, ShapeRect.size)
ubuntu = pygame.font.Font('Assests/fonts/font.ttf', 64)
ubuntuSmall = pygame.font.Font('Assests/fonts/font.ttf', 32)
ubuntuTiny = pygame.font.Font('Assests/fonts/font.ttf', 16)
lol = 0
FrameRateLimit = 240
clock = pygame.time.Clock()
UpImage = pygame.image.load('Assests/up.png')
UpImage = pygame.transform.scale(UpImage, (92,112))
UpRect = UpImage.get_rect()
UpRect.center = (103, screen_height - 60)
UpArea = pygame.Rect(UpRect.topleft, UpRect.size)
CostMultiplier = 1
cube = pygame.image.load("Assests/cube.png")
circle = pygame.image.load("Assests/circle.png")
maroon = pygame.image.load("Assests/maroon.png")
CrunchSFX = "Assests/SFX/Crunch.wav"
Crunch = pygame.mixer.Sound(CrunchSFX)
ShopWidth = 200
ShopHeight = 100 
woweyArea = pygame.Rect(screen_width - ShopWidth, screen_height - ShopHeight, ShopWidth, ShopHeight)

# the spaghetti code is to the max here

# Game Function
def Game():

    # update screen dimensions
    screen_width = random_varibles.screen_width  
    screen_height = random_varibles.screen_height

    clock.tick(FrameRateLimit)
    fps = clock.get_fps()
    elapsed_time = clock.tick(FrameRateLimit) / 1000.0 # i love milliseconds

    # not string to string
    # ^^^ this is pointless now.
    MoneyString = str(Money)
    LevelString = str(Level)

    # Switching Sprites

    if Level == 1:
        ShapeImageImage = cube
    elif Level == 2:
        ShapeImageImage = circle
    elif Level >= 3:
        ShapeImageImage = maroon
    # thought it was => instead of >= lol.
   
    ShapeImage = pygame.transform.scale(ShapeImageImage, Scale)
    ShapeRect = ShapeImage.get_rect()
    ShapeRect.center = (screen_width // 2, screen_height // 2 - 20)
    ShapeArea = pygame.Rect(ShapeRect.topleft, ShapeRect.size)

    # Visuals
    UI.Rect(colors.Secondary, 1065, 0, 15, 1280, 0, 0, 0, 0, "", 0, 0)
    UI.Rect(colors.Secondary, 215, 0, 15, 1280, 0, 0, 0, 0, "", 0, 0)
    UI.Rect(colors.Secondary, 0, screen_height - 150, 215, 15, 0, 0, 0, 0, "", 0, 0)
    UI.Rect(colors.Green, 0, 0, 215, screen_height - 150, 0, 0, 0, 0, "", 0, 0)
    screen.blit(ShapeImage, ShapeRect)
    screen.blit(UpImage, UpRect)
    text.Text(ubuntu, "Money: " + MoneyString, colors.White, screen_width // 2, screen_height // 2 + 150, "center")
    text.Text(ubuntu, "Level: " + LevelString, colors.White, screen_width // 2, screen_height // 2 + 225, "center")
    text.Text(ubuntu, "Cost: " + str(Cost), colors.White, screen_width // 2, screen_height // 2 + 300, "center")
    if random_varibles.devmode == 1:
        text.Text(ubuntuSmall, str(math.floor(fps)), colors.Secondary, 25, 10, "center")
        text.Text(ubuntuTiny, random_varibles.version, colors.Secondary, 87, 30, "center")
    UI.Rect(colors.Primary, screen_width - ShopWidth, screen_height - ShopHeight, ShopWidth, ShopHeight, 1, 30, colors.Secondary, 1, "Shop", colors.Secondary, ubuntu)
    # ^^^ Praiging this works. It does!

    # Other Stuff
    random_varibles.plooper = random_varibles.plooper + 1 #WTF this mean? I forgot what plooper is used for lol. Also it was gonna be where the shape will move up and down but different framerates affected it so, wasn't added.