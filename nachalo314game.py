import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

   
x = 320
y = 240 
speed = 20
  
game = True

while game:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x-=speed
    if keys[pygame.K_RIGHT]:
        x+=speed
    if keys[pygame.K_UP]:
        y-=speed
    if keys[pygame.K_DOWN]:
        y+=speed    
    if x < 25:
        x = 25
    elif x > 615:
        x = 615
    if y < 25:
        y = 25
    elif y > 455:
        y = 455

    window.fill((255,255,255))
    pygame.draw.circle(window, (255,0,0), (x,y),25) 
    pygame.display.update()


pygame.quit()