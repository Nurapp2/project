import pygame
import os
import datetime

pygame.init()

H = 1180
W = 1200
screen = pygame.display.set_mode((H, W))
clock = pygame.time.Clock()

_image_library = {}
def get_image(path):
    global _image_library
    if path not in _image_library:
        _image_library[path] = pygame.image.load(path)
    return _image_library[path]

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(x, y))
    return rotated_image, new_rect

done = False
now = datetime.datetime.now()

ang = -6 * now.second
ang2 = -6 * now.second - (now.minute + 60)

center_x, center_y = H // 2, W // 2

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    ang -= 1
    ang2 -= 0.1 

    screen.fill((0, 0, 0))

    screen.blit(get_image('clockk.jpg'), (0, 0))
    img = get_image('arrow.png')

    rotated_arrow, new_rect = rot_center(img, ang, center_x, center_y)
    screen.blit(rotated_arrow, new_rect.topleft)

    rotated_arrow2, new_rect2 = rot_center(img, ang2, center_x, center_y)
    screen.blit(rotated_arrow2, new_rect2.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()