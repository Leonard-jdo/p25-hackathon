def input():

    accelerated = False
    descelerated = False
    jump = False
    boost = False

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            quitter_jeu = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
            if event.key == pygame.K_RIGHT:
                accelerated = True
            if event.key == pygame.K_LEFT:
                descelerated = True
            if event.key == pygame.K_b:
                boost = True
                
            param = [accelerated, descelerated, jump, boost, quitter_jeu]

    return(param)
