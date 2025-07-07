import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

enemy_size = 40
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 0
enemy_speed = 3

clock = pygame.time.Clock()

score = 0
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y):
    img = font.render(text, True, BLUE)
    screen.blit(img, (x, y))


running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 0
        enemy_x = random.randint(0, WIDTH - enemy_size)
        score += 1


    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        draw_text("Game Over!", WIDTH // 2 - 80, HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()