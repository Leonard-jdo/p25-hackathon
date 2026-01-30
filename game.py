import pygame
from car import Car
from Ballon import Ballon
from constantes import dt, BORD1,BORD2,PLAFOND,SOL, alpha,g
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
        self.goal_width = 100
        self.goal_height = 300
        
        # Calcul de la position verticale (centrée)
        self.goal_y_math = (SOL + PLAFOND) / 2 # Centre mathématique
        
        # Création des Rect (en coordonnées Pygame)
        # But Gauche
        self.rect_but_gauche = pygame.Rect(0, 300, self.goal_width, self.goal_height)
        # But Droit
        self.rect_but_droit = pygame.Rect(self.SCREEN_WIDTH - self.goal_width, 300, self.goal_width, self.goal_height)


    def raffraichir(self):

        self.ballon.gravity_without_contact(alpha, g)
        self.car1.update()
        self.car1.contact_mur()
        contact_ballon(self.car1, self.ballon, 0.5, 15)
        print(self.car1.x, self.car1.y,)
        resultat = self.ballon.corr_contact()
        if resultat == "GOAL_LEFT":
            self.score_orange += 1 # e
            self.message_but = "BUT À GAUCHE !"
            self.couleur_but = (255, 165, 0) 
            self.affichage_but_timer = 60    
            self.ballon.reset_position()    

        elif resultat == "GOAL_RIGHT":
            self.score_bleu += 1
            self.message_but = "BUT À DROITE !"
            self.couleur_but = (0, 0, 255)   # Bleu
            self.affichage_but_timer = 60
            self.ballon.reset_position()
        


    def init_affichage(self): 
            pygame.font.init()
            self.police_but = pygame.font.SysFont("Arial", 100, bold=True)
            
            # Variables pour l'animation du but
            self.affichage_but_timer = 0
            self.message_but = ""
            self.couleur_but = (0, 0, 0)
            pygame.init()
            self.SCREEN_WIDTH = 1400
            self.SCREEN_HEIGHT = 900
            # On crée la fenêtre UNE SEULE FOIS
            self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            
            # Chargement et optimisation (convert_alpha pour la balle et voiture)
            background = pygame.image.load("bcakground.png").convert()
            self.background = pygame.transform.scale(background, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
            
            img_ballon = pygame.image.load("balle.png").convert_alpha()
            # On scale au DIAMÈTRE (2 * r)
            self.img_ballon = pygame.transform.scale(img_ballon, (self.ballon.r * 2, self.ballon.r * 2))
            
            self.loaded_car1 = pygame.image.load("voiture.png").convert_alpha()
            self.clock = pygame.time.Clock()
            
        


    def raffraichir_img(self):
        self.raffraichir() # Ta physique

        # 1. Gestion Voiture
        img_car1 = pygame.transform.scale(self.loaded_car1, (100, 50))
        img_car1_tournee = pygame.transform.rotate(img_car1, self.car1.teta)
        new_rect = img_car1_tournee.get_rect()

        target_y = PLAFOND +SOL - self.car1.y
        new_rect.center = (self.car1.x, target_y)
        
        # 2. Gestion Balle 
        ball_rect = self.img_ballon.get_rect()
        ball_target_y = (SOL + PLAFOND) - self.ballon.y
        ball_rect.center = (self.ballon.x, ball_target_y)

        # 3. Dessin
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.img_ballon, (self.ballon.x, PLAFOND+SOL- self.ballon.y))
        self.screen.blit(img_car1_tournee, new_rect)

        #BUT
        if self.affichage_but_timer > 0:
            # Création de la surface du texte
            texte_surface = self.police_but.render(self.message_but, True, self.couleur_but)
            texte_rect = texte_surface.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
            
            # Petit effet de contour blanc pour que ce soit lisible sur n'importe quel fond
            pygame.draw.rect(self.screen, (255, 255, 255), texte_rect.inflate(20, 20))
            self.screen.blit(texte_surface, texte_rect)
            
            # On décompte le timer
            self.affichage_but_timer -= 1

        pygame.display.flip()
        self.clock.tick(60) 

    



