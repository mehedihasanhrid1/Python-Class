import pygame
import sys

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Rectangle with Pagame")

BLACK = (0,0,0)
BLUE = (0,0,255)

RECT_X = 150
RECT_Y = 100

RECT_WIDTH = 300
RECT_HEIGHT = 150

running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(screen, BLUE, (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
    
    pygame.display.update()
    
pygame.quit()
sys.exit()

