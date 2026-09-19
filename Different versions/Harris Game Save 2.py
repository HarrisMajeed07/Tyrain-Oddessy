import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
game_active = True
screen_width = 800
screen_height = 400
font = pygame.font.Font('Fonts\Pixeltype.ttf', 36)
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 2
screen = pygame.display.set_mode((screen_width, screen_height))

if game_active:
    pygame.display.set_caption("Tyrain Oddessy")

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
            player_surf = player_idle[int(player_index)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

keys = pygame.key.get_pressed()
moving = False

if keys[pygame.K_w]:
    player_rect.y -= player_speed
    moving = True
if keys[pygame.K_a]:
    player_rect.x -= player_speed
    moving = True
    direction = "backward"
if keys[pygame.K_s]:
    player_rect.y += player_speed
    moving = True
if keys[pygame.K_d]:
    player_rect.x += player_speed
    moving = True
    direction = "forward"

screen.fill((0, 0, 0))
player_animation(moving, direction)
screen.blit(player_surf, player_rect)

pygame.display.flip()
pygame.display.update()
clock.tick(60)