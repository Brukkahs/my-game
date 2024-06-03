import pygame
from sys import exit
import random
import button


def bat_animation():
    global bat_surf, bat_index
    
    bat_index += 0.1
    if bat_index >= len(bat_fly):
        bat_index = 0
    bat_surf = bat_fly[int(bat_index)]

def spaceshipY_animation():
    global spaceshipY_surf, spaceshipY_index


    spaceshipY_index += 0.1
    if spaceshipY_index >= len(spaceshipY_fly):
        spaceshipY_index = 0
    spaceshipY_surf = spaceshipY_fly[int(spaceshipY_index)]

def spaceshipR_animation():
    global spaceshipR_surf, spaceshipR_index

    spaceshipR_index += 0.1
    if spaceshipR_index >= len(spaceshipR_fly):
        spaceshipR_index = 0
    spaceshipR_surf = spaceshipR_fly[int(spaceshipR_index)]


pygame.init()

def draw_text(text, font, text_col, x, y):
    img = font.render(text, font, text_col)
    screen.blit(img, (x,y))

text_font = pygame.font.SysFont("banglamn", 50)
big_font = pygame.font.SysFont("arialblack", 100)
vbig_font = pygame.font.SysFont("arialblack", 200)
cool_font = pygame.font.SysFont('banglamn', 110)
#print(pygame.font.get_fonts())

col = (60,70,80)
col1 = (255,0,0)
col2 = (0,0,0)
width = 1400
height = 800
# game over sound from open source website called mixkit
win_sound = pygame.mixer.Sound('gameover.wav')

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Main Menu')
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
game_state = "start"
difficulty = "none"
counter = 100
text =  '100'

#sky art from opengameart by: Paulina rivera
sky_surface = pygame.image.load('graphics/sky2.png').convert_alpha()


spaceshipY_fly_1 = pygame.image.load('graphics/spaceshipyellow/spaceship.png').convert_alpha()
spaceshipY_fly_2 = pygame.image.load('graphics/spaceshipyellow/spaceship2.png').convert_alpha()
spaceshipY_fly_3 = pygame.image.load('graphics/spaceshipyellow/spaceship3.png').convert_alpha()
spaceshipY_fly = [spaceshipY_fly_1,spaceshipY_fly_2,spaceshipY_fly_3, spaceshipY_fly_2]
spaceshipY_index = 0
spaceshipY_surf = spaceshipY_fly[spaceshipY_index]
spaceshipY_rect = spaceshipY_surf.get_rect(midbottom = (100,100))


spaceshipR_fly_1 = pygame.image.load('graphics/spaceshipred/space.png').convert_alpha()
spaceshipR_fly_2 = pygame.image.load('graphics/spaceshipred/space2.png').convert_alpha()
spaceshipR_fly_3 = pygame.image.load('graphics/spaceshipred/space3.png').convert_alpha()
spaceshipR_fly = [spaceshipR_fly_1,spaceshipR_fly_2,spaceshipR_fly_3, spaceshipR_fly_2]
spaceshipR_index = 0
spaceshipR_surf = spaceshipR_fly[spaceshipR_index]
spaceshipR_rect = spaceshipR_surf.get_rect(midbottom = (100,200))

