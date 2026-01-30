import pygame
from car import Car
from Ballon import Ballon
from constantes import dt, BORD1,BORD2,PLAFOND,SOL, alpha
from contact import contact_ballon

class Game:    

    #ballon = pygame.image.load("ballon.png").convert_alpha()
    #car1 = pygame.image.load("car1.png").convert_alpha()
    #car2 = pygame.image.load("car2.png").convert_alpha()
    
    def __init__(self):
        
        self.score = 0
        self.time = 0
        self.car1 = Car(300,300,0,0)
        self.ballon = Ballon(0, 0, 2, 80)


    def raffraichir(self):

        self.ballon.gravity_without_contact(10e-3, 10e-2)
        self.car1.update()
        self.car1.contact_mur()
        contact_ballon(self.car1, self.ballon, 0.5, 15)
        


    def init_affichage(self):
        pygame.init()

        self.SCREEN_WIDTH = 1400
        self.SCREEN_HEIGHT = 900
        pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        background = pygame.image.load("bcakground.png").convert()
        self.background = pygame.transform.scale(background, (self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        img_ballon = pygame.image.load("balle.png")
        self.loaded_car1 = pygame.image.load("voiture.png")

        #Ici changer la scale pour que visuellement ça match

        self.img_ballon = pygame.transform.scale(img_ballon, (self.ballon.r,self.ballon.r))

        

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.screen.blit(background, (0, 0))


        pygame.display.flip()


    def raffraichir_img(self):

        self.raffraichir()

        img_car1 = pygame.transform.scale(self.loaded_car1, (self.car1.x,self.car1.y))
        img_car1_tournee = pygame.transform.rotate(img_car1, self.car1.teta)
        new_rect = img_car1_tournee.get_rect()

        target_y = PLAFOND +SOL - self.car1.y
        new_rect.center = (self.car1.x, target_y)
        
        
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.img_ballon, (self.ballon.x, PLAFOND+SOL- self.ballon.y))
        self.screen.blit(img_car1_tournee, new_rect)

        pygame.display.flip()
        self.clock.tick(30)


