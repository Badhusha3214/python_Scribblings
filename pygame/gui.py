import serial
import math
import pygame
import time

# Set up the display
WIDTH = 1000
HEIGHT = 600
BACKGROUND = (0, 0, 0)  # Black
LINE_COLOR = (0, 255, 0)  # Green
TEXT_COLOR = (255, 255, 255)  # White
DOT_COLOR = (255, 0, 0)  # Red

# Radar settings
RADAR_RADIUS = 500  # Reduced radius
RADAR_CENTER = (WIDTH // 2, HEIGHT - 100)  # Moved the center up a bit

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arduino Radar")
font = pygame.font.Font(None, 36)

# Set up the serial connection (adjust the port as needed)
ser = serial.Serial('COM8', 9600, timeout=1)

def draw_radar():
    screen.fill(BACKGROUND)
    pygame.draw.circle(screen, LINE_COLOR, RADAR_CENTER, 5)
    for i in range(4):
        pygame.draw.circle(screen, LINE_COLOR, RADAR_CENTER, RADAR_RADIUS * (i+1) // 4, 1)
    
    for angle in range(0, 200, 30):
        radian = math.radians(angle)
        end_pos = (
            RADAR_CENTER[0] + math.sin(radian) * RADAR_RADIUS,
            RADAR_CENTER[1] - math.cos(radian) * RADAR_RADIUS
        )
        pygame.draw.line(screen, LINE_COLOR, RADAR_CENTER, end_pos, 1)

running = True
last_data_time = time.time()
points = []  # List to store detected points and their creation time

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_radar()

    current_time = time.time()

    if ser.in_waiting:
        data = ser.readline().decode('utf-8').rstrip().split(',')
        if len(data) == 2:
            angle, distance = map(int, data)
            distance = min(distance, 400)  # Cap the distance at 400 cm
            scaled_distance = (distance / 90) * RADAR_RADIUS  # Scale the distance to fit our radar
            radian = math.radians(angle)
            x = RADAR_CENTER[0] + math.sin(radian) * scaled_distance
            y = RADAR_CENTER[1] - math.cos(radian) * scaled_distance
            points.append((int(x), int(y), current_time))
            last_data_time = current_time

    # Draw and update points
    points = [p for p in points if current_time - p[2] <= 4]  # Keep only points less than 4 seconds old
    for point in points:
        pygame.draw.circle(screen, DOT_COLOR, (point[0], point[1]), 5)

    # Check if no data has been received for more than 5 seconds
    if current_time - last_data_time > 5:
        text = font.render("No data receiving", True, TEXT_COLOR)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text, text_rect)

    pygame.display.flip()

ser.close()
pygame.quit()