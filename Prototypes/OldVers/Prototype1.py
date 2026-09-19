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
# Walk Right
player_walk_1 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_0.png').convert_alpha()
player_walk_2 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_1.png').convert_alpha()
player_walk_3 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_2.png').convert_alpha()
player_walk_4 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_3.png').convert_alpha()
player_walk_5 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_4.png').convert_alpha()
player_walk_6 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_5.png').convert_alpha()
player_walk_7 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_6.png').convert_alpha()
player_walk_8 = pygame.image.load('Player Assets\Walk Right Down\images\walk_right_down_7.png').convert_alpha()

# Right Up
player_walk_rightup_1 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_0.png').convert_alpha()
player_walk_rightup_2 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_1.png').convert_alpha()
player_walk_rightup_3 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_2.png').convert_alpha()
player_walk_rightup_4 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_3.png').convert_alpha()
player_walk_rightup_5 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_4.png').convert_alpha()
player_walk_rightup_6 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_5.png').convert_alpha()
player_walk_rightup_7 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_6.png').convert_alpha()
player_walk_rightup_8 = pygame.image.load('Player Assets\Walk Right Up\images\walk_right_up_7.png').convert_alpha()

# Right Down
player_walk_down_1 = pygame.image.load('Player Assets\Walk Down\images\walk_down_0.png').convert_alpha()
player_walk_down_2 = pygame.image.load('Player Assets\Walk Down\images\walk_down_1.png').convert_alpha()
player_walk_down_3 = pygame.image.load('Player Assets\Walk Down\images\walk_down_2.png').convert_alpha()
player_walk_down_4 = pygame.image.load('Player Assets\Walk Down\images\walk_down_3.png').convert_alpha()
player_walk_down_5 = pygame.image.load('Player Assets\Walk Down\images\walk_down_4.png').convert_alpha()
player_walk_down_6 = pygame.image.load('Player Assets\Walk Down\images\walk_down_5.png').convert_alpha()
player_walk_down_7 = pygame.image.load('Player Assets\Walk Down\images\walk_down_6.png').convert_alpha()
player_walk_down_8 = pygame.image.load('Player Assets\Walk Down\images\walk_down_7.png').convert_alpha()

# Walk Left
player_walk_back_1 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_0.png').convert_alpha()
player_walk_back_2 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_1.png').convert_alpha()
player_walk_back_3 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_2.png').convert_alpha()
player_walk_back_4 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_3.png').convert_alpha()
player_walk_back_5 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_4.png').convert_alpha()
player_walk_back_6 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_5.png').convert_alpha()
player_walk_back_7 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_6.png').convert_alpha()
player_walk_back_8 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_7.png').convert_alpha()

# Left Up
player_walk_leftup_1 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_0.png').convert_alpha()
player_walk_leftup_2 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_1.png').convert_alpha()
player_walk_leftup_3 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_2.png').convert_alpha()
player_walk_leftup_4 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_3.png').convert_alpha()
player_walk_leftup_5 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_4.png').convert_alpha()
player_walk_leftup_6 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_5.png').convert_alpha()
player_walk_leftup_7 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_6.png').convert_alpha()
player_walk_leftup_8 = pygame.image.load('Player Assets\Walk Left Up\images\walk_left_up_7.png').convert_alpha()

# Left Down
player_walk_leftdown_1 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_0.png').convert_alpha()
player_walk_leftdown_2 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_1.png').convert_alpha()
player_walk_leftdown_3 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_2.png').convert_alpha()
player_walk_leftdown_4 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_3.png').convert_alpha()
player_walk_leftdown_5 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_4.png').convert_alpha()
player_walk_leftdown_6 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_5.png').convert_alpha()
player_walk_leftdown_7 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_6.png').convert_alpha()
player_walk_leftdown_8 = pygame.image.load('Player Assets\Walk Down Left\images\walk_left_down_7.png').convert_alpha()

# Up
player_walk_up_1 = pygame.image.load('Player Assets\Walk Up\images\walk_up_0.png').convert_alpha()
player_walk_up_2 = pygame.image.load('Player Assets\Walk Up\images\walk_up_1.png').convert_alpha()
player_walk_up_3 = pygame.image.load('Player Assets\Walk Up\images\walk_up_2.png').convert_alpha()
player_walk_up_4 = pygame.image.load('Player Assets\Walk Up\images\walk_up_3.png').convert_alpha()
player_walk_up_5 = pygame.image.load('Player Assets\Walk Up\images\walk_up_4.png').convert_alpha()
player_walk_up_6 = pygame.image.load('Player Assets\Walk Up\images\walk_up_5.png').convert_alpha()
player_walk_up_7 = pygame.image.load('Player Assets\Walk Up\images\walk_up_6.png').convert_alpha()
player_walk_up_8 = pygame.image.load('Player Assets\Walk Up\images\walk_up_7.png').convert_alpha()

