import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter = 10
text =  '10'
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
print(pygame.USEREVENT)
run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT and counter > 1: 
            counter -= 1
            text = str(counter) 
            print(counter)
        elif counter == 1:
            text = "boom"
        if e.type == pygame.QUIT: 
            run = False


    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.update()
    clock.tick(60)