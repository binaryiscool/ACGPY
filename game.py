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
ShapeImage = pygame.image.load("Assests/cube.png")
ShapeRect = ShapeImage.get_rect()
ShapeRect.center = (screen_width // 2, screen_height // 2)
ShapeArea = pygame.Rect(ShapeRect.topleft, ShapeRect.size)
oswald = "Assests/font.ttf"
oswald = pygame.font.Font('Assests/font.ttf', 32)

# Function
def Game():
    # not string to string
    MoneyString = str(Money)
    LevelString = str(Level)

    # Setup text
    MoneyText = oswald.render("Money: " + MoneyString, True, (255,255,255))
    MoneyTextRect = MoneyText.get_rect()
    MoneyTextRect.center = (screen_width // 2,  screen_height // 2 + 80) 

    LevelText = oswald.render("Level: " + LevelString, True, (255,255,255))
    LevelTextRect = LevelText.get_rect()
    LevelTextRect.center = (screen_width // 2,  screen_height // 2 + 120)  

    # Visuals
    screen.blit(ShapeImage, ShapeRect)
    screen.blit(MoneyText, MoneyTextRect)
    screen.blit(LevelText, LevelTextRect)