# Down
player_walk_down_1 = pygame.image.load('Player Assets\Walk Down\images\walk_down_0.png').convert_alpha()
player_walk_down_2 = pygame.image.load('Player Assets\Walk Down\images\walk_down_1.png').convert_alpha()
player_walk_down_3 = pygame.image.load('Player Assets\Walk Down\images\walk_down_2.png').convert_alpha()
player_walk_down_4 = pygame.image.load('Player Assets\Walk Down\images\walk_down_3.png').convert_alpha()
player_walk_down_5 = pygame.image.load('Player Assets\Walk Down\images\walk_down_4.png').convert_alpha()
player_walk_down_6 = pygame.image.load('Player Assets\Walk Down\images\walk_down_5.png').convert_alpha()
player_walk_down_7 = pygame.image.load('Player Assets\Walk Down\images\walk_down_6.png').convert_alpha()
player_walk_down_8 = pygame.image.load('Player Assets\Walk Down\images\walk_down_7.png').convert_alpha()

# Bow -----------------------------------
bow_1 = pygame.image.load('Assets/Bow 1.png').convert_alpha()

# Player Initial Position
player_rect = player_walk_down_1.get_rect(center=(screen_width // 2, screen_height // 2))
player_speed = 5

# Initialize player movement
last_direction = "down"
moving = False

# Bow radius (distance from player to bow)
bow_radius = 40

# Function to calculate angle between player and mouse
def calculate_angle(player_pos, mouse_pos):
    dx = mouse_pos[0] - player_pos[0]
    dy = mouse_pos[1] - player_pos[1]
    angle = math.atan2(dy, dx)  # Get angle in radians
    return angle

# Function to update bow position and rotation
def update_bow(player_rect, mouse_pos):
    angle = calculate_angle(player_rect.center, mouse_pos)

    # Calculate the new position of the bow based on the angle
    bow_x = player_rect.centerx + math.cos(angle) * bow_radius
    bow_y = player_rect.centery + math.sin(angle) * bow_radius

    # Create a rotated version of the bow that faces the mouse cursor
    bow_rotated = pygame.transform.rotate(bow_1, math.degrees(angle))  # Convert angle to degrees

    # Get the new rectangle for the rotated bow
    bow_rect = bow_rotated.get_rect(center=(bow_x, bow_y))

    return bow_rotated, bow_rect

# Game loop
game_state = "menu"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == "running":
                background_color = brown
                game_state = "menu"
                pygame.mouse.set_visible(True)

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

    dx, dy = 0, 0

    if keys[pygame.K_w]:  # Move up
        dy -= player_speed
    if keys[pygame.K_s]:  # Move down
        dy += player_speed
    if keys[pygame.K_a]:  # Move left
        dx -= player_speed
    if keys[pygame.K_d]:  # Move right
        dx += player_speed

    if dx != 0 and dy != 0:
        diagonal_speed = player_speed / math.sqrt(2)
        dx = int(dx / abs(dx) * diagonal_speed)
        dy = int(dy / abs(dy) * diagonal_speed)

    if dx != 0 or dy != 0:
        new_rect = player_rect.move(dx, dy)
        if not check_collision(new_rect, tilemap_data):
            player_rect = new_rect
            moving = True

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

    # Fill screen and draw tiles
    screen.fill(white)
    for y, row in enumerate(tilemap_data):
        for x, tile in enumerate(row):
            if tile != 0:
                draw_tile(x, y, tile, camera_x, camera_y)

    # Animate player movement
    player_animation(moving, direction)
    screen.blit(player_surf, player_rect.move(-camera_x, -camera_y).topleft)

    # Update the bow position and draw it
    bow_rotated, bow_rect = update_bow(player_rect, mouse_pos)
    screen.blit(bow_rotated, bow_rect.move(-camera_x, -camera_y).topleft)

    pygame.draw.rect(screen, black, health_surface_border)
    pygame.draw.rect(screen, red, health_bar)

    pygame.display.flip()
    clock.tick(60)
