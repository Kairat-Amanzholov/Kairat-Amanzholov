import pygame
import random
import os

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
myfont = pygame.font.SysFont('arial', 40)


screen = pygame.display.set_mode((1200, 900))
background = pygame.image.load('ground.jpg')

FPS = 60

shoot_sound = pygame.mixer.music.load("crash.mp3")

clock = pygame.time.Clock() 

tank1 = pygame.image.load('t1_up.png') 
tank2 = pygame.image.load('t2_up.png') 

arrow_1 = pygame.Surface((10,10))
arrow_2 = pygame.Surface((10,10))


arrow1_x = 1200
arrow1_y = 1200
shoot1 = False
arrow2_x = 1200
arrow2_y = 1200
shoot2 = False

x_tank1 = 100
y_tank1 = 500

x_tank2 = 1000
y_tank2 = 500

life1 = 3
life2 = 3


pygame.display.update()

def end(last_thene1, last_thene2):
	myfont = pygame.font.SysFont('arial', 100)
	ending1 = myfont.render('GAME OVER', True, (255,255,255))
	ending1_1 = myfont.render('P1 wins', True, (255,255,255))
	ending2 = myfont.render('GAME OVER', True, (255,255,255))
	ending1_2 = myfont.render('P2 wins', True, (255,255,255))

	if last_thene1 == 0:
		background = pygame.display.set_mode((1200,900))
		background.fill((0,0,0))
		screen.blit(background,(0,0))
		screen.blit(ending2,(300, 200))
		screen.blit(ending1_2,(400, 300))
		
	if last_thene2 == 0:
		background = pygame.display.set_mode((1200,900))
		background.fill((0,0,0))
		screen.blit(background,(0,0))
		screen.blit(ending1,(300, 200))
		screen.blit(ending1_1,(400, 300))



while True:

	pygame.display.update()

	arrow_1.fill((255,255,0))
	arrow_2.fill((255,255,0))

	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]:
		tank1 = pygame.image.load('t1_left.png')
		x_tank1 = x_tank1 - 4
		if shoot1:
			arrow1_x = arrow1_x - 15
			if arrow1_x < - 10:
				shoot1 = False

	if keys[pygame.K_s]:
		tank1 = pygame.image.load('t1_down.png')
		y_tank1 = y_tank1 + 4
		if shoot1:
			arrow1_y = arrow1_y + 15
			if arrow1_y > 1000 + 10:
				shoot1 = False

	if keys[pygame.K_w]:
		tank1 = pygame.image.load('t1_up.png') 
		y_tank1 = y_tank1 - 4
		if shoot1:
			arrow1_y = arrow1_y - 15
			if arrow1_y < - 10:
				shoot1 = False

	if keys[pygame.K_d]:
		tank1 = pygame.image.load('t1_right.png')
		x_tank1 = x_tank1 + 4
		if shoot1:
			arrow1_x = arrow1_x + 15
			if arrow1_x > 1200 + 10:
				shoot1 = False


	if keys[pygame.K_RIGHT]:
		tank2 = pygame.image.load('t2_right.png')
		x_tank2 = x_tank2 + 4
		if shoot2:
			arrow2_x = arrow2_x + 15
			if arrow2_x > 1200 + 10:
				shoot2 = False


	if keys[pygame.K_DOWN]:
		tank2 = pygame.image.load('t2_down.png')
		y_tank2 = y_tank2 + 4
		if shoot2:
			arrow2_y = arrow2_y + 15
			if arrow2_y > 900 + 10:
				shoot2 = False

	if keys[pygame.K_UP]:
		tank2 = pygame.image.load('t2_up.png')
		y_tank2 = y_tank2 - 4
		if shoot2:
			arrow2_y = arrow2_y - 15
			if arrow2_y < - 10:
				shoot2 = False


	if keys[pygame.K_LEFT]:
		tank2 = pygame.image.load('t2_left.png')
		x_tank2 = x_tank2 - 4	
		if shoot2:
			arrow2_x = arrow2_x - 15
			if arrow2_x < - 10:
				shoot2 = False


	if arrow1_x >= x_tank2 and arrow1_x <= x_tank2 + 72 and arrow1_y >= y_tank2 and arrow1_y <= y_tank2 +72:
		life2 = life2 - 1
		shoot1 = False
		pygame.mixer.music.play()
		arrow1_x = 1200
		arrow1_y = 1200
		x_tank2 = 1000
		y_tank2 = 500


	if  arrow2_x >= x_tank1 and arrow2_x <= x_tank1 + 72 and arrow2_y >= y_tank1 and arrow2_y <= y_tank1 +72:
		life1 = life1 - 1
		shoot2 = False
		pygame.mixer.music.play()
		arrow2_x = 1200
		arrow2_y = 1200
		x_tank1 = 100
		y_tank1 = 500

	if x_tank1 > 1260:
		x_tank1 = -60

	if x_tank1 < -60:
		x_tank1 = 1260

	if y_tank1 > 960:
		y_tank1 = -60

	if y_tank1 < -60:
		y_tank1 = 960
                                             
	if x_tank2 > 1260:
		x_tank2 = -60

	if x_tank2 < -60:
		x_tank2 = 1260

	if y_tank2 > 960:
		y_tank2 = -60

	if y_tank2 < -60:
		y_tank2 = 960

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			if event.key == pygame.K_SPACE:
				pygame.mixer.music.play()
				if shoot1 == False:
					shoot1 = True

					if keys[pygame.K_d]:
						arrow1_x = x_tank1 + 72
						arrow1_y = y_tank1 + 35

					if keys[pygame.K_w]:
						arrow1_x = x_tank1 + 35
						arrow1_y = y_tank1

					if keys[pygame.K_a]:
						arrow1_x = x_tank1 
						arrow1_y = y_tank1 + 35

					if keys[pygame.K_s]:
						arrow1_x = x_tank1 + 35
						arrow1_y = y_tank1 + 72
				
			if event.key == pygame.K_RETURN:
				pygame.mixer.music.play()
				if shoot2 == False:
					shoot2 = True
					if keys[pygame.K_UP]:
						arrow2_x = x_tank2 + 35
						arrow2_y = y_tank2 

					if keys[pygame.K_LEFT]:
						arrow2_x = x_tank2 
						arrow2_y = y_tank2 + 35

					if keys[pygame.K_RIGHT]:
						arrow2_x = x_tank2 + 72
						arrow2_y = y_tank2 + 35

					if keys[pygame.K_DOWN]:
						arrow2_x = x_tank2 + 35
						arrow2_y = y_tank2 + 72

	string1 = myfont.render("P1:" + str(life1), True, (255,255,255))

	string2 = myfont.render("P2:" + str(life2), True, (255,255,255))
	
	screen.blit(background, (0,0))
	screen.blit(string1, (100, 100))
	screen.blit(string2, (1040, 100))
	screen.blit(tank1, (x_tank1, y_tank1))
	screen.blit(tank2, (x_tank2, y_tank2))
	
	clock.tick(FPS)
	
	screen.blit(arrow_1, (arrow1_x,arrow1_y))
	screen.blit(arrow_2, (arrow2_x,arrow2_y))
	
	end(life1,life2)
	pygame.display.flip()



pygame.quit()