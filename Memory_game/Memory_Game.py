import pygame
from random import *


#레벨에 맞게 설정
def setup(level):
   #얼마동안 숫자보여줄지
    global display_time
    display_time = 5 -(level//3)
    display_time = max(display_time,1)#1초 미만이면 1초로 처리

    #얼마나 많은 숫자를 보여줄 것인가
    number_count = (level // 3) + 5
    number_count = min(number_count, 20) #만약 20 초과시 20으로 처리

    #실제 화면에 grid 형태로 숫자 랜덤 배치
    shuffle_grid(number_count)

#숫자 섞기 *********
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130 #각 Grid cell 별 가로 , 세로 크기
    button_size = 110 # Grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 55 #전체 스크린 왼쪽 여백
    screen_top_margin = 20 # 전체 스크린 위쪽 여백

    #[[0,0,0,0,0,0,0,5,0],
    # [0,0,0,0,0,4,0,0,0],
    # [0,0,1,0,0,0,2,0,0],
    # [0,0,0,0,3,0,0,0,0],
    # [0,0,0,0,0,0,0,0,0]]
    grid = [[0 for col in range(columns)] for row in range(rows)] #5 x 9
    
    number = 1 #시작 숫자 1부터 number_count 까지 , 만약 5라면 5까지 숫자를 랜덤으로 배치

    while number <= number_count:
        row_idx = randrange(0, rows) #0,1,2,3,4 중에서 랜덤으로 뽑기
        col_idx = randrange(0,columns) #0~8 중에서 랜덤으로 뽑기

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] == number
            number += 1

            # 현재 grid cell 위치 기준으로 x,y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2) 

            #숫자 버튼 만들기 
            button = pygame.Rect(0,0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)

        #배치된 랜덤 숫자 확인
        print(grid)




#시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE,start_button.center, 60,5)
    #흰색으로 동그라미를 그리는데 중심좌표는 start_button의 중심좌표 따라가고
    #반지름 60 , 선 두께 5

    msg = game_font.render(f"{curr_level}", True, WHITE)
    msg_rect = msg.get_rect(center=start_button.center)
    screen.blit(msg, msg_rect)

#게임 화면 보여주기 
def display_game_screen():
    global hidden
    if not hidden:
        elapsed_time = (pygame.time.get_ticks() - start_ticks)  / 1000
        if elapsed_time > display_time:
            hidden = True

    for idx, rect in enumerate(number_buttons, start=1):
        if hidden: #숨김처리
            #버튼 사각형 그리기
            pygame.draw.rect(screen , WHITE, rect)
        else:
        # 실제 숫자 텍스트 
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center = rect.center)
            screen.blit(cell_text, text_rect)

#pos 에 해당하는 버튼 확인
def check_buttons(pos):
    global start,start_ticks


    if start: #게임이 시작했으면
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True
        start_ticks = pygame.time.get_ticks()

def check_number_buttons(pos):
    global start,hidden,curr_level

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:
                print("Correct")
                del number_buttons[0]
                if not hidden:
                    hidden = True
            else: # 잘못된 숫자 클릭
                game_over()
            break
    if len(number_buttons) == 0:
        start = False
        hidden = False
        curr_level += 1
        setup(curr_level)

def game_over():
    global running
    running = False

    msg = game_font.render(f"Your level is {curr_level}", True,WHITE)
    msg_rect = msg.get_rect(center=(screen_width/2 , screen_height/2))

    screen.fill(BLACK)
    screen.blit(msg,msg_rect)

#초기화
pygame.init()
screen_width = 1280 #가로 크기
screen_height = 720 #세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None,120) #폰트정의

#시작 버튼 
start_button = pygame.Rect(0,0,120,120)
start_button.center = (120 , screen_height - 120)

#색깔
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (50, 50,50)

number_buttons = [] #플레이어가 눌러야하는 버튼들
display_time = None # 숫자보여주는 시간
start_ticks = None #시간계산
curr_level = 1 #현재 레벨

#게임 시작 여부
start = False
#숫자 숨김 여부 (사용자가 1을 클릭 했거나 , 보여주는 시간 초과했을때)
hidden = False

#게임 시작 전에 게임 설정 함수 수행 
setup(curr_level)

#게임 루프 
running = True #게임이 실행중인가?
while running:
    click_pos = None
    #이벤트 루프
    for event in pygame.event.get(): #어떤 이벤트 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트인가?
            running = False #게임이 더 이상 실행중 x
        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            print(click_pos)

    #화면 전체 까맣게
    screen.fill(BLACK)

    if start:
        display_game_screen()#게임화면 표시
    else:
        display_start_screen()#시작화면 표시

    if click_pos:
        check_buttons(click_pos)
        


    #화면 업데이트
    pygame.display.update()

pygame.time.delay(5000)
#게임종료
pygame.quit()