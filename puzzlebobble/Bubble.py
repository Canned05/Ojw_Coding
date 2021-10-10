import os
import pygame
from pygame import image

class Bubble(pugame.sprite.Sprite):
    def __init__(self.image , color , position):
        super().__init__()
        self.image = image
        self.color = pygame.Color
        self.rect = image.get_rect(center=position)

def setup():
    global map
    map = [
        list("RRYYBBGG"),
        list("RRYYBBG/"),
        list("BBGGRRYY"),
        list("BGGRRYY/"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
        list("......./"),
        list("........"),
    ]

    for row_idx, row in enumerate(map):
        for col_idx, col in enumerate(row):
            if col in [".", "/"]:
                continue
            position = get_bubble_posittion(row_idx, col_idx)
            image = get_bubble_image(col)
            bubble_group.add(Bubble(image, col ,position))

def get_bubble_postiton(row_idx, col_idx):
    pos_x = col_idx * CELL_SIZE + (BUBLLE_WIDTH // 2)
    pos_y = row_idx * CELL_SIZE + (BUBBLE_HEIGHT // 2)
    if row_idx % 2 ==1:
        pos_x += CELL_SIZE //2
    return pos_x,pos_y

def get_bubble_image(color):
    if color == "R":
        return bubble_images[0]
    elif color == "Y":
        return bubble_images[1]
    elif color == "B":
        return bubble_images[2]
    elif color == "G":
        return bubble_images[3]
    elif color == "P":
        return bubble_images[4]
    else: 
        return bubble_images[-1]        





pygame.init()
screen_width = 448 
screen_height =720
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

#배경 이미지 불러오기
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

running = True
while running:
    clock.tick(60) #FPS 60 으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnung = False

    screen.blit(background, (0,0))
    pygame.display.update()


pygame.quit()