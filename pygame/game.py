import pygame
import time
import random

pygame.init()

display_width = 1000
display_height = 750

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

rump_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Rump Racer')

rumpImage = pygame.image.load('rumpadump.png')

def bolts_speed_display(speed):
	font = pygame.font.SysFont(None,25)
	text = font.render("Speed: " + str(speed),True,white)
	gameDisplay.blit(text,(5,30))

def bolts_dodged(count):
	font = pygame.font.SysFont(None,25)
	text = font.render("Dodged: " + str(count),True,red)
	gameDisplay.blit(text,(5,15))

def bolts(bolts_x,bolts_y,bolts_w,bolts_h,color):
	pygame.draw.rect(gameDisplay,color,[bolts_x,bolts_y,bolts_w,bolts_h])

def rump(x,y):
	gameDisplay.blit(rumpImage,(x,y))
	
def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text,largeText)
	TextRect.center = ((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	
	pygame.display.update()
	
	time.sleep(2)
	
	game_loop()

def text_objects(text, font):
	textSurface = font.render(text, True, red) #True for anti-aliasing
	return textSurface, textSurface.get_rect()
	
def crash():
	message_display('You crashed!')
	
def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.70)

	x_change = 0

	bolts_start_x = random.randrange(0,display_width)
	bolts_start_y = -600
	bolts_speed = 5
	bolts_speed_mult = 1
	bolts_width = 15
	bolts_height = 120
	
	dodged = 0
	
	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -4
				elif event.key == pygame.K_RIGHT:
					x_change = 4
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		
		x += x_change
		gameDisplay.fill(black)
		
		#bolts(bolts_x,bolts_y,bolts_w,blots_h,color)
		bolts(bolts_start_x,bolts_start_y,bolts_width,bolts_height,white)
		bolts_start_y += bolts_speed
		rump(x,y)
		bolts_dodged(dodged)
		bolts_speed_display(bolts_speed)
		
		if x > (display_width - rump_width) or x < 0:
			crash()
			
		if bolts_start_y > display_height:
			bolts_start_y = 0 - bolts_height
			bolts_start_x = random.randrange(0,display_width)
			dodged += 1
			#speed
			bolts_speed_mult += 1
			if bolts_speed_mult % 5 == 0:
				bolts_speed += 3
			bolts_width += (dodged * 1.1)
			
		if y < bolts_start_y + bolts_height:	
			if x > bolts_start_x and x < bolts_start_x + bolts_width or x + rump_width > bolts_start_x and x + rump_width < bolts_start_x + bolts_width:
				crash()
		
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
