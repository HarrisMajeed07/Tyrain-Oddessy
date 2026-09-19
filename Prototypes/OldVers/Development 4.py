import pygame
from Config import *
import sys
import random
import math

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tyrain Odyssey")

health_surface_border = pygame.Rect(42, 36, 200, 20)
health_bar = pygame.Rect(42, 36, health_width, 20)

enemy_square = pygame.Rect(250, 250, enemy_size, enemy_size)

# Pause Button
pause_button = pygame.image.load('Assets/Pause.png').convert_alpha()
pause_button_rect = pause_button.get_rect(topright=(screen_width - 20, 20))

# Crosshair - Load the sprite, but keep the default cursor in the menu
crosshair = pygame.image.load('Assets/Crosshair 1.png').convert_alpha()
crosshair_rect = crosshair.get_rect()

# Player ------------------------------------
player_idle_1 = pygame.image.load('Assets/Character/Knight/Idle/character_6.png').convert_alpha()
player_idle_2 = pygame.image.load('Assets/Character/Knight/Idle/character_7.png').convert_alpha()
player_idle_3 = pygame.image.load('Assets/Character/Knight/Idle/character_8.png').convert_alpha()
player_idle_4 = pygame.image.load('Assets/Character/Knight/Idle/character_9.png').convert_alpha()

#Walk Right
player_walk_1 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_0.png').convert_alpha()
player_walk_2 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_1.png').convert_alpha()
player_walk_3 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_2.png').convert_alpha()
player_walk_4 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_3.png').convert_alpha()
player_walk_5 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_4.png').convert_alpha()
player_walk_6 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_5.png').convert_alpha()
player_walk_7 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_6.png').convert_alpha()
player_walk_8 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_7.png').convert_alpha()

#Right Up
player_walk_up_1 = pygame.image.load('Player Assets\Walk Up\images\walk_up_0.png').convert_alpha()
player_walk_up_2 = pygame.image.load('Player Assets\Walk Up\images\walk_up_1.png').convert_alpha()
player_walk_up_3 = pygame.image.load('Player Assets\Walk Up\images\walk_up_2.png').convert_alpha()
player_walk_up_4 = pygame.image.load('Player Assets\Walk Up\images\walk_up_3.png').convert_alpha()
player_walk_up_5 = pygame.image.load('Player Assets\Walk Up\images\walk_up_4.png').convert_alpha()
player_walk_up_6 = pygame.image.load('Player Assets\Walk Up\images\walk_up_5.png').convert_alpha()
player_walk_up_7 = pygame.image.load('Player Assets\Walk Up\images\walk_up_6.png').convert_alpha()
player_walk_up_8 = pygame.image.load('Player Assets\Walk Up\images\walk_up_7.png').convert_alpha()

#Right Down
player_walk_down_1 = pygame.image.load('Player Assets\Walk Down\images\walk_down_0.png').convert_alpha()
player_walk_down_2 = pygame.image.load('Player Assets\Walk Down\images\walk_down_1.png').convert_alpha()
player_walk_down_3 = pygame.image.load('Player Assets\Walk Down\images\walk_down_2.png').convert_alpha()
player_walk_down_4 = pygame.image.load('Player Assets\Walk Down\images\walk_down_3.png').convert_alpha()
player_walk_down_5 = pygame.image.load('Player Assets\Walk Down\images\walk_down_4.png').convert_alpha()
player_walk_down_6 = pygame.image.load('Player Assets\Walk Down\images\walk_down_5.png').convert_alpha()
player_walk_down_7 = pygame.image.load('Player Assets\Walk Down\images\walk_down_6.png').convert_alpha()
player_walk_down_8 = pygame.image.load('Player Assets\Walk Down\images\walk_down_7.png').convert_alpha()

#Walk Left
player_walk_back_1 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_0.png').convert_alpha()
player_walk_back_2 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_1.png').convert_alpha()
player_walk_back_3 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_2.png').convert_alpha()
player_walk_back_4 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_3.png').convert_alpha()
player_walk_back_5 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_4.png').convert_alpha()
player_walk_back_6 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_5.png').convert_alpha()
player_walk_back_7 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_6.png').convert_alpha()
player_walk_back_8 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_7.png').convert_alpha()

#Left Up
player_walk_leftup_1 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_0.png').convert_alpha()
player_walk_leftup_2 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_1.png').convert_alpha()
player_walk_leftup_3 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_2.png').convert_alpha()
player_walk_leftup_4 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_3.png').convert_alpha()
player_walk_leftup_5 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_4.png').convert_alpha()
player_walk_leftup_6 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_5.png').convert_alpha()
player_walk_leftup_7 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_6.png').convert_alpha()
player_walk_leftup_8 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_7.png').convert_alpha()

