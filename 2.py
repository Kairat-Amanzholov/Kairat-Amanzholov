import pygame

window = pygame.display.set_mode([800,640])


while 1:
    for f in pygame.event.get():
        if f.type == pygame.QUIT:
            pygame.quit()
            quit()
    window.fill((155,155,155))
   # pygame.draw.circle(window, (0,0,255), (400,320),10)
  # pygame.draw.rect(window, (0,0,0), (100,180),10)
    pygame.display.update()