# bat art from opengameart by: Bagzie 
bat_fly_1 = pygame.image.load('graphics/bat/tile004.png').convert_alpha()
bat_fly_2 = pygame.image.load('graphics/bat/tile005.png').convert_alpha()
bat_fly_3 = pygame.image.load('graphics/bat/tile006.png').convert_alpha()
bat_fly_4 = pygame.image.load('graphics/bat/tile007.png').convert_alpha()
bat_fly = [bat_fly_1,bat_fly_2,bat_fly_3,bat_fly_4]
bat_index = 0
bat_surf = bat_fly[bat_index]
bat_jump = "0"
bat_rect1 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,390)))
bat_rect2 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,790)))
bat_rect3 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,790)))
bat_rect4= bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,790)))
bat_rect5 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,790)))
bat_rect6 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(200,390)))
bat_rect7 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(210,790)))
bat_rect8 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(210,790)))
bat_rect9= bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(210,790)))
bat_rect10 = bat_surf.get_rect(midbottom = (random.randint(100,950),random.randint(210,790)))
bat_x_vel1 = random.randint(2,6)
bat_y_vel1 = random.randint(2,6)
bat_x_vel2 = random.randint(2,6)
bat_y_vel2 = random.randint(2,6)
bat_x_vel3 = random.randint(2,6)
bat_y_vel3 = random.randint(2,6)
bat_x_vel4 = random.randint(2,6)
bat_y_vel4 = random.randint(2,6)
bat_x_vel5 = random.randint(2,6)
bat_y_vel5 = random.randint(2,6)
bat_x_vel6 = random.randint(2,6)
bat_y_vel6 = random.randint(2,6)
bat_x_vel7 = random.randint(2,6)
bat_y_vel7 = random.randint(2,6)
bat_x_vel8 = random.randint(2,6)
bat_y_vel8 = random.randint(2,6)
bat_x_vel9 = random.randint(2,6)
bat_y_vel9 = random.randint(2,6)
bat_x_vel10 = random.randint(2,6)
bat_y_vel10 = random.randint(2,6)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
start_img = pygame.image.load('images/button_start.png').convert_alpha()
single_img = pygame.image.load('images/1 player.png').convert_alpha()
multi_img = pygame.image.load('images/2 players.png').convert_alpha()
hard_img = pygame.image.load('images/hard.png').convert_alpha()
medium_img = pygame.image.load('images/medium.png').convert_alpha()
easy_img = pygame.image.load('images/easy.png').convert_alpha()
#create button instances
resume_button = button.Button(600, 125, resume_img, 1)
options_button = button.Button(590, 250, options_img, 1)
quit_button = button.Button(630, 375, quit_img, 1)
back_button = button.Button(600, 450, back_img, 1)
start_button = button.Button(570, 450, start_img, 1)
single_button = button.Button(520, 450, single_img, 1)
multi_button = button.Button(500, 550, multi_img, 1)
hard_button = button.Button(605, 350, hard_img, 1)
medium_button = button.Button(560, 250, medium_img, 1)
easy_button = button.Button(610, 150, easy_img, 1)