#Left Down
player_walk_leftdown_1 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_0.png').convert_alpha()
player_walk_leftdown_2 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_1.png').convert_alpha()
player_walk_leftdown_3 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_2.png').convert_alpha()
player_walk_leftdown_4 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_3.png').convert_alpha()
player_walk_leftdown_5 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_4.png').convert_alpha()
player_walk_leftdown_6 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_5.png').convert_alpha()
player_walk_leftdown_7 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_6.png').convert_alpha()
player_walk_leftdown_8 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_7.png').convert_alpha()

#Up
player_walk_up_1 = pygame.image.load('Player Assets\Walk Up\images\walk_up_0.png').convert_alpha()
player_walk_up_2 = pygame.image.load('Player Assets\Walk Up\images\walk_up_1.png').convert_alpha()
player_walk_up_3 = pygame.image.load('Player Assets\Walk Up\images\walk_up_2.png').convert_alpha()
player_walk_up_4 = pygame.image.load('Player Assets\Walk Up\images\walk_up_3.png').convert_alpha()
player_walk_up_5 = pygame.image.load('Player Assets\Walk Up\images\walk_up_4.png').convert_alpha()
player_walk_up_6 = pygame.image.load('Player Assets\Walk Up\images\walk_up_5.png').convert_alpha()
player_walk_up_7 = pygame.image.load('Player Assets\Walk Up\images\walk_up_6.png').convert_alpha()
player_walk_up_8 = pygame.image.load('Player Assets\Walk Up\images\walk_up_7.png').convert_alpha()

#Down
player_walk_down_1 = pygame.image.load('Player Assets\Walk Down\images\walk_down_0.png').convert_alpha()
player_walk_down_2 = pygame.image.load('Player Assets\Walk Down\images\walk_down_1.png').convert_alpha()
player_walk_down_3 = pygame.image.load('Player Assets\Walk Down\images\walk_down_2.png').convert_alpha()
player_walk_down_4 = pygame.image.load('Player Assets\Walk Down\images\walk_down_3.png').convert_alpha()
player_walk_down_5 = pygame.image.load('Player Assets\Walk Down\images\walk_down_4.png').convert_alpha()
player_walk_down_6 = pygame.image.load('Player Assets\Walk Down\images\walk_down_5.png').convert_alpha()
player_walk_down_7 = pygame.image.load('Player Assets\Walk Down\images\walk_down_6.png').convert_alpha()
player_walk_down_8 = pygame.image.load('Player Assets\Walk Down\images\walk_down_7.png').convert_alpha()

player_index = 0
player_idle = [player_idle_1, player_idle_2, player_idle_3, player_idle_4]
#right
player_walk_forward = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7, player_walk_8]
player_walk_right_up = [player_walk_up_1, player_walk_up_2, player_walk_up_3, player_walk_up_4, player_walk_up_5, player_walk_up_6, player_walk_up_7, player_walk_up_8]
player_walk_right_down = [player_walk_down_1, player_walk_down_2, player_walk_down_3, player_walk_down_4, player_walk_down_5, player_walk_down_6, player_walk_down_7, player_walk_down_8]
#left
player_walk_back = [player_walk_back_1, player_walk_back_2, player_walk_back_3, player_walk_back_4, player_walk_back_5, player_walk_back_6, player_walk_back_7,  player_walk_back_8]
player_walk_left_up = [player_walk_leftup_1, player_walk_leftup_2, player_walk_leftup_3, player_walk_leftup_4, player_walk_leftup_5, player_walk_leftup_6, player_walk_leftup_7, player_walk_leftup_8]
player_walk_left_down = [player_walk_leftdown_1, player_walk_leftdown_2, player_walk_leftdown_3, player_walk_leftdown_4, player_walk_leftdown_5, player_walk_leftdown_6, player_walk_leftdown_7, player_walk_leftdown_8]
#up/down
player_walk_up = [player_walk_up_1, player_walk_up_2, player_walk_up_3, player_walk_up_4, player_walk_up_5, player_walk_up_6, player_walk_up_7, player_walk_up_8]
player_walk_down = [player_walk_down_1, player_walk_down_2, player_walk_down_3, player_walk_down_4, player_walk_down_5, player_walk_down_6, player_walk_down_7, player_walk_down_8]

player_surf = player_idle[player_index]

player_rect = player_surf.get_rect(topleft=(90, 90))
direction = "forward"
last_direction = "forward" #Keeps track of the last direction of the player movement.

#Calculating the distance between the enemy and the player
def calculate_distance(player, square):
    dx = player.centerx - square.centerx
    dy = player.centery - square.centery
    return (dx ** 2 + dy ** 2) ** 0.5

