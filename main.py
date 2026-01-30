from game import Game
import pygame

game = Game()
game.init_affichage()

i = 0
while i < 200:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    game.raffraichir()
    i +=1 
        
    # Une fois la boucle terminée, on quitte proprement pygame
pygame.quit()