import pygame
from Config import *
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tyrain Odyssey")

health_surface_border = pygame.Rect(42, 36, 200, 20)
health_bar = pygame.Rect(42, 36, health_width, 20)
enemy_square = pygame.Rect(190, 186, 50, 20)

# Player ------------------------------------
player_idle_1 = pygame.image.load('Assets/Character/Knight/Idle/character_6.png').convert_alpha()
player_idle_2 = pygame.image.load('Assets/Character/Knight/Idle/character_7.png').convert_alpha()
player_idle_3 = pygame.image.load('Assets/Character/Knight/Idle/character_8.png').convert_alpha()
player_idle_4 = pygame.image.load('Assets/Character/Knight/Idle/character_9.png').convert_alpha()

player_walk_1 = pygame.image.load('Assets/Character/Knight/Walking/character_0.png').convert_alpha()
player_walk_2 = pygame.image.load('Assets/Character/Knight/Walking/character_1.png').convert_alpha()
player_walk_3 = pygame.image.load('Assets/Character/Knight/Walking/character_2.png').convert_alpha()
player_walk_4 = pygame.image.load('Assets/Character/Knight/Walking/character_3.png').convert_alpha()
player_walk_5 = pygame.image.load('Assets/Character/Knight/Walking/character_4.png').convert_alpha()
player_walk_6 = pygame.image.load('Assets/Character/Knight/Walking/character_5.png').convert_alpha()

player_walk_back_7 = pygame.image.load('Assets/Character/Knight/Walking back/character_10.png').convert_alpha()
player_walk_back_8 = pygame.image.load('Assets/Character/Knight/Walking back/character_11.png').convert_alpha()
player_walk_back_9 = pygame.image.load('Assets/Character/Knight/Walking back/character_12.png').convert_alpha()
player_walk_back_10 = pygame.image.load('Assets/Character/Knight/Walking back/character_13.png').convert_alpha()
player_walk_back_11 = pygame.image.load('Assets/Character/Knight/Walking back/character_14.png').convert_alpha()
player_walk_back_12 = pygame.image.load('Assets/Character/Knight/Walking back/character_15.png').convert_alpha()

player_block_1 = pygame.image.load('Assets/Character/Knight/Block/character_17.png').convert_alpha()
player_block_2 = pygame.image.load('Assets/Character/Knight/Block/character_18.png').convert_alpha()
player_block_3 = pygame.image.load('Assets/Character/Knight/Block/character_19.png').convert_alpha()
player_block_4 = pygame.image.load('Assets/Character/Knight/Block/character_20.png').convert_alpha()
player_block_5 = pygame.image.load('Assets/Character/Knight/Block/character_21.png').convert_alpha()

player_index = 0
player_idle = [player_idle_1, player_idle_2, player_idle_3, player_idle_4]
player_walk_forward = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6]
player_walk_back = [player_walk_back_7, player_walk_back_8, player_walk_back_9, player_walk_back_10, player_walk_back_11, player_walk_back_12]
player_block = [player_block_1, player_block_2, player_block_3, player_block_4, player_block_5]
player_surf = player_idle[player_index]

player_rect = player_surf.get_rect(topleft=(90, 100))
direction = "forward"
last_direction = "forward" #Keeps track of the last direction of the player movement.

def player_animation(moving, direction):
    global player_surf, player_index
    if moving:
        if direction == "forward":
            player_index += 0.1
            if player_index >= len(player_walk_forward):
                player_index = 0
            player_surf = player_walk_forward[int(player_index)]
        else:
            player_index += 0.1
            if player_index >= len(player_walk_back):
                player_index = 0
            player_surf = player_walk_back[int(player_index)]

    else: 
        player_index += 0.1
        if player_index >= len(player_idle):
            player_index = 0
        if direction == "forward":
            player_surf = player_walk_forward[0] #forward frame is displayed
        else:
            player_surf = player_walk_back[0] #backwards frame is displayed
             
    # else:
    #     player_index += 0.1
    #     if player_index >= len(player_idle):
    #         player_index = 0
    #     player_surf = player_idle[int(player_index)]

def draw_tile(x, y, tile_index, camera_x, camera_y):
    screen.blit(tile_images[tile_index], (x * tile_size - camera_x, y * tile_size - camera_y))

