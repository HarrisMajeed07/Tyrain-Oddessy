import pygame
import sys
pygame.init()

width, height = 1600, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Toggle Game State")

brown = (210,180,140)
black = (0, 0, 0)
background_color = brown
game_state = "menu"
font = pygame.font.Font('Fonts\Pixeltype.ttf', 60)

#Menu - Title Image
title_image = pygame.image.load('Assets/Tyrain Oddessy Title.png').convert_alpha()
title_image_rect = title_image.get_rect(midtop = (800,100))

#Start Button
start_surf = font.render('Start', False, 'Black')
start_rect = start_surf.get_rect(center = (800, 300))

#Quit Button
quit_surf = font.render(' Quit', False, 'Black')
quit_rect = quit_surf.get_rect(center = (800, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == "menu":
                background_color = black
                game_state = "running"
            else:
                background_color = brown
                game_state = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                game_state = "running"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    mouse_pos = pygame.mouse.get_pos()
    if start_rect.collidepoint((mouse_pos)):
        pygame.mouse.get_pressed()
    if quit_rect.collidepoint((mouse_pos)):
        pygame.mouse.get_pressed()

    screen.fill(background_color)
    screen.blit(start_surf,start_rect)
    screen.blit(quit_surf,quit_rect)
    screen.blit(title_image, title_image_rect)

    if game_state == "running":
        screen.fill(black)
        # game logic

    pygame.display.flip()