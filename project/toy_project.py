import pygame
import os
#################################################################
# 기본 초기화(반드시 해야할 것들) # 
pygame.init()

#화면크기 설정
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width , screen_height))


#화면 타이틀
pygame.display.set_caption("game")  #게임 이름

#FPS
clock = pygame.time.Clock()
###############################################################

#1. 사용자 게임 초기화(배경화면 , 게임 이미지, 좌표, 속도, 폰트)
current_path = os.path.dirname(__file__) 
image_path = os.path.join(current_path, "pygame_images")

#배경
background = pygame.image.load(os.path.join(image_path, "background.png"))\

#스테이지
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

#캐릭터
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_heihgt = character_size[1]
character_width = character_size[0]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_heihgt - stage_height

#캐릭터 이동 방향
character_to_x = 0

#캐릭터 이동 속도
character_speed = 5

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기 발사 #위치(x, y)
weapons = [] 
weapon_speed = 10

# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "ball_1.png")),
    pygame.image.load(os.path.join(image_path, "ball_2.png")),
    pygame.image.load(os.path.join(image_path, "ball_3.png")),
    pygame.image.load(os.path.join(image_path, "ball_4.png"))
]

#공 크기에 따른 최초 스피드
ball_y_speed = [-18, -15, -12, -9]

#공들
balls = []

#최초 발생 공   
balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx": 0,
    "to_x": 3,
    "to_y": -6,
    "init_spd_y": ball_y_speed[0]
})

weapon_remove = -1
ball_remove = -1

#font
game_font = pygame.font.Font(None, 40)


total_time = 100
start_ticks = pygame.time.get_ticks()

game_result = "Game Over"


#event loop
running = True
while running:
    dt = clock.tick(30) #초당 프레임 수
    

    #2. 이벤트 처리
    for event in pygame.event.get(): #어떤 이벤특가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 event
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


    #3. 게임 케릭터 위치 정의
    character_x_pos += character_to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #3-1 무기 위치 정의
    weapons = [[w[0], w[1] - weapon_speed] for w  in weapons if w[1] > 0]
    #3-2 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_hieght = ball_size[1]

        #가로벽

        if ball_pos_x < 0 or ball_pos_x > screen_width-ball_width:
            ball_val["to_x"] *= -1

        #위 아래
        if ball_pos_y >= screen_height - stage_height - ball_hieght:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: #속도를 줄인다.
            ball_val["to_y"] += 0.5
        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
    
    #4. 충돌 처리(공 캐릭터)
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        if character_rect.colliderect(ball_rect):
             running = False
             break
    #4-1 공 무기 충돌
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_rect = weapon.get_rect(topleft=weapon_val)

        for ball_idx, ball_val in enumerate(balls):
            ball_rect = ball_images[ball_val["img_idx"]].get_rect(
                topleft=(ball_val["pos_x"], ball_val["pos_y"])
            )

            if weapon_rect.colliderect(ball_rect):
                weapon_remove = weapon_idx
                ball_remove = ball_idx

                if ball_val["img_idx"] < 3:
                    ball_width = ball_rect.width
                    ball_height = ball_rect.height

                    small_rect = ball_images[ball_val["img_idx"] + 1].get_rect()
                    sw, sh = small_rect.width, small_rect.height

                    balls.append({
                        "pos_x": ball_val["pos_x"] + ball_width/2 - sw/2,
                        "pos_y": ball_val["pos_y"] + ball_height/2 - sh/2,
                        "img_idx": ball_val["img_idx"] + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y": ball_y_speed[ball_val["img_idx"] + 1]
                    })

                    balls.append({
                        "pos_x": ball_val["pos_x"] + ball_width/2 - sw/2,
                        "pos_y": ball_val["pos_y"] + ball_height/2 - sh/2,
                        "img_idx": ball_val["img_idx"] + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_spd_y": ball_y_speed[ball_val["img_idx"] + 1]
                    })

                break
        if ball_remove > -1:
            break
    if ball_remove > -1:
        del balls[ball_remove]
        ball_remove = -1
    if weapon_remove > -1:
        del weapons[weapon_remove]
        weapon_remove = -1
    
    #모든 공 없애면
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    #5. 화면에 그리기

    screen.blit(background, (0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    elapsed_time = (pygame.time.get_ticks()- start_ticks) / 1000
    timer = game_font.render(f"Time:{int(total_time-elapsed_time)}", True, (255,255,255))
    screen.blit(timer, (10, 10) ) 

    if total_time - elapsed_time <= 0:
        game_result= "Time Over"
        running = False
    
    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width/2),int(screen_height/2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)

#게임 종료
pygame.quit()