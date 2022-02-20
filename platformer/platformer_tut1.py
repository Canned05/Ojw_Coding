import pygame

class Map:
	def __init__(self , map):
		self.map = map
		dirt_img = pygame.image.load("img/dirt.png")
		grass_img = pygame.image.load("img/grass.png")

		self.dirt_img = pygame.transform.scale(dirt_img ,(50,50))
		self.grass_img = pygame.transform.scale(grass_img ,(50,50))

	def update(self,SCR):
		for i,row in enumerate(self.map): # row -> [0,0,0,0,...0]
			for j, col in enumerate(row): # col -> 0 or 1
				print(j,col)
				if col == 1:
					SCR.blit(self.grass_img,(50*j,50*i))
				elif col == 2:
					SCR.blit(self.dirt_img,(50*j,50*i))
					
class Player:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.img = pygame.image.load("img/guy1.png")
	
	def update(self , screen):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.x -= 5
		elif key[pygame.K_RIGHT]:
			self.x += 5
		screen.blit(self.img , (self.x,self.y))
		


pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('오정우')

sky_img = pygame.image.load("img/sky.png")
sun_img = pygame.image.load("img/sun.png")

player_img = pygame.image.load("img/guy1.png")

player_x = 100
player_y = 100

#dirt_img = pygame.image.load("img/dirt.png")
#grass_img = pygame.image.load("img/grass.png")

#dirt_img = pygame.transform.scale(dirt_img ,(50,50))
#grass_img = pygame.transform.scale(grass_img ,(50,50))

world_map = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],

]

map = Map(world_map)
player = Player(200,200)

run = True  
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	'''
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		player.x -= 5
	elif key[pygame.K_RIGHT]:
		player.x += 5
	'''
	

	screen.blit(sky_img,(0,0))
	screen.blit(sun_img,(10,10))
	map.update(screen)
	player.update(screen)
	#screen.blit(player.img , (player.x,player.y))

	'''
	for i,row in enumerate(world_map): # row -> [0,0,0,0,...0]
		for j, col in enumerate(row): # col -> 0 or 1
			print(j,col)
			if col == 1:
				screen.blit(self.grass_img,(50*j,50*i))
			elif col == 2:
				screen.blit(self.dirt_img,(50*j,50*i))
	'''
	pygame.display.update()

pygame.quit()