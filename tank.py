import pygame
import random
import os

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

def shoot1(arrow_x, arrow_y, x_tank, y_tank):
	if arrow_x >= x_tank and arrow_x <= x_tank + 70 and arrow_y >= y_tank and arrow_y <= y_tank +70:
		return 1
	else: return 0

def shoot2(arrow_x, arrow_y, x_tank, y_tank):
	if arrow_x >= x_tank and arrow_x <= x_tank + 70 and arrow_y >= y_tank and arrow_y <= y_tank +70:
		return 1
	else: return 0



screen = pygame.display.set_mode((1000, 1000))
background = pygame.image.load('ground.jpg')

FPS = 60


clock = pygame.time.Clock() 

tank1 = pygame.image.load('t1_up.png') 
tank2 = pygame.image.load('t2_up.png') 

life1 = 3
life2 = 3
myfont = pygame.font.SysFont('arial', 40)

arrow_1 = pygame.Surface((15,15))

arrow1_x = 1100
arrow1_y = 1100
strike1 = False

arrow_2 = pygame.Surface((15,15))

arrow2_x = 1100
arrow2_y = 1100
strike2 = False

x_tank1 = 70 
y_tank1 = 535

x_tank2 = 860
y_tank2 = 535

speed = 5

shoot_sound = pygame.mixer.music.load("crash.mp3")


up = 'up'
down = 'down'
left = 'left'
right = 'right'

movement1 = False 
movement2 = False 





pygame.display.update()

