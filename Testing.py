import pygame
from Config import *
import sys
import random
import math
import time

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

# Initialize Pygame mixer
pygame.mixer.init()

# List of MP3 file paths
music_tracks = [
    "Music\mp3\Medieval Vol. 2 1 (Loop).mp3",
    "mMusic\mp3\Medieval Vol. 2 2 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 3 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 4 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 5 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 6 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 7 (Loop).mp3",
    "Music\mp3\Medieval Vol. 2 8 (Loop).mp3"
]

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
player_rect = player_surf.get_rect(center=(400, 300))

player_center_x = player_rect.centerx
player_center_y = player_rect.centery

player_rect.center = (screen_width // 2, screen_height // 2) 

# Direction initialization
direction = "forward"
last_direction = "forward"

def get_bow_position(player_rect, bow_distance, angle):
    bow_x = player_rect.centerx + bow_distance * math.cos(angle)
    bow_y = player_rect.centery + bow_distance * math.sin(angle)
    return bow_x, bow_y

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
    global player_surf, player_index, last_direction

    if moving:
        player_index += 0.1
        if player_index >= len(player_walk_forward):
            player_index = 0

        if direction == "right":
            player_surf = player_walk_forward[int(player_index)]
        elif direction == "left":
            player_surf = player_walk_back[int(player_index)]
        elif direction == "right_up":
            player_surf = player_walk_right_up[int(player_index)]
        elif direction == "right_down":
            player_surf = player_walk_right_down[int(player_index)]
        elif direction == "left_up":
            player_surf = player_walk_left_up[int(player_index)]
        elif direction == "left_down":
            player_surf = player_walk_left_down[int(player_index)]
        elif direction == "up":
            player_surf = player_walk_up[int(player_index)]
        elif direction == "down":
            player_surf = player_walk_down[int(player_index)]
        
        last_direction = direction
    
    else:
        # Set the idle frame to the first frame of the last direction
        if last_direction == "right":
            player_surf = player_walk_forward[0]
        elif last_direction == "left":
            player_surf = player_walk_back[0]
        elif last_direction == "right_up":
            player_surf = player_walk_right_up[0]
        elif last_direction == "right_down":
            player_surf = player_walk_right_down[0]
        elif last_direction == "left_up":
            player_surf = player_walk_left_up[0]
        elif last_direction == "left_down":
            player_surf = player_walk_left_down[0]
        elif last_direction == "up":
            player_surf = player_walk_up[0]
        elif last_direction == "down":
            player_surf = player_walk_down[0]

def draw_tile(x, y, tile_index, camera_x, camera_y):
    screen.blit(tile_images[tile_index], (x * tile_size - camera_x, y * tile_size - camera_y))

class Arrow:
    def __init__(self, x, y, angle):
        self.image = pygame.image.load('Assets/Bow/bow_3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 10))  
        self.angle = angle
        self.speed = 10
        self.damage = arrow_damage # sets the arrow damage
        self.rect = self.image.get_rect(center=(x, y))
        self.vel_x = self.speed * math.cos(angle)
        self.vel_y = self.speed * math.sin(angle)
        self.rotated_image = pygame.transform.rotate(self.image, -math.degrees(angle))
        self.rect = self.rotated_image.get_rect(center=self.rect.center)
        
    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.rotated_image, (self.rect.x - camera_x, self.rect.y - camera_y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect.move(-camera_x, -camera_y), 2)

class Enemy:
    def __init__(self, x, y):
        self.health = random.uniform(50, 100)  # Health between 50% and 100%
        self.attack_damage = random.uniform(5, 20)  # Attack damage between 5% and 20%
        self.speed = random.uniform(1, 2)  # Speed between 1 and 4
        self.rect = pygame.Rect(x, y, enemy_size, enemy_size)
        
        self.right_frames = [
            pygame.image.load('Assets/enemies/walkright1.png').convert_alpha(),
            pygame.image.load('Assets/enemies/walkright2.png').convert_alpha()
        ]
        self.left_frames = [
            pygame.image.load('Assets/enemies/walkleft1.png').convert_alpha(),
            pygame.image.load('Assets/enemies/walkleft2.png').convert_alpha()
        ]

        self.direction = "right"
        self.animation_index = 0
        self.animation_speed = 0.1
        self.image = self.right_frames[self.animation_index]
        self.detection_radius = 200

        self.last_attack_time = 0
        self.attack_cooldown = 1  # 1 second cooldown

    def attack_player(self, player_rect):
        global player_health
        current_time = time.time()
        if self.rect.colliderect(player_rect) and current_time - self.last_attack_time > self.attack_cooldown:
            player_health -= self.attack_damage
            update_health_bar()  # Update the health bar
            self.last_attack_time = current_time
            print(f"Player took {self.attack_damage:.2f} damage! Health: {player_health:.2f}")
            if player_health <= 0:

                game_over()

    def check_enemy_collision(self, enemies):
        for enemy in enemies:
            if enemy != self:
                distance = self.rect.colliderect(enemy.rect)
                if distance:
                    if self.rect.centerx < enemy.rect.centerx:
                        self.rect.x -= self.speed
                    else:
                        self.rect.x += self.speed
                    if self.rect.centery < enemy.rect.centery:
                        self.rect.y -= self.speed
                    else:
                        self.rect.y += self.speed

    def animate(self):
        self.animation_index += self.animation_speed
        if self.animation_index >= 2:
            self.animation_index = 0

        if self.direction == "right":
            self.image = self.right_frames[int(self.animation_index)]
        elif self.direction == "left":
            self.image = self.left_frames[int(self.animation_index)]

    def move_towards(self, target_rect):
        if self.rect.x < target_rect.x:
            self.rect.x += self.speed
            self.direction = "right"
        elif self.rect.x > target_rect.x:
            self.rect.x -= self.speed
            self.direction = "left"
        
        if self.rect.y < target_rect.y:
            self.rect.y += self.speed
        elif self.rect.y > target_rect.y:
            self.rect.y -= self.speed
        
        self.check_enemy_collision(enemies)
        self.animate()

    def draw(self, screen, camera_x, camera_y, player_rect):
        screen.blit(self.image, self.rect.move(-camera_x, -camera_y))
        pygame.draw.rect(screen, (255, 0, 0), self.rect.move(-camera_x, -camera_y), 2)
        pygame.draw.circle(
            screen, (0, 255, 0), 
            (self.rect.centerx - camera_x, self.rect.centery - camera_y), 
            self.detection_radius, 1
        )

    def is_player_in_radius(self, player_rect):
        distance = math.sqrt(
            (self.rect.centerx - player_rect.centerx) ** 2 +
            (self.rect.centery - player_rect.centery) ** 2
        )
        return distance < self.detection_radius

def update_health_bar():
    health_ratio = player_health / player_max_health
    health_bar.width = int(200 * health_ratio)

def game_over():
    global game_state
    if game_state != "death_screen":  # Prevent repeated calls
        print("Player died. Returning to menu...")
        pygame.time.wait(1000)
        game_state = "death_screen"
        pygame.mouse.set_visible(True)

def restart_game():
    global game_state, player_health, enemies, arrows, wave_number, enemies_per_wave
    player_health = 100  # Reset health
    game_state = "running"  # Set game back to running
    arrows.clear()  # Remove arrows
    enemies.clear()  # Remove enemies
    for _ in range(enemies_per_wave):  # Spawn enemies for the current wave
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        enemies.append(Enemy(x, y))
    wave_number = 1  # Reset wave number to 1
    pygame.mouse.set_visible(False)

def check_wave_status():
    global wave_number, enemies_per_wave
    if len(enemies) == 0:  # All enemies are killed
        wave_number += 1  # Increase wave number
        enemies_per_wave += 2  # Increase enemies per wave (adjust as needed)
        for _ in range(enemies_per_wave):  # Spawn new enemies
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            enemies.append(Enemy(x, y))

class Hearts:
    def __init__(self, x, y):
        self.image = pygame.image.load("Assets\heart.png")  # Placeholder for heart image
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.image, (self.rect.x - camera_x, self.rect.y - camera_y))

# List to store hearts
hearts_list = []

# Function to spawn a heart at a random position
def spawn_heart():
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    hearts_list.append(Hearts(x, y))

# Function to play a random track
def play_random_music():
    track = random.choice(music_tracks)
    print("Music Is Playing")
    pygame.mixer.music.fadeout(1000)  # Fade out the current track over 1 second
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1, fade_ms=1000)  # Fade in new track over 1 second
    pygame.mixer.music.set_volume(music_volume)  # Set volume

