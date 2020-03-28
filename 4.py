import pygame

window = pygame.display.set_mode([640,640])


while 1:
    for f in pygame.event.get():
        if f.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.fill((155,155,155))
    pi = 3.14
    pygame.draw.arc(window,(0,0,255), (0,0,640,640),5*pi/4,9*pi/4)
    pygame.display.update()
