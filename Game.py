import pygame
from Renderer import Shapes
import config

pygame.init()

class Main:
    def __init__(self,screen,screenWidth,screenHeight,clock):
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.money = 0
        self.level = 1
        self.scale_factor = 1
        self.scale_tick = 0
        self.shrink = False
        self.setupped = False
        self.clock = clock
        self.tickSpeed = 0
    
    def Tick(self):
        self.fps = self.clock.get_fps()
        if not self.fps == 0:
            self.tickSpeed = 45 / self.fps
        drawer = Shapes(self.screen)
        self.options = config.load_options('options.cfg','Game')
        self.ToggleScale()
        self.square_rect = drawer.Rectangle((0,0,0),self.screenWidth - (200 + self.screenWidth//1.5) ,self.screenHeight//2,200 * self.scale_factor,200 * self.scale_factor,True,(255,255,255),10)
        if not self.setupped:
            self.setupped = True

    def ToggleScale(self):
        if self.shrink:
            self.scale_factor += 0.1 * self.tickSpeed
            
        if self.scale_factor <= 0.5:
             self.shrink = True
        elif self.scale_factor >= 1.0:
            self.shrink = False
    
    def Click(self):
        if self.setupped:
            #print(self.options["scale"])
            mouse_pos = pygame.mouse.get_pos()
            if self.square_rect.collidepoint(mouse_pos):
                self.money += self.level
                if self.options["scale"] == "True":
                    self.scale_factor = 0.5
                print([self.money, self.level])

