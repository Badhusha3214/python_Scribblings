import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game variables
width, height = 800, 600
cell_size = 20
snake_speed = 15

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Snake initial position and direction
snake = [(width // 2, height // 2)]
snake_direction = (cell_size, 0)

# Initial food position
food = (random.randrange(0, width, cell_size), random.randrange(0, height, cell_size))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Check for key presses to change snake direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, cell_size):
        snake_direction = (0, -cell_size)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -cell_size):
        snake_direction = (0, cell_size)
    elif keys[pygame.K_LEFT] and snake_direction != (cell_size, 0):
        snake_direction = (-cell_size, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-cell_size, 0):
        snake_direction = (cell_size, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    # Check for collisions with walls or itself
    if (
        new_head[0] < 0
        or new_head[0] >= width
        or new_head[1] < 0
        or new_head[1] >= height
        or new_head in snake
    ):
        pygame.quit()
        sys.exit()

    # Check for collision with food
    if new_head == food:
        snake.append(food)
        food = (random.randrange(0, width, cell_size), random.randrange(0, height, cell_size))
    else:
        snake.pop()

    # Update the snake
    snake.insert(0, new_head)

    # Draw everything
    screen.fill(black)
    for segment in snake:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))
    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Control the snake speed
    pygame.time.Clock().tick(snake_speed)
