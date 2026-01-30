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


    def raffraichir(self, x_ballon, z_ballon, x_car1, z_car1, x_car2, z_car2):
        
        self.screen.blit(background, (0, 0))
        self.screen.blit(ballon, (x_ballon, z_ballon))
        self.screen.blit(car, (x_car1, z_car1))
        self.screen.blit(car, (x_car2, z_car2))
        pygame.display.flip()
        clock.tick(60)






