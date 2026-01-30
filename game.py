import pygame
from car import Car
from Ballon import Ballon
dt = 0.05
BORD1, BORD2 = 75, 1320
PLAFOND = 90
SOL = 690


class Game:    

    #ballon = pygame.image.load("ballon.png").convert_alpha()
    #car1 = pygame.image.load("car1.png").convert_alpha()
    #car2 = pygame.image.load("car2.png").convert_alpha()
    
    def __init__(self):
        
        self.score = 0
        self.time = 0
        self.car1 = Car(300,300,0,0)
        self.ballon = Ballon(700, 500, 0, 0, 2, 80)

        


    def init_affichage(self):
        pygame.init()

        self.SCREEN_WIDTH = 1400
        self.SCREEN_HEIGHT = 900
        pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        background = pygame.image.load("bcakground.png").convert()
        self.background = pygame.transform.scale(background, (self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        img_ballon = pygame.image.load("balle.png")

        #Ici changer la scale pour que visuellement ça match

        self.img_ballon = pygame.transform.scale(img_ballon, (self.ballon.r,self.ballon.r))

        img_car1 = pygame.image.load("voiture.png")
        self.img_car1 = pygame.transform.scale(img_car1, (self.car1.x,self.car1.y))


        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.blit(background, (0, 0))


        pygame.display.flip()


    def raffraichir(self):

        
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.img_ballon, (self.ballon.x, self.ballon.y))

        pygame.display.flip()
        self.clock.tick(30)


