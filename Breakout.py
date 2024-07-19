import pygame
import random

# Inicializa pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255)]

# Paddle
paddle_width = 100
paddle_height = 10
paddle_speed = 6
paddle = pygame.Rect(screen_width // 2 - paddle_width // 2, screen_height - 30, paddle_width, paddle_height)

# Ball
ball_radius = 10
ball_speed = [4, -4]
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius, ball_radius)

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 20
bricks = []

for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# Función para dibujar objetos
def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    pygame.draw.ellipse(screen, white, ball)
    for i, brick in enumerate(bricks):
        color = colors[i // brick_cols % len(colors)]
        pygame.draw.rect(screen, color, brick)
    pygame.display.flip()

# Bucle principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screen_width:
        paddle.right += paddle_speed

    # Movimiento de la pelota
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    if ball.colliderect(paddle) and ball_speed[1] > 0:
        ball_speed[1] = -ball_speed[1]

    # Colisión con los ladrillos
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
            break

    # Perder el juego
    if ball.bottom >= screen_height:
        running = False

    draw_objects()
    clock.tick(60)

pygame.quit()

