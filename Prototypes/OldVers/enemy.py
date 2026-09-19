import pygame
from pygame.locals import *

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Animation Example")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Player animation setup
player_sprites = [
    pygame.Surface((50, 50), pygame.SRCALPHA),  # Placeholder frames
    pygame.Surface((50, 50), pygame.SRCALPHA),
    pygame.Surface((50, 50), pygame.SRCALPHA),
]
player_sprites[0].fill((255, 0, 0))
player_sprites[1].fill((0, 255, 0))
player_sprites[2].fill((0, 0, 255))

player_index = 0
player_pos = [WIDTH // 2, HEIGHT // 2]  # Player's position in the world
player_speed = 5

# Rect to follow the player animation
player_rect = player_sprites[0].get_rect(center=player_pos)

# Animation timing
ANIMATION_SPEED = 200  # Milliseconds per frame
last_update_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    screen.fill((30, 30, 30))

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        player_pos[1] -= player_speed
    if keys[K_DOWN]:
        player_pos[1] += player_speed
    if keys[K_LEFT]:
        player_pos[0] -= player_speed
    if keys[K_RIGHT]:
        player_pos[0] += player_speed

    # Update animation frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > ANIMATION_SPEED:
        player_index = (player_index + 1) % len(player_sprites)
        last_update_time = current_time

    # Update player_rect to follow the animation and player position
    player_rect = player_sprites[player_index].get_rect(center=player_pos)

    # Draw player animation
    screen.blit(player_sprites[player_index], player_rect.topleft)

    # Debugging: Draw the player_rect (outline)
    pygame.draw.rect(screen, (255, 255, 0), player_rect, 2)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()
