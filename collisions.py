# Showing how to detect collisions between two rectangles in Pygame
# Version 1: Using the colliderect method
# Version 2: Using the sprite group collision detection
# Version 3: Using the sprite group collision detection with a custom method
# Removing a sprite from a sprite group
# Removing 1 life from the player when a collision is detected
# Date: 2024-08-20
# Author: Juergen Lier

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

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Prevent player from moving off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
   
# Enemy sprite setup
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
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

# Create sprite group for enemies
enemies = pygame.sprite.Group()
enemy = Enemy(300, 300)
enemies.add(enemy)  # Add enemy to sprite group

# Player lives setup
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


    '''# Check for collision (Version 1)
    if enemy_active and player.colliderect(enemy):
        player_lives -= 1
        enemy_active = False
        print(f"Lives left: {player_lives}")
        if player_lives <= 0:
            print("Game Over")
            running = False
    
    enemy_active = True'''

    '''# Check for collision with sprite group (Version 2)
    for enemy in enemies:
        if player.colliderect(enemy.rect):
            player_lives -= 1
            print(f"Lives left: {player_lives}")
            enemies.remove(enemy) # Remove enemy from sprite group
            if player_lives <= 0:
                print("Game Over")
                running = False'''

    # Check for collision with sprite group (Version 3)
    # This version uses the collision detection created in the Enemy class
    for enemy in enemies:
        enemy.check_collision(player)


    # Clear screen
    screen.fill((0, 0, 0))

    # Draw player and enemy
    pygame.draw.rect(screen, (0, 128, 255), player)
    
    # Draw enemies
    enemies.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
