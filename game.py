class Game:
    background = pygame.image.load("background.jpg").convert()
    background = pygame.transform.scale(background, (800, 600))

    ballon = pygame.image.load("ballon.png").convert_alpha()
    car1 = pygame.image.load("car1.png").convert_alpha()
    car2 = pygame.image.load("car2.png").convert_alpha()
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.screen.blit(background, (0, 0))
        self.screen.blit(ballon, (400, 300))
        self.screen.blit(car1, (0, 0))
        self.screen.blit(car2, (800, 0))
        pygame.display.flip()



    quitter_jeu = False
    while not quitter_jeu:
        screen.blit(background, (0, 0))


        screen.fill((30, 30, 30))
        screen.blit(ballon, (x_ballon, z_ballon))
        screen.blit(car, (x_car, y_car))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


