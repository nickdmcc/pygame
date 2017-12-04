import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

rump_width = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
pygame.display.set_caption('Rump Racer')

rumpImage = pygame.image.load('rumpadump.png')

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
	y = (display_height * 0.65)

	x_change = 0

	gameExit = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -3
				elif event.key == pygame.K_RIGHT:
					x_change = 3
					
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		
		x += x_change
		
		gameDisplay.fill(black)
		rump(x,y)
		
		if x > (display_width - rump_width) or x < 0:
			crash()
		
		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