# Function to check and play new music after the current one finishes
def check_and_play_music():
    if not pygame.mixer.music.get_busy():  # Check if the current track is finished
        play_random_music()  # Play a new random track

# Call play_random_music() to start the first track when the game starts
play_random_music()

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
player_index = 0  
arrows = []

enemies = []
for _ in range(5): 
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    enemies.append(Enemy(x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        check_and_play_music()
        
        # Spawn hearts randomly (~1 in 600 chance per frame, about every 10 seconds)
        if random.randint(1, 600) == 1:
            spawn_heart()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state == "running":
                background_color = brown
                game_state = "menu"
                pygame.mouse.set_visible(True)
                pygame.time.delay(200)  # Prevents accidental repeated triggering

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "running" and event.button == 1:  # Left-click to shoot
                mouse_x, mouse_y = pygame.mouse.get_pos()
                player_x, player_y = player_rect.centerx - camera_x, player_rect.centery - camera_y
                angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

                # Create a new arrow
                new_arrow = Arrow(player_rect.centerx, player_rect.centery, angle)
                arrows.append(new_arrow)
        
        if game_state == "death_screen":
            while game_state == "death_screen":
                screen.fill((0, 0, 0, 150))  # Semi-transparent background

                # Draw death menu UI
                pygame.draw.rect(screen, (50, 50, 50), (screen_width // 2 - 150, screen_height // 2 - 75, 300, 150), border_radius=10)

                # Display death text
                death_text = font.render("You Died..", True, (255, 0, 0))
                screen.blit(death_text, (screen_width // 2 - death_text.get_width() // 2, screen_height // 2 - 50))

                wave_text = font.render(f"Wave: {wave_number}", True, (255, 255, 255))
                screen.blit(wave_text, (screen_width // 2 - wave_text.get_width() // 2, screen_height // 2 - 10))

                # Display buttons
                restart_text = font.render("Restart", True, (255, 255, 255))
                quit_text = font.render("Quit", True, (255, 255, 255))

                restart_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 60, 200, 50)
                quit_rect = pygame.Rect(screen_width // 2 - 100, screen_height // 2 + 120, 200, 50)

                pygame.draw.rect(screen, (100, 100, 100), restart_rect, border_radius=5)
                pygame.draw.rect(screen, (100, 100, 100), quit_rect, border_radius=5)

                screen.blit(restart_text, (restart_rect.x + 50, restart_rect.y + 10))
                screen.blit(quit_text, (quit_rect.x + 65, quit_rect.y + 10))

                pygame.display.flip()  # Only update screen once per loop

                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if restart_rect.collidepoint(event.pos):
                            restart_game()
                        elif quit_rect.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()

                pygame.time.delay(100)  # Prevent high CPU usage & flickering

        # Handle Death Screen Clicks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    restart_game()
                elif quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

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

    for heart in hearts_list[:]:  # Iterate over a copy to safely remove items
        if player_rect.colliderect(heart.rect):
            heal_amount = random.randint(50, 100)  # Restore 50% to 100% health
            player_health = min(player_health + heal_amount, 100)  # Cap at 100%
            hearts_list.remove(heart)  # Remove heart after pickup

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

    dx, dy = 0, 0 

    # Movement keys
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
        dx = dx / abs(dx) * diagonal_speed if dx != 0 else 0
        dy = dy / abs(dy) * diagonal_speed if dy != 0 else 0

    new_x = player_rect.x + dx
    new_y = player_rect.y + dy
    new_rect = pygame.Rect(new_x, new_y, player_rect.width, player_rect.height)

    if not check_collision(new_rect, tilemap_data):  
        player_rect.x = new_x
        player_rect.y = new_y
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

    # Debug - Prints the player_index
    #print("Length of player_walk_forward:", len(player_walk_forward))
    #sprint("Current player_index:", int(player_index))

    # Update player sprite **before** calling animation
    player_surf = player_walk_forward[int(player_index)]  

    player_animation(moving, direction)

    screen.fill(white)
    for y, row in enumerate(tilemap_data):
        for x, tile in enumerate(row):
            if tile != 0:
                draw_tile(x, y, tile, camera_x, camera_y)    

    distance = calculate_distance(player_rect, enemy_square)
    if distance < enemy_detection:
        move_square(player_rect, enemy_square)
        
    crosshair_rect.center = mouse_pos
    screen.blit(crosshair, crosshair_rect)

    pygame.draw.rect(screen, black, health_surface_border)
    pygame.draw.rect(screen, red, health_bar)
    screen.blit(pause_button, pause_button_rect)

    # Debugging Visuals
    pygame.draw.rect(screen, (255, 0, 0), (player_rect.centerx - camera_x - 2, player_rect.centery - camera_y - 2, 4, 4))
    pygame.draw.rect(screen, (0, 255, 0), player_rect.move(-camera_x, -camera_y), 2)

    for enemy in enemies:
        if enemy.is_player_in_radius(player_rect):
            enemy.move_towards(player_rect)
        enemy.draw(screen, camera_x, camera_y, player_rect)

    screen.blit(player_surf, player_rect.move(-camera_x, -camera_y).topleft)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    player_x, player_y = player_rect.centerx - camera_x, player_rect.centery - camera_y
    angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

    # Calculate bow position
    bow_distance = 40
    bow_x, bow_y = get_bow_position(player_rect, bow_distance, angle)
    rotated_bow = pygame.transform.rotate(bow_image, -math.degrees(angle))
    bow_rect = rotated_bow.get_rect(center=(bow_x - camera_x, bow_y - camera_y))

    # Draw bow
    screen.blit(rotated_bow, bow_rect.topleft)
    pygame.draw.rect(screen, (255, 0, 0), (player_rect.centerx - camera_x - 2, player_rect.centery - camera_y - 2, 4, 4))
    pygame.draw.rect(screen, (0, 255, 0), player_rect.move(-camera_x, -camera_y), 2)

    # Render the wave number on the screen
    wave_text = font.render(f"Wave: {wave_number}", True, (0, 0, 0))  # Black color
    text_width = wave_text.get_width()
    screen.blit(wave_text, ((screen_width // 2) - (text_width // 2), 10))  # positioning of the counter

    for heart in hearts_list:
        heart.draw(screen, camera_x, camera_y)

    for enemy in enemies:
        if enemy.is_player_in_radius(player_rect):
            enemy.move_towards(player_rect)
            enemy.attack_player(player_rect)
        enemy.draw(screen, camera_x, camera_y, player_rect)

    for arrow in arrows[:]:
        arrow.update()
        arrow.draw(screen, camera_x, camera_y)

        # Check for arrow and enemy collision
        for enemy in enemies[:]:
            # Removes the arrow after it hits the enemy
            if arrow.rect.colliderect(enemy.rect):
                enemy.health -= arrow.damage
                arrows.remove(arrow)
                # Deletes the enemy if the health gets to 0 
                if enemy.health <= 0:
                    enemies.remove(enemy) 
                    print("Enemy killed")
                
                break
        # After the enemy code, check for wave status
        check_wave_status()

        # deeletes the arrow if it gets out of the screen.
        if arrow.rect.right < 0 or arrow.rect.left > screen_width or arrow.rect.bottom < 0 or arrow.rect.top > screen_height:
            arrows.remove(arrow)

    pygame.display.flip()
    clock.tick(60)