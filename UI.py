import pygame
import text

# Eat. Sleep. Click. Repeat.
pygame.init()

# Set up the screen dimensions
screen_width = 1280  
screen_height = 720

# Screen
screen = pygame.display.set_mode((screen_width, screen_height))

# made it work well with all sizes :)

def Rect(color, x, y, sizeW, sizeH, Border: int, BordersizeOffset, BorderColor, DrawText: int, Text: str, TextColor, TextFont):
    if Border == 1:
        pygame.draw.rect(screen, BorderColor, (x - BordersizeOffset / 2, y - BordersizeOffset / 2, sizeW + BordersizeOffset, sizeH + BordersizeOffset))
    pygame.draw.rect(screen, color, (x, y, sizeW, sizeH))
    if DrawText == 1:
        text.Text(TextFont, Text, TextColor, x + sizeW/2, y + sizeH/2, "center")