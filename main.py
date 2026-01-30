from game import Game
import pygame

game = Game()
game.init_affichage()

i = 0
while i < 10000:
    game.raffraichir_img()
    i +=1 
        
    # Une fois la boucle terminée, on quitte proprement pygame
pygame.quit()