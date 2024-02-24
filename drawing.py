"""
Q - clear canvas
LEFT MOUSE - draw
A - increase font size
D - decrease font size
"""
import pygame
import numpy as np
from main import model
import random
import time
import threading


pygame.init()
WIDTH = 560
HEIGHT = 560
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 500
fuld = np.zeros((28, 28))
interval = 0.1    # frequency of model prediction in seconds

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


font = pygame.font.Font("freesansbold.ttf", 32)
random_color = False


def predict_and_display():
    global screen, fuld, font
    pred = model.predict(np.expand_dims(fuld, axis=0))
    pygame.display.set_caption(f"It's {str(np.argmax(pred))}")
    
def draw_grid():
    for x in range(0, WIDTH, 20):  # Рисуем вертикальные линии
        pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 20):  # Рисуем горизонтальные линии
        pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y))


def main():
    global fuld, interval
    field = np.zeros((28, 28), dtype=bool)
    font_size = 20
    draw = False
    change_font = 0
    
    clock = pygame.time.Clock()

    def predict_loop():
        while True:
            predict_and_display()
            time.sleep(interval)

    predict_thread = threading.Thread(target=predict_loop)
    predict_thread.daemon = True
    predict_thread.start()
    
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                draw = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                field = np.zeros((28, 28))
                fuld = np.zeros((28, 28))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                change_font = 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                change_font = -1
            if event.type == pygame.KEYUP and (event.key == pygame.K_a or event.key == pygame.K_d):
                change_font = 0

        screen.fill(BLACK)

        if change_font == 1 and font_size <= 50:
            font_size += 0.2
        elif change_font == -1 and font_size >= 2:
            font_size -= 0.2

        if draw:
            grid_x = mx // 20
            grid_y = my // 20
            if 0 <= grid_x < 28 and 0 <= grid_y < 28:
                field[grid_y][grid_x] = True
                fuld[my // 20][mx // 20] = 1
        
        for y in range(28):
            for x in range(28):
                if field[y][x]:
                    square_rect = pygame.Rect(x * 20, y * 20, 20, 20)
                    pygame.draw.rect(screen, WHITE, square_rect)
                        
        start_text = font.render(f"{str(int(clock.get_fps()))} FPS", False, GREEN)
        screen.blit(start_text, (0, 0))
        draw_grid()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
