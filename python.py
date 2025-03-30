import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Get full screen size
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GLITCH_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Load font
font_large = pygame.font.Font(None, WIDTH // 10)
font_small = pygame.font.Font(None, WIDTH // 18)

# Fake Click Button
button_rect = pygame.Rect(WIDTH//4, HEIGHT//2, WIDTH//2, HEIGHT//10)

# Function to display text
def display_text(text, x, y, color=WHITE, font=font_large):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Step 1: Fake Click Screen
screen.fill(WHITE)
display_text("Click Here to Continue", WIDTH//5, HEIGHT//2 - 50, BLACK, font_small)
pygame.draw.rect(screen, BLACK, button_rect, 2)
pygame.display.update()

# Wait for the user to click
clicked = False
while not clicked:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                clicked = True

# Step 2: Fake System Scan
screen.fill(BLACK)
display_text("Analyzing Device...", WIDTH//6, HEIGHT//3, WHITE, font_small)
pygame.display.update()
time.sleep(2)

for _ in range(5):
    screen.fill(BLACK)
    display_text(f"Scanning System Files... {random.randint(10, 99)}%", WIDTH//6, HEIGHT//3, WHITE, font_small)
    pygame.display.update()
    time.sleep(random.uniform(0.5, 1.5))

# Step 3: Fake Critical Warning
start_time = time.time()
shutdown_time = start_time + 15  # 10-second shutdown countdown

while time.time() < shutdown_time:
    screen.fill(random.choice(GLITCH_COLORS))
    
    display_text("⚠ SYSTEM FAILURE ⚠", WIDTH//5, HEIGHT//4, RED, font_large)
    display_text("CRITICAL ERROR DETECTED!", WIDTH//6, HEIGHT//2 - 50, WHITE, font_small)
    display_text("DO NOT TURN OFF YOUR DEVICE!", WIDTH//7, HEIGHT//2 + 50, WHITE, font_small)
    
    countdown = int(shutdown_time - time.time())
    display_text(f"FORCED SHUTDOWN IN: {countdown}s", WIDTH//4, HEIGHT//1.5, RED, font_small)
    
    pygame.display.update()
    time.sleep(1)

# Step 4: Fake Shutdown Screen
screen.fill(BLACK)
display_text("Shutting Down...", WIDTH//3, HEIGHT//2, WHITE, font_small)
pygame.display.update()
time.sleep(3)

# Close the prank
pygame.quit()
