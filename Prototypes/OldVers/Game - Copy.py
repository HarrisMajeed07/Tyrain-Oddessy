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

# Crosshair
crosshair = pygame.image.load('Assets/Crosshair 1.png').convert_alpha()
crosshair_rect = crosshair.get_rect()

# Player ------------------------------------
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
player_walk_rightup_1 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_0.png').convert_alpha()
player_walk_rightup_2 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_1.png').convert_alpha()
player_walk_rightup_3 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_2.png').convert_alpha()
player_walk_rightup_4 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_3.png').convert_alpha()
player_walk_rightup_5 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_4.png').convert_alpha()
player_walk_rightup_6 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_5.png').convert_alpha()
player_walk_rightup_7 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_6.png').convert_alpha()
player_walk_rightup_8 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_7.png').convert_alpha()

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

#Bow and arrow
bow_1 = pygame.image.load('Assets/Bow/bow_1.png').convert_alpha()
bow_2 = pygame.image.load('Assets/Bow/bow_2.png').convert_alpha()
bow_3 = pygame.image.load('Assets/Bow/bow_3.png').convert_alpha()
bow_4 = pygame.image.load('Assets/Bow/bow_4.png').convert_alpha()
arrow = pygame.image.load('Assets/Bow/bow_3.png').convert_alpha()

player_index = 0
#right
player_walk_forward = [player_walk_1, player_walk_2, player_walk_3, player_walk_4, player_walk_5, player_walk_6, player_walk_7, player_walk_8]
player_walk_right_up = [player_walk_rightup_1, player_walk_rightup_2, player_walk_rightup_3, player_walk_rightup_4, player_walk_rightup_5, player_walk_rightup_6, player_walk_rightup_7, player_walk_up_8]
player_walk_right_down = [player_walk_down_1, player_walk_down_2, player_walk_down_3, player_walk_down_4, player_walk_down_5, player_walk_down_6, player_walk_down_7, player_walk_down_8]
#left
player_walk_back = [player_walk_back_1, player_walk_back_2, player_walk_back_3, player_walk_back_4, player_walk_back_5, player_walk_back_6, player_walk_back_7,  player_walk_back_8]
player_walk_left_up = [player_walk_leftup_1, player_walk_leftup_2, player_walk_leftup_3, player_walk_leftup_4, player_walk_leftup_5, player_walk_leftup_6, player_walk_leftup_7, player_walk_leftup_8]
player_walk_left_down = [player_walk_leftdown_1, player_walk_leftdown_2, player_walk_leftdown_3, player_walk_leftdown_4, player_walk_leftdown_5, player_walk_leftdown_6, player_walk_leftdown_7, player_walk_leftdown_8]
#up/down
player_walk_up = [player_walk_up_1, player_walk_up_2, player_walk_up_3, player_walk_up_4, player_walk_up_5, player_walk_up_6, player_walk_up_7, player_walk_up_8]
player_walk_down = [player_walk_down_1, player_walk_down_2, player_walk_down_3, player_walk_down_4, player_walk_down_5, player_walk_down_6, player_walk_down_7, player_walk_down_8]
#Bow and arrow animation
bowanimation = [bow_1,bow_2,bow_3,bow_4]
bow_image = pygame.image.load('Assets/Bow/bow_1.png').convert_alpha()

player_surf = player_walk_forward[player_index]
# player_rect = player_surf.get_rect(center=(400, 300))
player_rect = player_surf.get_rect(player_surf)
player_center_x = player_rect.centerx
player_center_y = player_rect.centery

