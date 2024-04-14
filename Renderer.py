import pygame

pygame.init()

class Shapes:
    def __init__(self,screen):
        self.screen = screen

    def Rectangle(self,color,x,y,width,height,border,bordercolor,borderthickness):
        left = x - width // 2
        top = y - height // 2
        BordRect = "Not Defined"
        if border:
            BordRect = pygame.Rect(left-borderthickness,top-borderthickness,width + borderthickness * 2,height + borderthickness * 2)
            pygame.draw.rect(self.screen,bordercolor,BordRect)
        Rect = pygame.Rect(left,top,width,height)
        pygame.draw.rect(self.screen,color,Rect)
        if not border:
            return Rect
        else:
            return BordRect