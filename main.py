import pygame
# Инициализация на Pygame
pygame.init()

# Настройки на екрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Memory Game")

# Цветове
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (170, 170, 170)

# Размери на квадратите
square_size = 100
margin = 10

# Генериране на позиции за квадратите
def generate_positions(rows, cols, square_size, margin):
    positions = []
    for row in range(rows):
        for col in range(cols):
            x = col * (square_size + margin) + margin
            y = row * (square_size + margin) + margin
            positions.append((x, y))
    return positions

# Основна логика на играта
def main():
    running = True
    positions = generate_positions(4, 6, square_size, margin)  # 4 реда и 6 колони
    clicked_squares = [False] * 24  # Списък за следене на състоянието на квадратите

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                for i, pos in enumerate(positions):
                    x, y = pos
                    if x < mouse_x < x + square_size and y < mouse_y < y + square_size:
                        clicked_squares[i] = not clicked_squares[i]

        screen.fill(WHITE)

        # Рисуване на квадратите
        for i, pos in enumerate(positions):
            color = LIGHT_GRAY if clicked_squares[i] else GRAY
            pygame.draw.rect(screen, color, (*pos, square_size, square_size))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()