def move_square(player, square):
    if player.x > square.x:
        square.x += enemy_speed
    elif player.x < square.x:
        square.x -= enemy_speed
    if player.y > square.y:
        square.y += enemy_speed
    elif player.y < square.y:
        square.y -= enemy_speed

def player_animation(moving, direction):
    global player_surf, player_index
    if moving:
        player_index += 0.1
        if direction == "forward":
            if player_index >= len(player_walk_forward):
                player_index = 0
            player_surf = player_walk_forward[int(player_index)]
        elif direction == "backward":
            if player_index >= len(player_walk_back):
                player_index = 0
            player_surf = player_walk_back[int(player_index)]
        elif direction == "right_up":
            if player_index >= len(player_walk_right_up):
                player_index = 0
            player_surf = player_walk_right_up[int(player_index)]
        elif direction == "right_down":
            if player_index >= len(player_walk_right_down):
                player_index = 0
            player_surf = player_walk_right_down[int(player_index)]
        elif direction == "left_up":
            if player_index >= len(player_walk_left_up):
                player_index = 0
            player_surf = player_walk_left_up[int(player_index)]
        elif direction == "left_down":
            if player_index >= len(player_walk_left_down):
                player_index = 0
            player_surf = player_walk_left_down[int(player_index)]
        elif direction == "up":
            if player_index >= len(player_walk_up):
                player_index = 0
            player_surf = player_walk_up[int(player_index)]
        elif direction == "down":
            if player_index >= len(player_walk_down):
                player_index = 0
            player_surf = player_walk_down[int(player_index)]

def draw_tile(x, y, tile_index, camera_x, camera_y):
    screen.blit(tile_images[tile_index], (x * tile_size - camera_x, y * tile_size - camera_y))

# Menu - Title Image
title_image = pygame.image.load('Assets/Tyrain Oddessy Title.png').convert_alpha()
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
                pygame.mouse.set_visible(True)  # Show mouse when returning to the menu

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                game_state = "running"
                pygame.mouse.set_visible(False)  # Hide the cursor when the game starts
            if game_state == "running":
                if pause_button_rect.collidepoint(event.pos):
                    game_state = "menu"
                    pygame.mouse.set_visible(True)  # Show mouse when paused
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
    direction = last_direction

# Function to check for collisions
    def check_collision(player_rect, tilemap_data):
        # Get player's new position
        player_x, player_y = player_rect.topleft
        tile_x = player_x // tile_size
        tile_y = player_y // tile_size

        # Check boundaries
        if tile_x < 0 or tile_x >= len(tilemap_data[0]) or tile_y < 0 or tile_y >= len(tilemap_data):
            return True  # Out of bounds

        # Check if the tile the player is trying to move into is a collision tile (1)
        return tilemap_data[tile_y][tile_x] == 1

    # Inside the game loop, before moving the player:
    if keys[pygame.K_w] and keys[pygame.K_d]:  # Move up-right
        new_rect = player_rect.move(player_speed, -player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "right_up"

    elif keys[pygame.K_w] and keys[pygame.K_a]:  # Move up-left
        new_rect = player_rect.move(-player_speed, -player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "left_up"

    elif keys[pygame.K_s] and keys[pygame.K_d]:  # Move down-right
        new_rect = player_rect.move(player_speed, player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "right_down"

    elif keys[pygame.K_s] and keys[pygame.K_a]:  # Move down-left
        new_rect = player_rect.move(-player_speed, player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "left_down"

    elif keys[pygame.K_w]:  # Move up
        new_rect = player_rect.move(0, -player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "up"

    elif keys[pygame.K_s]:  # Move down
        new_rect = player_rect.move(0, player_speed)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "down"

    elif keys[pygame.K_d]:  # Move right
        new_rect = player_rect.move(player_speed, 0)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "forward"

    elif keys[pygame.K_a]:  # Move left
        new_rect = player_rect.move(-player_speed, 0)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True
            direction = "backward"

    if not moving:
        direction = last_direction  # If the player is not moving, use the last direction

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

    # Enemy (Drawn and Detection)
    distance = calculate_distance(player_rect, enemy_square)
    if distance < enemy_detection:
        move_square(player_rect, enemy_square)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square.move(-camera_x, -camera_y))

    # Draw the crosshair at the position of the mouse
    crosshair_rect.center = mouse_pos
    screen.blit(crosshair, crosshair_rect)

    pygame.draw.rect(screen, black, health_surface_border)
    pygame.draw.rect(screen, red, health_bar)
    screen.blit(pause_button, pause_button_rect)

    pygame.display.flip()
    clock.tick(60)

#WHEN A BUTTON IS PRESSED INCRIMENT POSITION (CAMERA AND PLAYER) BY A CERTAIN AMOUNT OF PIXELS
#https://www.youtube.com/watch?v=tJiKYMQJnYg - collisions for the arrows