import pygame

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

RADIUS = 25
x, y = WIDTH // 2, HEIGHT // 2  

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)  

    pygame.draw.circle(screen, RED, (x, y), RADIUS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and x + RADIUS + 20 <= WIDTH:
                x += 20
            if event.key == pygame.K_LEFT and x - RADIUS - 20 >= 0:
                x -= 20
            if event.key == pygame.K_DOWN and y + RADIUS + 20 <= HEIGHT:
                y += 20
            if event.key == pygame.K_UP and y - RADIUS - 20 >= 0:
                y -= 20

    pygame.display.flip()
    clock.tick(60)

pygame.quit()