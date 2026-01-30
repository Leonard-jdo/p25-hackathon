import pygame

background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (800, 600))

ballon = pygame.image.load("ballon.png").convert_alpha()
car = pygame.image.load("car.png").convert_alpha()


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

quitter_jeu = False
while not quitter_jeu:
    screen.blit(background, (0, 0))


    screen.fill((30, 30, 30))
    screen.blit(ballon, (x_ballon, z_ballon))
    screen.blit(car, (x_car, y_car))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
