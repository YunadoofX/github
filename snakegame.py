import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")
clock = pygame.time.Clock()

# Snake starting point
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# Food position
food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, (*block, BLOCK_SIZE, BLOCK_SIZE))

def move_snake(snake, direction):
    x, y = snake[0]
    if direction == "UP":
        y -= BLOCK_SIZE
    elif direction == "DOWN":
        y += BLOCK_SIZE
    elif direction == "LEFT":
        x -= BLOCK_SIZE
    elif direction == "RIGHT":
        x += BLOCK_SIZE
    new_head = (x, y)
    snake.insert(0, new_head)
    return snake

def check_collision(snake):
    head = snake[0]
    # Wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Self collision
    if head in snake[1:]:
        return True
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move snake
    snake = move_snake(snake, direction)

    # Check if snake ate the food
    if snake[0] == food:
        food = (random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE))
    else:
        snake.pop()

    # Game over check
    if check_collision(snake):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    pygame.draw.rect(screen, RED, (*food, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

    clock.tick(10)  # Adjust speed (higher = faster)
