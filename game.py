import pygame
#from car import Car
from Ballon import Ballon
dt = 0.05
class Game:    

    #ballon = pygame.image.load("ballon.png").convert_alpha()
    #car1 = pygame.image.load("car1.png").convert_alpha()
    #car2 = pygame.image.load("car2.png").convert_alpha()
    
    def __init__(self):
        
        self.score = 0
        self.time = 0
        #self.car1 = Car(0,0,0,0)
        self.ballon = Ballon(100, 100, 0, 0, 2, 10)


    def init_affichage(self):
        pygame.init()
        pygame.display.set_mode((1400, 1800))
        background = pygame.image.load("bcakground.png").convert()
        self.background = pygame.transform.scale(background, (1400, 1800))
        self.img_ballon = pygame.image.load("balle.png")

        self.screen = pygame.display.set_mode((1400, 1800))
        self.clock = pygame.time.Clock()
        self.screen.blit(background, (0, 0))


        pygame.display.flip()


    def raffraichir(self):
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.img_ballon, (self.ballon.x, self.ballon.y))

        pygame.display.flip()
        self.clock.tick(30)


