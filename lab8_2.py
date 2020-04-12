import pygame
import random

pygame.init()
class Pygameprog(object):
    
    def __init__(self):
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screenrect = self.screen.get_rect()
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background2= self.background.copy()
        self.ballsurface = pygame.Surface((50,50))
        self.ballrect= self.ballsurface.get_rect()
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.paint_big_circles = False
        self.cleanup = True
        self.playtime = 0
        pygame.display.set_caption("x: paint ({}) y: cleanup ({}) ,"
                               " w: white, 0-9: limit FPS to {}"
                               " (now: {:.2f})".format(
                    self.paint_big_circles, self.cleanup, self.FPS,self.clock.get_fps()))
        self.ballx = 550
        self.bally=240
        self.dx = 60
        self.dy = 50

    def wildPainting(self):
        pygame.draw.circle(self.background, (random.randint(0,255),
                       random.randint(0,255), random.randint(0,255)),
                       (random.randint(0,self.screenrect.width),
                       random.randint(0,self.screenrect.height)),
                       random.randint(50,500))
        

    

    
    

    def run(self):
        
        self.ballsurface.set_colorkey((0,0,0))
        self.background.fill((255,255,255))
        pygame.draw.circle(self.ballsurface, (0,0,255), (25,25),25)
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.ballsurface, (self.ballx,self.bally))
        mainloop=True
        while mainloop:
            milliseconds = self.clock.tick(self.FPS)  # milliseconds passed since last frame
            seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
            self.playtime += seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False # pygame window closed by user
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False # user pressed ESC
                    elif event.key == pygame.K_1:
                        self.FPS = 5
                    elif event.key == pygame.K_2:
                        self.FPS = 20
                    elif event.key == pygame.K_3:
                        self.FPS = 30
                    elif event.key == pygame.K_4:
                        self.FPS = 40
                    elif event.key == pygame.K_5:
                        self.FPS = 50
                    elif event.key == pygame.K_6:
                        self.FPS = 60
                    elif event.key == pygame.K_7:
                        self.FPS = 70
                    elif event.key == pygame.K_8:
                        self.FPS = 80
                    elif event.key == pygame.K_9:
                        self.FPS = 90
                    elif event.key == pygame.K_0:
                        self.FPS = 1000 # absurd high value
                    elif event.key == pygame.K_x:
                        self.paint_big_circles =  not self.paint_big_circles # toggle
                    elif event.key == pygame.K_y:
                        self.cleanup = not self.cleanup # toggle boolean value
                    elif event.key == pygame.K_w: # restore old background
                        self.background.blit(self.background2, (0,0)) # clean the screen

                
            
            if self.cleanup:
                self.screen.blit(self.background, (0,0))     #draw background on screen (overwriting all)
            if self.paint_big_circles:
                self.wildPainting()
            self.ballx += self.dx * seconds # float, since seconds passed since last frame is a decimal value
            self.bally += self.dy * seconds 
            # bounce ball if out of screen
            if self.ballx < 0:
                self.ballx = 0
                self.dx *= -1 
            elif self.ballx + self.ballrect.width > self.screenrect.width:
                self.ballx = self.screenrect.width - self.ballrect.width
                self.dx *= -1
            if self.bally < 0:
                self.bally = 0
                self.dy *= -1
            elif self.bally + self.ballrect.height > self.screenrect.height:
                self.bally = self.screenrect.height - self.ballrect.height
                self.dy *= -1
            # paint the ball    
            self.screen.blit(self.ballsurface, (round(self.ballx,0), round(self.bally,0 )))
            pygame.display.flip() 
        print("This 'game' was played for {:.2f} seconds".format(self.playtime)) 


if __name__ == '__main__':
    pygame.init()
    game=Pygameprog()
    game.run()
