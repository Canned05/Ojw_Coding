import pygame


pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('오정우')

sky_img = pygame.image.load("img/sky.png")
sun_img = pygame.image.load("img/sun.png")

run = True  
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		print("left")
	elif key[pygame.K_RIGHT]:
		print("right")
	

	screen.blit(sky_img,(0,0))
	screen.blit(sun_img,(10,10))
	pygame.display.update()

pygame.quit()