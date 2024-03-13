import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 700
HEIGHT = 700
GRID_SIZE = 100
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Coin Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

# Font
FONT = pygame.font.Font(None, 36)

# Define the game board
def draw_board():
    for row in range(7):
        for col in range(7):
            pygame.draw.rect(SCREEN, GRAY, (col * GRID_SIZE, row * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)
            square_number = row * 7 + col + 1
            text = FONT.render(str(square_number), True, WHITE)
            text_rect = text.get_rect(center=(col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2))
            SCREEN.blit(text, text_rect)

# Define the coin and its position
class Coin:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def draw(self):
        pygame.draw.circle(SCREEN, WHITE, (self.col * GRID_SIZE + GRID_SIZE // 2, self.row * GRID_SIZE + GRID_SIZE // 2), GRID_SIZE // 4)

coin = Coin(0, 0)  # Initial position

# Check if the coin has reached square 49
def check_game_over():
    return coin.row == 6 and coin.col == 6

# Main game loop
running = True
game_over = False
while running:
    SCREEN.fill((0, 0, 0))
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif not game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                coin.row = max(0, coin.row - 1)
            elif event.key == pygame.K_DOWN:
                coin.row = min(6, coin.row + 1)
            elif event.key == pygame.K_LEFT:
                coin.col = max(0, coin.col - 1)
            elif event.key == pygame.K_RIGHT:
                coin.col = min(6, coin.col + 1)
    
    # Draw the game board
    draw_board()
    
    # Draw the coin
    coin.draw()
    
    # Check for game over condition
    if not game_over and check_game_over():
        game_over = True
        game_over_text = FONT.render("Game Over!", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        SCREEN.blit(game_over_text, game_over_rect)
    
    pygame.display.update()

pygame.quit()
sys.exit()