player_rect.center = (screen_width // 2, screen_height // 2) 

# Direction initialization
direction = "forward"
last_direction = "forward"

def calculate_distance(player, square):
    dx = player.centerx - square.centerx
    dy = player.centery - square.centery
    return (dx ** 2 + dy ** 2) ** 0.5

#function to calculate the distance between the cursor
def calculate_angle(player_pos, mouse_pos):
    dx = mouse_pos[0] - player_pos[0]
    dy = mouse_pos[1] - player_pos[1]
    angle = math.atan2(dy, dx)
    return angle

def update_bow(player_rect, mouse_pos):
    angle = calculate_angle(player_rect.center, mouse_pos)

    bow_x = player_rect.centerx + math.cos(angle) * bow_radius
    bow_y = player_rect.centery + math.sin(angle) * bow_radius

    bow_rotated = pygame.transform.rotate(bow_image, -math.degrees(angle))
    bow_rect = bow_rotated.get_rect(center=(bow_x, bow_y))

    return bow_rotated, bow_rect

def move_square(player, square):
    if player.x > square.x:
        square.x += enemy_speed
    elif player.x < square.x:
        square.x -= enemy_speed
    if player.y > square.y:
        square.y += enemy_speed
    elif player.y < square.y:
        square.y -= enemy_speed

#Animations for the player
def player_animation(moving, direction):
    global player_surf, player_index
    if moving:
        player_index += 0.1
        if direction == "right":
            if player_index >= len(player_walk_forward):
                player_index = 0
            player_surf = player_walk_forward[int(player_index)]
        elif direction == "left":
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

# ----------- Menu
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
                pygame.mouse.set_visiblde(True)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                game_state = "running"
                pygame.mouse.set_visible(False)
            if game_state == "running":
                if pause_button_rect.collidepoint(event.pos):
                    game_state = "menu"
                    pygame.mouse.set_visible(True)
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

    def check_collision(player_rect, tilemap_data):
        player_x, player_y = player_rect.topleft
        tile_x = player_x // tile_size
        tile_y = player_y // tile_size

        if tile_x < 0 or tile_x >= len(tilemap_data[0]) or tile_y < 0 or tile_y >= len(tilemap_data):
            return True
        return tilemap_data[tile_y][tile_x] == 1

    keys = pygame.key.get_pressed()
    moving = False
    direction = last_direction 

    # Movement input (Player keys)
    dx, dy = 0, 0  # Start with no movement

    if keys[pygame.K_w]:  # Move up
        dy -= player_speed
    if keys[pygame.K_s]:  # Move down
        dy += player_speed
    if keys[pygame.K_a]:  # Move left
        dx -= player_speed
    if keys[pygame.K_d]:  # Move right
        dx += player_speed

    # Adjust for diagonal movement (so the player doesn't move faster diagonally)
    if dx != 0 and dy != 0:
        diagonal_speed = player_speed / math.sqrt(2)  # Normalize diagonal movement speed
        dx = int(dx / abs(dx) * diagonal_speed)
        dy = int(dy / abs(dy) * diagonal_speed)

    # Calculate the new player position
    new_rect = player_rect.move(dx, dy)

    # Check if the new position causes a collision
    if not check_collision(new_rect, tilemap_data):
        player_rect = new_rect  # Update player position if no collision
        moving = True  # Player is moving

        # Determine direction based on movement
        if dx > 0 and dy < 0:
            direction = "right_up"
        elif dx > 0 and dy > 0:
            direction = "right_down"
        elif dx < 0 and dy < 0:
            direction = "left_up"
        elif dx < 0 and dy > 0:
            direction = "left_down"
        elif dx > 0:
            direction = "right"
        elif dx < 0:
            direction = "left"
        elif dy < 0:
            direction = "up"
        elif dy > 0:
            direction = "down"

    if not moving:
        direction = last_direction

    camera_x = player_rect.x - (screen_width // 2)
    camera_y = player_rect.y - (screen_height // 2)

    screen.fill(white)
    for y, row in enumerate(tilemap_data):
        for x, tile in enumerate(row):
            if tile != 0:
                draw_tile(x, y, tile, camera_x, camera_y)

    player_animation(moving, direction)
    
    # screen.blit(player_surf, player_rect.move(-camera_x, -camera_y).topleft)
    # pygame.draw.rect(screen, (255, 0, 0), player_rect.move(-camera_x, -camera_y), 2)
    
    player_rect = player_surf.get_rect(center=player_rect.center)

    distance = calculate_distance(player_rect, enemy_square)
    if distance < enemy_detection:
        move_square(player_rect, enemy_square)
    pygame.draw.rect(screen, (255, 0, 0), enemy_square.move(-camera_x, -camera_y))

    crosshair_rect.center = mouse_pos
    screen.blit(crosshair, crosshair_rect)

    pygame.draw.rect(screen, black, health_surface_border)
    pygame.draw.rect(screen, red, health_bar)
    screen.blit(pause_button, pause_button_rect)

    bow_rotated, bow_rect = update_bow(player_rect, mouse_pos)
    
    player_rect = player_surf.get_rect(center=player_rect.center)
    pygame.draw.rect(screen, (255, 0, 0), (player_rect.centerx - camera_x - 2, player_rect.centery - camera_y - 2, 4, 4))
    pygame.draw.rect(screen, (0, 255, 0), player_rect.move(-camera_x, -camera_y), 2)

    screen.blit(player_surf, player_rect.move(-camera_x, -camera_y).topleft)
    screen.blit(bow_rotated, bow_rect.move(-camera_x, -camera_y).topleft)

    # Draw the red square at the center of the player_rect
    pygame.draw.rect(screen, (255, 0, 0), (player_rect.centerx - 2, player_rect.centery - 2, 4, 4))
    pygame.draw.rect(screen, (0, 255, 0), player_rect, 2)
    
    pygame.display.flip()
    clock.tick(60) 