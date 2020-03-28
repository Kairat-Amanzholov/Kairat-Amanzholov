import pygame

window = pygame.display.set_mode([800,640])


while 1:
    for f in pygame.event.get():
        if f.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.fill((155,155,155))
    pygame.draw.polygon(window, (230,50,230), [[70,30],[80,60],[100,10],[120,60],[130,30]]
    pygame.display.update()
