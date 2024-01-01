import pygame
import sys
import math

pygame.init()

# Set up the screen dimensions
screen_width = 1280  
screen_height = 720

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
oswald = pygame.font.Font('Assests/font.ttf', 64)
lol = 0
FrameRateLimit = 555
clock = pygame.time.Clock()
UpImage = pygame.image.load('Assests/up.png')
UpImage = pygame.transform.scale(UpImage, (92,112))
UpRect = UpImage.get_rect()
UpRect.center = (50, screen_height - 60)
UpArea = pygame.Rect(UpRect.topleft, UpRect.size)
CostMultiplier = 1
cube = pygame.image.load("Assests/cube.png")
circle = pygame.image.load("Assests/circle.png")

# Game Function
def Game():

    elapsed_time = clock.tick(FrameRateLimit) / 1000.0

    # not string to string
    MoneyString = str(Money)
    LevelString = str(Level)

    # Setup Visuals
    MoneyText = oswald.render("Money: " + MoneyString, True, (255,255,255))
    MoneyTextRect = MoneyText.get_rect()
    MoneyTextRect.center = (screen_width // 2,  screen_height // 2 + 150) 

    LevelText = oswald.render("Level: " + LevelString, True, (255,255,255))
    LevelTextRect = LevelText.get_rect()
    LevelTextRect.center = (screen_width // 2,  screen_height // 2 + 225)  

    CostText = oswald.render("Cost: " + str(Cost), True, (255,255,255))
    CostTextRect = CostText.get_rect()
    CostTextRect.center = (screen_width // 2,  screen_height // 2 + 300)  

    if Level == 1:
        ShapeImageImage = cube
    elif Level == 2:
        ShapeImageImage = circle
    else:
        ShapeImageImage = circle
    
    ShapeImage = pygame.transform.scale(ShapeImageImage, Scale)
    ShapeRect = ShapeImage.get_rect()
    ShapeRect.center = (screen_width // 2, screen_height // 2 - 20)
    ShapeArea = pygame.Rect(ShapeRect.topleft, ShapeRect.size)

    # Visuals
    screen.blit(ShapeImage, ShapeRect)
    screen.blit(UpImage, UpRect)
    screen.blit(MoneyText, MoneyTextRect)
    screen.blit(LevelText, LevelTextRect)
    screen.blit(CostText, CostTextRect)