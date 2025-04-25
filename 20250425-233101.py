import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Wave Simulation")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()

def draw_waveform():
    win.fill(BLACK)
    num_lines = 100
    spacing = WIDTH // num_lines

    for i in range(num_lines):
        x = i * spacing
        y = HEIGHT // 2
        height = random.randint(10, 100)
        pygame.draw.line(win, GREEN, (x, y - height), (x, y + height), 2)

# Main loop
running = True
while running:
    clock.tick(20)  # Control the frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_waveform()
    pygame.display.update()

pygame.quit()
sys.exit()