import sys
import pygame
import UI
import colors
import random_varibles
import text

baseWidth = 1080
baseheight = 540
centerX = random_varibles.screen_width // 2
centerY = random_varibles.screen_height // 2
baseX = centerX - (baseWidth / 2)
baseY = centerY - (baseheight / 2)

pygame.init()

def Shop():
    # used for testing
    # pygame.quit
    # sys.exit()

    UI.Rect(colors.Primary, baseX, baseY, baseWidth, baseheight, 1, 30, colors.Secondary, 0, "", 0, 0)
    text.Text(random_varibles.ubuntu, "Shop", colors.Secondary, 107, 90, "topleft")
