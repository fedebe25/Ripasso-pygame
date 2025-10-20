# Lezione 1 – Template pulito
# Obiettivo: creare la finestra di gioco e disegnare il personaggio

import pygame

# Inizializzazione Pygame
pygame.init()  

# Dimensioni della finestra
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ladro in fuga - Lezione 1")

# Clock per gestire FPS
clock = pygame.time.Clock()

# Ladro placeholder (rettangolo rosso)
player_x = 100
player_y = 250
player_width = 50
player_height = 50
player_speed = 5

# Loop principale del gioco
running = True
while running:
    # Gestione eventi (chiusura finestra)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Disegna sfondo
    screen.fill((50, 50, 50))  # Grigio scuro

    # Disegna ladro
    pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_width, player_height))

    # Aggiorna display
    pygame.display.update()

    # Mantieni 60 FPS
    clock.tick(60)

# Chiudi Pygame
pygame.quit()
