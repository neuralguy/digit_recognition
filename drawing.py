import pygame
import numpy as np
from main import model


WIDTH = 280
HEIGHT = 280
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing")
clock = pygame.time.Clock()
FPS = 300

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font_size = 10


def main():
    field = []
    fuld = np.zeros((28, 28))
    draw = False
    clear = False
    while True:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    draw = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    draw = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    clear = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    clear = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    field.clear()
                    fuld = np.zeros((28, 28))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    pred = model.predict(np.expand_dims(fuld, axis=0))
                    print(f"Это цифра {np.argmax(pred)}")

        screen.fill(BLACK)

        if draw:
            field.append([mx, my])
            fuld[my // 10][mx // 10] = 1
        if clear:
            for i in field:
                if pygame.rect.Rect(i[0], i[1], font_size * 2, font_size * 2).collidepoint([mx, my]):
                    try:
                        field.remove(i)
                    except:
                        pass
        for i in field:
            pygame.draw.line(screen, WHITE, [int(i[0]), int(i[1])], [int(i[0]), int(i[1])])
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
