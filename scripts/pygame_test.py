import pygame
from src.flock import player, boid, game

# Init pygame module and screen
pygame.init()

# set constants
width = 1600
height = 900
n_boids = 20
max_velocity = 0.5
v_player = 0.6

# init
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flock simulation with China")

p1 = player(width=width, height=height, screen=screen)
game = game(max_v=max_velocity, n_boids=n_boids, width=width, height=height, screen=screen)

# game loop
running = True
while running:
    screen.fill(game.background)
    p1.move()
    player.show_player(p1, p1)
    # game.update()
    game.show_flock()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

        # if event.type == pygame.MOUSEBUTTONUP:
        #     game.getPos()

        # key pressed down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RCTRL:
                p1.change_sprite()
            if event.key == pygame.K_UP:
                p1.direction[1] += -v_player
            if event.key == pygame.K_DOWN:
                p1.direction[1] += v_player
            if event.key == pygame.K_LEFT:
                p1.direction[0] += -v_player
            if event.key == pygame.K_RIGHT:
                p1.direction[0] += v_player

        # key pressed up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                p1.direction[0] += v_player
            if event.key == pygame.K_RIGHT:
                p1.direction[0] += -v_player
            if event.key == pygame.K_UP:
                p1.direction[1] += v_player
            if event.key == pygame.K_DOWN:
                p1.direction[1] += -v_player
