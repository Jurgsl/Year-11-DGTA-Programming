# Collision detection between player and enemy sprite
# Adding a platform to the game
# Date: 2024-08-20
# Author: Juergen Lier
# Version 1.0

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))

# Player sprite setup
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.gravity = 0.5
        self.velocity_y = 0
        self.jump_strength = -10
        self.on_ground = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Prevent player from moving off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.on_ground = True
            self.velocity_y = 0

    def check_collision_with_platform(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0: # Falling
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0

# Platform setup
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
   
# Enemy sprite setup
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 3
        self.gravity = 0.5
        self.velocity_y = 0
        self.on_ground = False

    def move_enemy(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False

        # Apply gravity
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # Prevent the enemy from moving off the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            self.on_ground = True
            self.velocity_y = 0
        
    def check_collision(self, player):
        global player_lives
        global running
        if self.rect.colliderect(player):
            player_lives -= 1
            print(f"Lives left: {player_lives}")
            enemies.remove(self)  # Remove enemy from sprite group
            if player_lives <= 0:
                print("Game Over")
                running = False
    
    def check_collision_with_platform(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0: # Falling
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0

# Create sprite group for enemies
enemies = pygame.sprite.Group()
enemy = Enemy(300, 300)
enemies.add(enemy)  # Add enemy to sprite group

# Create sprite group for platforms
platforms = pygame.sprite.Group()
platform = Platform(0, 550, 800, 50)
platforms.add(platform)  # Add platform to sprite group

player = Player(100,100)
player_lives = 3

# enemy_active = True

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calling the move method of the player
    player.move()
    player.check_collision_with_platform(platforms)

    # Calling the move method of the enemy
    enemy.move_enemy()
    enemy.check_collision_with_platform(platforms)

    # Check for collision with sprite group (Version 3)
    # This version uses the collision detection created in the Enemy class
    for enemy in enemies:
        enemy.check_collision(player)


    # Clear screen
    screen.fill((0, 0, 0))

    # Draw player, platforms and enemy
    screen.blit(player.image, player.rect)
    platforms.draw(screen)
    enemies.draw(screen)
    

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
