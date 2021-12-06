#Python game from Udemy
import pygame, sys, random, time

pygame.init() # Initialize pygame
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
wood_bg = pygame.image.load("Wood_BG.png")
land_bg = pygame.image.load("Land_BG.png")
water_bg = pygame.image.load("Water_BG.png")
cloud1_bg = pygame.image.load("Cloud1.png")
cloud2_bg = pygame.image.load("Cloud2.png")
crosshair = pygame.image.load("crosshair.png")
crosshair_rect = 0,0
time_up = False
played_time = 0
duck_surface = pygame.image.load("duck.png")
duck_list =[]
for duck in range(20):
    duck_position_x = random.randrange(50,1200)
    duck_position_y = random.randrange(120,550)
    duck_rect = duck_surface.get_rect(center = (duck_position_x, duck_position_y))
    duck_list.append(duck_rect)

landposition_y = 510
landspeed = 1
waterposition_y = 630
waterspeed = 1.5

game_font = pygame.font.Font(None,60)
text_surface = game_font.render('You Won !! ',True,(255,255,255))
text_rect = text_surface.get_rect(center=(640, 360))

start_time = time.time()
print(start_time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect(center = event.pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            for index,duck_rect in enumerate(duck_list):
                if duck_rect.collidepoint(event.pos):
                    del duck_list[index]


    screen.blit(wood_bg, (0, 0))
    for duck_rect in duck_list:
        screen.blit(duck_surface,duck_rect)

    if len(duck_list) <= 0:
        screen.blit(text_surface,(text_rect))
        if time_up == False:
            end_time = time.time()
            played_time = end_time - start_time
            text_time = game_font.render(f'Time record:{played_time:.2f}s', True, (255, 255, 255))
            time_rect = text_time.get_rect(center=(640, 420))
            screen.blit(text_time, (time_rect))

            time_up = True
            print(played_time)
        if time_up == True:
            screen.blit(text_time, (time_rect))


    screen.blit(crosshair, crosshair_rect)
    screen.blit(cloud1_bg, (10, 50))
    screen.blit(cloud2_bg, (300, 40))
    screen.blit(cloud2_bg, (510, 80))
    screen.blit(cloud1_bg, (600, 50))
    screen.blit(cloud2_bg, (900, 90))
    screen.blit(cloud1_bg, (1100, 50))


# Animate land
    landposition_y += landspeed
    if landposition_y <= 500 or landposition_y >=540:
        landspeed *= -1
    screen.blit(land_bg, (0,landposition_y))

# Animate water
    waterposition_y += waterspeed
    if waterposition_y <= 610 or waterposition_y >= 660:
        waterspeed *= -1

    screen.blit(water_bg, (0, waterposition_y))
    pygame.display.update()
    clock.tick(120)