print(pygame.USEREVENT)
while True:
    

    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    

      
    
        
    
    if game_state == "multiplayer": 
        screen.blit(sky_surface,(0,0))  
        draw_text("Press SPACE to pause", text_font, col, 400, 730)      
        spaceshipY_animation()
        screen.blit(spaceshipY_surf,spaceshipY_rect)
        spaceshipR_animation()
        screen.blit(spaceshipR_surf,spaceshipR_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            spaceshipY_rect.y -= 4
        if keys[pygame.K_a]:
            spaceshipY_rect.x -= 4
        if keys[pygame.K_s]:
            spaceshipY_rect.y += 4
        if keys[pygame.K_d]:
            spaceshipY_rect.x += 4
        
        if keys[pygame.K_UP]:
            spaceshipR_rect.y -= 4
        if keys[pygame.K_LEFT]:
            spaceshipR_rect.x -= 4
        if keys[pygame.K_DOWN]:
            spaceshipR_rect.y += 4
        if keys[pygame.K_RIGHT]:
            spaceshipR_rect.x += 4
        
        if keys[pygame.K_SPACE]:
            game_state = "paused"
        
        if spaceshipY_rect.x < -30:
            spaceshipY_rect.x = 1420
        if spaceshipY_rect.x > 1420:
            spaceshipY_rect.x = -30
        
        if spaceshipY_rect.y < -30:
            spaceshipY_rect.y = 820
        if spaceshipY_rect.y > 820:
            spaceshipY_rect.y = -30

        
        if spaceshipR_rect.x < -30:
            spaceshipR_rect.x = 1420
        if spaceshipR_rect.x > 1420:
            spaceshipR_rect.x = -30
        
        if spaceshipR_rect.y < -30:
            spaceshipR_rect.y = 820
        if spaceshipR_rect.y > 820:
            spaceshipR_rect.y = -30

        if difficulty == "easy":
        
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100




            if spaceshipY_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
        
            if spaceshipR_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
    


        if difficulty == "medium":
        
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            screen.blit(bat_surf,bat_rect7) 
            screen.blit(bat_surf,bat_rect8)
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100

            bat_rect7.centerx += bat_x_vel7
            bat_rect7.centery += bat_y_vel7

            if bat_rect7.right>=width or bat_rect7.left <= 0:
                bat_x_vel7 *= random.randint(-110,-90)/100
            if bat_rect7.top <= 0 or bat_rect7.bottom >= height:
                bat_y_vel7 *= random.randint(-110,-90)/100

            bat_rect8.centerx += bat_x_vel8
            bat_rect8.centery += bat_y_vel8

            if bat_rect8.right>=width or bat_rect8.left <= 0:
                bat_x_vel8 *= random.randint(-110,-90)/100
            if bat_rect8.top <= 0 or bat_rect8.bottom >= height:
                bat_y_vel8 *= random.randint(-110,-90)/100



            if spaceshipY_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect7):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect8):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect7):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect8):
                game_state = "collision"
                win_sound.play()
        
        if difficulty == "hard":
       
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            screen.blit(bat_surf,bat_rect7) 
            screen.blit(bat_surf,bat_rect8)
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100

            bat_rect7.centerx += bat_x_vel7
            bat_rect7.centery += bat_y_vel7

            if bat_rect7.right>=width or bat_rect7.left <= 0:
                bat_x_vel7 *= random.randint(-110,-90)/100
            if bat_rect7.top <= 0 or bat_rect7.bottom >= height:
                bat_y_vel7 *= random.randint(-110,-90)/100

            bat_rect8.centerx += bat_x_vel8
            bat_rect8.centery += bat_y_vel8

            if bat_rect8.right>=width or bat_rect8.left <= 0:
                bat_x_vel8 *= random.randint(-110,-90)/100
            if bat_rect8.top <= 0 or bat_rect8.bottom >= height:
                bat_y_vel8 *= random.randint(-110,-90)/100

            bat_rect7.centerx += bat_x_vel7
            bat_rect7.centery += bat_y_vel7

            if bat_rect9.right>=width or bat_rect9.left <= 0:
                bat_x_vel9 *= random.randint(-110,-90)/100
            if bat_rect9.top <= 0 or bat_rect9.bottom >= height:
                bat_y_vel9 *= random.randint(-110,-90)/100

            bat_rect9.centerx += bat_x_vel9
            bat_rect9.centery += bat_y_vel9

            if bat_rect10.right>=width or bat_rect10.left <= 0:
                bat_x_vel10 *= random.randint(-110,-90)/100
            if bat_rect10.top <= 0 or bat_rect10.bottom >= height:
                bat_y_vel10 *= random.randint(-110,-90)/100



            if spaceshipY_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect7):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect8):
                game_state = "collision"
            if spaceshipY_rect.colliderect(bat_rect9):
                game_state = "collision"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect10):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect1):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect2):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect3):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect4):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect5):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect6):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect7):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect8):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect9):
                game_state = "collision"
                win_sound.play()
            if spaceshipR_rect.colliderect(bat_rect10):
                game_state = "collision"
                win_sound.play()

    if game_state == "single player": 
        screen.blit(sky_surface,(0,0))  
        draw_text("Press SPACE to pause", text_font, col, 400, 730) 
        
        
        
            
        
            

        for e in pygame.event.get():
            if counter >1: 
                counter -= 1
                text = str(counter) 
                print(counter)
            elif counter == 1:
                game_state = "win"

        screen.blit(big_font.render(text, True, (0, 0, 0)), (32, 48))

        spaceshipY_animation()
        screen.blit(spaceshipY_surf,spaceshipY_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            spaceshipY_rect.y -= 4
        if keys[pygame.K_a]:
            spaceshipY_rect.x -= 4
        if keys[pygame.K_s]:
            spaceshipY_rect.y += 4
        if keys[pygame.K_d]:
            spaceshipY_rect.x += 4
        
        if keys[pygame.K_SPACE]:
            game_state = "paused"
        
        if spaceshipY_rect.x < -30:
            spaceshipY_rect.x = 1420
        if spaceshipY_rect.x > 1420:
            spaceshipY_rect.x = -30
        
        if spaceshipY_rect.y < -30:
            spaceshipY_rect.y = 820
        if spaceshipY_rect.y > 820:
            spaceshipY_rect.y = -30

        if difficulty == "easy":
        
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100




        if spaceshipY_rect.colliderect(bat_rect1):
            game_state = "collision1"
            win_sound.play()
        if spaceshipY_rect.colliderect(bat_rect2):
            game_state = "collision1"
            win_sound.play()
        if spaceshipY_rect.colliderect(bat_rect3):
            game_state = "collision1"
            win_sound.play()
        if spaceshipY_rect.colliderect(bat_rect4):
            game_state = "collision1"
            win_sound.play()
        if spaceshipY_rect.colliderect(bat_rect5):
            game_state = "collision1"
            win_sound.play()
        if spaceshipY_rect.colliderect(bat_rect6):
            game_state = "collision1"
            win_sound.play()

        if difficulty == "medium":
        
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            screen.blit(bat_surf,bat_rect7) 
            screen.blit(bat_surf,bat_rect8)
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100

            bat_rect7.centerx += bat_x_vel7
            bat_rect7.centery += bat_y_vel7

            if bat_rect7.right>=width or bat_rect7.left <= 0:
                bat_x_vel7 *= random.randint(-110,-90)/100
            if bat_rect7.top <= 0 or bat_rect7.bottom >= height:
                bat_y_vel7 *= random.randint(-110,-90)/100

            bat_rect8.centerx += bat_x_vel8
            bat_rect8.centery += bat_y_vel8

            if bat_rect8.right>=width or bat_rect8.left <= 0:
                bat_x_vel8 *= random.randint(-110,-90)/100
            if bat_rect8.top <= 0 or bat_rect8.bottom >= height:
                bat_y_vel8 *= random.randint(-110,-90)/100



            if spaceshipY_rect.colliderect(bat_rect1):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect2):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect3):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect4):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect5):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect6):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect7):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect8):
                game_state = "collision1"
                win_sound.play()

        if difficulty == "hard":
        
            bat_animation()
            screen.blit(bat_surf,bat_rect1)
            screen.blit(bat_surf,bat_rect2) 
            screen.blit(bat_surf,bat_rect3)
            screen.blit(bat_surf,bat_rect4)
            screen.blit(bat_surf,bat_rect5)  
            screen.blit(bat_surf,bat_rect6)
            screen.blit(bat_surf,bat_rect7) 
            screen.blit(bat_surf,bat_rect8)
            screen.blit(bat_surf,bat_rect9) 
            screen.blit(bat_surf,bat_rect10)
            

            bat_rect1.centerx += bat_x_vel1
            bat_rect1.centery += bat_y_vel1

            if bat_rect1.right>=width or bat_rect1.left <= 0:
                bat_x_vel1 *= random.randint(-110,-90)/100
            if bat_rect1.top <= 0 or bat_rect1.bottom >= height:
                bat_y_vel1 *= random.randint(-110,-90)/100

            bat_rect2.centerx += bat_x_vel2
            bat_rect2.centery += bat_y_vel2

            if bat_rect2.right>=width or bat_rect2.left <= 0:
                bat_x_vel2 *= random.randint(-110,-90)/100
            if bat_rect2.top <= 0 or bat_rect2.bottom >= height:
                bat_y_vel2 *= random.randint(-110,-90)/100

            bat_rect3.centerx += bat_x_vel3
            bat_rect3.centery += bat_y_vel3

            if bat_rect3.right>=width or bat_rect3.left <= 0:
                bat_x_vel3 *= random.randint(-110,-90)/100
            if bat_rect3.top <= 0 or bat_rect3.bottom >= height:
                bat_y_vel3 *= random.randint(-110,-90)/100

            bat_rect4.centerx += bat_x_vel4
            bat_rect4.centery += bat_y_vel4

            if bat_rect4.right>=width or bat_rect4.left <= 0:
                bat_x_vel4 *= random.randint(-110,-90)/100
            if bat_rect4.top <= 0 or bat_rect4.bottom >= height:
                bat_y_vel4 *= random.randint(-110,-90)/100

            bat_rect5.centerx += bat_x_vel5
            bat_rect5.centery += bat_y_vel5

            if bat_rect5.right>=width or bat_rect5.left <= 0:
                bat_x_vel5 *= random.randint(-110,-90)/100
            if bat_rect5.top <= 0 or bat_rect5.bottom >= height:
                bat_y_vel5 *= random.randint(-110,-90)/100

            bat_rect6.centerx += bat_x_vel6
            bat_rect6.centery += bat_y_vel6

            if bat_rect6.right>=width or bat_rect6.left <= 0:
                bat_x_vel6 *= random.randint(-110,-90)/100
            if bat_rect6.top <= 0 or bat_rect6.bottom >= height:
                bat_y_vel6 *= random.randint(-110,-90)/100

            bat_rect7.centerx += bat_x_vel7
            bat_rect7.centery += bat_y_vel7

            if bat_rect7.right>=width or bat_rect7.left <= 0:
                bat_x_vel7 *= random.randint(-110,-90)/100
            if bat_rect7.top <= 0 or bat_rect7.bottom >= height:
                bat_y_vel7 *= random.randint(-110,-90)/100

            bat_rect8.centerx += bat_x_vel8
            bat_rect8.centery += bat_y_vel8

            if bat_rect8.right>=width or bat_rect8.left <= 0:
                bat_x_vel8 *= random.randint(-110,-90)/100
            if bat_rect8.top <= 0 or bat_rect8.bottom >= height:
                bat_y_vel8 *= random.randint(-110,-90)/100
            
            bat_rect9.centerx += bat_x_vel9
            bat_rect9.centery += bat_y_vel9

            if bat_rect9.right>=width or bat_rect9.left <= 0:
                bat_x_vel9 *= random.randint(-110,-90)/100
            if bat_rect9.top <= 0 or bat_rect9.bottom >= height:
                bat_y_vel9 *= random.randint(-110,-90)/100

            bat_rect10.centerx += bat_x_vel10
            bat_rect10.centery += bat_y_vel10

            if bat_rect10.right>=width or bat_rect10.left <= 0:
                bat_x_vel10 *= random.randint(-110,-90)/100
            if bat_rect10.top <= 0 or bat_rect10.bottom >= height:
                bat_y_vel10 *= random.randint(-110,-90)/100



            if spaceshipY_rect.colliderect(bat_rect1):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect2):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect3):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect4):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect5):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect6):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect7):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect8):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect9):
                game_state = "collision1"
                win_sound.play()
            if spaceshipY_rect.colliderect(bat_rect10):
                game_state = "collision1"
                win_sound.play()
        
    
    if game_state == "start":
        screen.blit(sky_surface,(0,0))  
        keys = pygame.key.get_pressed()
        draw_text("Galactic Bat Dodge", cool_font, col2, 140, 200)   
        if single_button.draw(screen):
            game_state = "difficulty"
            sing = 1
            
        if multi_button.draw(screen):
            game_state = "difficulty"
            sing = 2
    
    if game_state == "win":
        screen.fill("Green")
        draw_text("you win", vbig_font, col2, 300, 200) 
        
        
        
    if game_state == "difficulty":
        screen.blit(sky_surface,(0,0))
        draw_text("pick your difficulty", text_font, col2, 450, 20)  
        if hard_button.draw(screen):
            if sing == 1:
                game_state = "single player"
            elif sing == 2:
                game_state = "multiplayer"
            difficulty = "hard"
        if medium_button.draw(screen):
            difficulty = "medium"
            if sing == 1:
                game_state = "single player"
            elif sing == 2:
                game_state = "multiplayer"
        if easy_button.draw(screen):
            difficulty = "easy"
            if sing == 1:
                game_state = "single player"
            elif sing == 2:
                game_state = "multiplayer"
    
    
    
    if game_state == "paused":
        screen.blit(sky_surface,(0,0))  

        if resume_button.draw(screen):
            if sing == 2:
                game_state = "multiplayer"
            elif sing == 1:
                game_state = "single player"
        if options_button.draw(screen):
            game_state = "options"
        if quit_button.draw(screen):
            break
        

    if game_state == "collision1":
            if spaceshipY_rect.colliderect(bat_rect1):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect2):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect3):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect4):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250,200)  
            if spaceshipY_rect.colliderect(bat_rect5):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect6):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect7):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect8):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect9):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  
            if spaceshipY_rect.colliderect(bat_rect10):
                screen.fill("Red")
                draw_text("you lose", vbig_font, col, 250, 200)  

    #test
    if game_state == "collision":
            
        if spaceshipR_rect.colliderect(bat_rect1):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect2):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect3):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect4):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect5):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect6):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect7):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipR_rect.colliderect(bat_rect8):
            screen.fill("Yellow")
            draw_text("yellow wins!!!", big_font, col, 340, 300)  
        if spaceshipY_rect.colliderect(bat_rect1):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect2):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect3):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect4):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect5):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect6):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect7):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect8):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect9):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300)  
        if spaceshipY_rect.colliderect(bat_rect10):
            screen.fill("Red")
            draw_text("red wins!!!", big_font, col, 440, 300) 
        
            

    pygame.display.update()
    clock.tick(60)

    