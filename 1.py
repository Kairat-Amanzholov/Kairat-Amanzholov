import pygame

window = pygame.display.set_mode([800,640])


while 1:
    for f in pygame.event.get():
        if f.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.fill((155,155,155))
    pygame.draw.circle(window, (230,50,230), (400,320),10)
    pygame.display.update()
