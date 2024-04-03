
import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set display dimensions
display_width = 800
display_height = 600

# Set size of each block in the grid
block_size = 20

# Initialize display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Set clock for controlling game speed
clock = pygame.time.Clock()

# Define font for displaying messages
font = pygame.font.SysFont(None, 25)

# Define levels
levels = [
    {"speed": 10, "initial_length": 1, "food_frequency": 0.1, "map": [(10, 10), (15, 15), (20, 20)]},  # Level 1
    {"speed": 15, "initial_length": 1, "food_frequency": 0.15, "map": [(5, 5), (10, 10), (15, 15)]}, # Level 2
    {"speed": 20, "initial_length": 1, "food_frequency": 0.2, "map": [(2, 2), (4, 4), (6, 6)]}        # Level 3
]

def drawGrid():
    # Draw grid lines
    for x in range(0, display_width, block_size):
        pygame.draw.line(gameDisplay, BLACK, (x,0), (x,display_height))
    for y in range(0, display_height, block_size):
        pygame.draw.line(gameDisplay, BLACK, (0,y), (display_width,y))

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 6, display_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    level = 0  # Start at Level 0
    snake_speed = levels[level]["speed"]
    snake_length = levels[level]["initial_length"]
    food_frequency = levels[level]["food_frequency"]
    current_map = levels[level]["map"]

    # Set initial position of the snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Set initial movement direction of the snake
    lead_x_change = 0
    lead_y_change = 0

    # Set initial position of the food
    rand_food_x, rand_food_y = random.choice(current_map)
    rand_food_x *= block_size  # Adjust food position to align with the grid
    rand_food_y *= block_size

    # Initialize score
    score = 0

    snake_list = []  # Initialize snake list

    while not game_over:

        while game_close == True:
            gameDisplay.fill(WHITE)
            message_to_screen("Game over, press C to play again or Q to quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            game_close = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(WHITE)
        drawGrid()
        pygame.draw.rect(gameDisplay, GREEN, [rand_food_x, rand_food_y, block_size, block_size])

        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head.copy())  # Append a copy of the snake's head position

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        for segment in snake_list:
            pygame.draw.rect(gameDisplay, BLACK, [segment[0], segment[1], block_size, block_size])

        # Display score
        score_text = font.render("Score: " + str(score), True, BLACK)
        gameDisplay.blit(score_text, [10, 10])

        pygame.display.update()

        # Check if snake has eaten the food
        if lead_x == rand_food_x and lead_y == rand_food_y:
            current_map.remove((rand_food_x // block_size, rand_food_y // block_size))  # Remove eaten food position from map
            if not current_map:  # Check if all food positions have been eaten
                current_map = levels[level]["map"][:]  # Reset map
            rand_food_x, rand_food_y = random.choice(current_map)
            rand_food_x *= block_size  # Adjust food position to align with the grid
            rand_food_y *= block_size
            snake_length += 1
            score += 1

        # Update snake speed and food frequency based on the level
        snake_speed = levels[level]["speed"]
        food_frequency = levels[level]["food_frequency"]

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
