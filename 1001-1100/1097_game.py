import pygame
import random
import sys

pygame.init()
WIDTH, HEIGHT = 400, 300
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")
font = pygame.font.SysFont(None, 32)

def draw_text(text, y):
    txt = font.render(text, True, BLACK)
    rect = txt.get_rect(center=(WIDTH // 2, y))
    screen.blit(txt, rect)

def main():
    number = random.randint(1, 10)
    attempts, input_text, guessed = 0, '', False
    message = "Guess a number between 1 and 10!"
    clock = pygame.time.Clock()
    while True:
        screen.fill(WHITE)
        draw_text(message, 50)
        draw_text(f"Your guess: {input_text}", 120)
        if guessed:
            draw_text(f"Guessed in {attempts} attempts!", 200)
            draw_text("Press R to restart", 240)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if guessed and event.key == pygame.K_r:
                    number, attempts, input_text, guessed = random.randint(1, 10), 0, '', False
                    message = "Guess a number between 1 and 10!"
                elif not guessed:
                    if event.key == pygame.K_RETURN:
                        try:
                            guess = int(input_text)
                            attempts += 1
                            if guess < number: message = "Too low!"
                            elif guess > number: message = "Too high!"
                            else: message, guessed = "Congratulations!", True
                        except ValueError:
                            message = "Enter a valid integer."
                        input_text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif event.unicode.isdigit():
                        input_text += event.unicode
        clock.tick(30)

if __name__ == "__main__":
    main()