def end(l1, l2):
	myfont = pygame.font.SysFont('arial', 100)
	ending1 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending1_1 = myfont.render('P1 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending2 = myfont.render('GAME OVER', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	ending1_2 = myfont.render('P2 wins', True, (random.randint(0,255),random.randint(0,255),random.randint(0,255)))
	if l1 == 0:
		background = pygame.image.load('ground1.jpg')
		screen.blit(background,(0,0))
		screen.blit(ending2,(250, 200))
		screen.blit(ending1_2,(350, 300))
	if l2 == 0:
		background = pygame.image.load('ground1.jpg')
		screen.blit(background,(0,0))
		screen.blit(ending1,(250, 200))
		screen.blit(ending1_1,(350, 300))


play = True

while play:

	pygame.display.update()
	arrow_1.fill((random.randint(0,255),random.randint(0,255),0))
	arrow_2.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

	if movement1 == up:
		tank1 = pygame.image.load('t1_up.png') 
		y_tank1 = y_tank1 - speed
		if strike1:
			arrow1_y = arrow1_y - 20
			if arrow1_y < - 10:
				strike1 = False

	if movement1 == down:
		tank1 = pygame.image.load('t1_down.png')
		y_tank1 = y_tank1 + speed
		if strike1:
			arrow1_y = arrow1_y + 20
			if arrow1_y > 1000 + 10:
				strike1 = False

	if movement1 == right:
		tank1 = pygame.image.load('t1_right.png')
		x_tank1 = x_tank1 + speed
		if strike1:
			arrow1_x = arrow1_x + 20
			if arrow1_x > 1000 + 10:
				strike1 = False

	if movement1 == left:
		tank1 = pygame.image.load('t1_left.png')
		x_tank1 = x_tank1 - speed
		if strike1:
			arrow1_x = arrow1_x - 20
			if arrow1_x < - 10:
				strike1 = False


	if movement2 == up:
		tank2 = pygame.image.load('t2_up.png')
		y_tank2 = y_tank2 - speed
		if strike2:
			arrow2_y = arrow2_y - 20
			if arrow2_y < - 10:
				strike2 = False

	if movement2 == down:
		tank2 = pygame.image.load('t2_down.png')
		y_tank2 = y_tank2 + speed
		if strike2:
			arrow2_y = arrow2_y + 20
			if arrow2_y > 1000 + 10:
				strike2 = False

	if movement2 == right:
		tank2 = pygame.image.load('t2_right.png')
		x_tank2 = x_tank2 + speed
		if strike2:
			arrow2_x = arrow2_x + 20
			if arrow2_x > 1000 + 10:
				strike2 = False

	if movement2 == left:
		tank2 = pygame.image.load('t2_left.png')
		x_tank2 = x_tank2 - speed	
		if strike2:
			arrow2_x = arrow2_x - 20
			if arrow2_x < - 10:
				strike2 = False



	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				exit()
			if event.key == pygame.K_SPACE:
				pygame.mixer.music.play()
				if strike1 == False:
					strike1 = True
					if movement1 == up:
						arrow1_x = x_tank1 + 32
						arrow1_y = y_tank1
					if movement1 == down:
						arrow1_x = x_tank1 + 32
						arrow1_y = y_tank1 + 70
					if movement1 == right:
						arrow1_x = x_tank1 + 70
						arrow1_y = y_tank1 + 32
					if movement1 == left:
						arrow1_x = x_tank1 
						arrow1_y = y_tank1 + 32

				
			if event.key == pygame.K_RETURN:
				pygame.mixer.music.play()
				if strike2 == False:
					strike2 = True
					if movement2 == up:
						arrow2_x = x_tank2 + 32
						arrow2_y = y_tank2 
					if movement2 == down:
						arrow2_x = x_tank2 + 32
						arrow2_y = y_tank2 + 70
					if movement2 == right:
						arrow2_x = x_tank2 + 70
						arrow2_y = y_tank2 + 32
					if movement2 == left:
						arrow2_x = x_tank2 
						arrow2_y = y_tank2 + 32

			if event.key == pygame.K_d:  
				movement1 = right
			if event.key == pygame.K_a:
				movement1 = left
			if event.key == pygame.K_w: 	
				movement1 = up
			if event.key == pygame.K_s:
				movement1 = down
			if event.key == pygame.K_LALT:
				movement1 = False

			if event.key == pygame.K_RIGHT:
				movement2 = right
			if event.key == pygame.K_LEFT:
				movement2 = left
			if event.key == pygame.K_UP:
				movement2 = up
			if event.key == pygame.K_DOWN:
				movement2 = down
			if event.key == pygame.K_KP0:
				movement2 = False

	if shoot1(arrow1_x, arrow1_y, x_tank2, y_tank2):
		life2 = life2 - 1
		strike1 = False
		pygame.mixer.music.play()
		arrow1_x = 1100
		arrow1_y = 1100
		x_tank2 = 860
		y_tank2 = 535


	if shoot2(arrow2_x, arrow2_y, x_tank1, y_tank1):
		life1 = life1 - 1
		strike2 = False
		pygame.mixer.music.play()
		arrow2_x = 1100
		arrow2_y = 1100
		x_tank1 = 70
		y_tank1 = 535


	if x_tank1 > 1000 + 60:
		x_tank1 = 0 - 60
	if x_tank1 < 0 -60:
		x_tank1 = 1000 + 60
	if y_tank1 > 1000 + 60:
		y_tank1 = 0 - 60
	if y_tank1 < 0 -60:
		y_tank1 = 1000 + 60
                                             
	if x_tank2 > 1000 + 60:
		x_tank2 = 0 - 60
	if x_tank2 < 0 -60:
		x_tank2 = 1000 + 60
	if y_tank2 > 1000 + 60:
		y_tank2 = 0 - 60
	if y_tank2 < 0 -60:
		y_tank2 = 1000 + 60

	string1 = myfont.render("P1:" + str(life1), True, (255,255,255))
	string2 = myfont.render("P2:" + str(life2), True, (255,255,255))


	screen.blit(background, (0,0))
	screen.blit(string1, (70, 70))
	screen.blit(string2, (840, 70))
	screen.blit(tank1, (x_tank1, y_tank1))
	screen.blit(tank2, (x_tank2, y_tank2))
	clock.tick(FPS)
	screen.blit(arrow_1, (arrow1_x,arrow1_y))
	screen.blit(arrow_2, (arrow2_x,arrow2_y))

	pygame.display.set_caption("TANK GAME")
	end(life1,life2)
	pygame.display.flip()



pygame.quit()