# Menu - Title Image
title_image = pygame.image.load('Assets\Tyrain Oddessy Title.png').convert_alpha()
title_image_rect = title_image.get_rect(midtop=(800, 100))

# Start Button
start_surf = font.render('Start', False, 'Black')
start_rect = start_surf.get_rect(center=(800, 300))

# Quit Button
quit_surf = font.render('Quit', False, 'Black')
quit_rect = quit_surf.get_rect(center=(800, 400))

game_state = "menu"
background_color = brown

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == "running":
                background_color = brown
                game_state = "menu"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                game_state = "running"
            elif quit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    mouse_pos = pygame.mouse.get_pos()

    if game_state == "menu":
        screen.fill(background_color)
        screen.blit(start_surf, start_rect)
        screen.blit(quit_surf, quit_rect)
        screen.blit(title_image, title_image_rect)
        pygame.display.flip()
        continue

    # Game Running ------------------------------------

    keys = pygame.key.get_pressed()
    moving = False
    if keys[pygame.K_w]:
        player_rect.y -= player_speed
        moving = True
        for y, row in enumerate(tilemap_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    if player_rect.colliderect(tile_rect):
                        player_rect.top = tile_rect.bottom

    if keys[pygame.K_a]:
        player_rect.x -= player_speed
        moving = True     
        direction = "backward"
        last_direction = "backward"
        for y, row in enumerate(tilemap_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    if player_rect.colliderect(tile_rect):
                        player_rect.left = tile_rect.right

    if keys[pygame.K_s]:
        player_rect.y += player_speed
        moving = True
        for y, row in enumerate(tilemap_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    if player_rect.colliderect(tile_rect):
                        player_rect.bottom = tile_rect.top

    if keys[pygame.K_d]:
        player_rect.x += player_speed
        moving = True
        direction = "forward"
        last_direction = "forward"
        for y, row in enumerate(tilemap_data):
            for x, tile in enumerate(row):
                if tile == 1:
                    tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                    if player_rect.colliderect(tile_rect):
                        player_rect.right = tile_rect.left

    # keys = pygame.key.get_pressed()
    # moving = False
    # if keys[pygame.K_w]:
    #     player_rect.y -= player_speed
    #     moving = True
    #     for y, row in enumerate(tilemap_data):
    #         for x, tile in enumerate(row):
    #             if tile == 1:
    #                 tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    #                 if player_rect.colliderect(tile_rect):
    #                     player_rect.top = tile_rect.bottom

    # if keys[pygame.K_a]:
    #     player_rect.x -= player_speed
    #     moving = True     
    #     direction = "backward"
    #     for y, row in enumerate(tilemap_data):
    #         for x, tile in enumerate(row):
    #             if tile == 1:
    #                 tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    #                 if player_rect.colliderect(tile_rect):
    #                     player_rect.left = tile_rect.right

    # if keys[pygame.K_s]:
    #     player_rect.y += player_speed
    #     moving = True
    #     for y, row in enumerate(tilemap_data):
    #         for x, tile in enumerate(row):
    #             if tile == 1:
    #                 tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    #                 if player_rect.colliderect(tile_rect):
    #                     player_rect.bottom = tile_rect.top

    # if keys[pygame.K_d]:
    #     player_rect.x += player_speed
    #     moving = True
    #     direction = "forward"
    #     for y, row in enumerate(tilemap_data):
    #         for x, tile in enumerate(row):
    #             if tile == 1:
    #                 tile_rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
    #                 if player_rect.colliderect(tile_rect):
    #                     player_rect.right = tile_rect.left


    if not moving:
        direction = last_direction #if the player is not moving this will use the last direction and will display that

    camera_x = player_rect.x - (screen_width // 2)
    camera_y = player_rect.y - (screen_height // 2)
    
    screen.fill(white)
    for y, row in enumerate(tilemap_data):
        for x, tile in enumerate(row):
            if tile != 0:
                draw_tile(x, y, tile, camera_x, camera_y)

    player_animation(moving, direction)
    screen.blit(player_surf, player_rect.move(-camera_x, -camera_y).topleft)
    pygame.draw.rect(screen, black, health_surface_border)
    pygame.draw.rect(screen, red, health_bar)

    pygame.display.flip()
    clock.tick(60)