import pygame
import os
from random import randint

pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

clock = pygame.time.Clock()

# Проверяем существование файлов
songs = ["st.mp3", "tm.mp3", "wk.mp3"]
songs = [s for s in songs if os.path.exists(s)]  # Фильтруем только существующие файлы

if not songs:
    print("Нет доступных аудиофайлов!")
    exit()

cur = 0
effect = pygame.mixer.Sound(songs[cur])

def play_random():
    """Проигрывает случайный трек."""
    global cur, effect
    cur = randint(0, len(songs) - 1)
    effect.stop()
    effect = pygame.mixer.Sound(songs[cur])
    effect.play()
    print(f"Playing: {songs[cur]}")

def next_song():
    """Переключение на следующий трек."""
    global cur, effect
    cur = (cur + 1) % len(songs)  # Цикличное переключение
    effect.stop()
    effect = pygame.mixer.Sound(songs[cur])
    effect.play()
    print(f"Playing: {songs[cur]}")

def prev_song():
    """Переключение на предыдущий трек."""
    global cur, effect
    cur = (cur - 1) % len(songs)  
    effect.stop()
    effect = pygame.mixer.Sound(songs[cur])
    effect.play()
    print(f"Playing: {songs[cur]}")

running = True
playing = False

print("s - stop, f - play, n - next, p - previous, r - random")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                effect.stop()
                playing = False
            elif event.key == pygame.K_f and not playing:
                effect.play()
                playing = True
            elif event.key == pygame.K_n:
                next_song()
            elif event.key == pygame.K_p:
                prev_song()
            elif event.key == pygame.K_r:
                play_random()

    clock.tick(60)

pygame.quit()