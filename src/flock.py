import numpy as np
import webcolors as wc
import pygame

# Player
class player():
    def __init__(self, width, height, screen):
        self.x = width/2
        self.y = height/2
        self.pooh = [pygame.transform.scale(pygame.image.load("static/winnie_pooh.png"), (120, 180)), "pooh"]
        self.xijinping = [pygame.transform.scale(pygame.image.load("static/xijinping.png"), (120, 180)), "xi"]
        self.sprite = self.pooh
        self.direction = [0, 0]

        self.screen = screen
        self.width = width
        self.height = height

    def change_sprite(self):
        self.sprite = self.pooh if self.sprite[-1] == "xi" else self.xijinping

    def move_forced(self, dx, dy):
        self.x += dx
        self.y += dy

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def show_player(self, player):
        self.screen.blit(player.sprite[0], ((player.x + self.width) % self.width, (player.y + self.height) % self.height))

class boid():
    def __init__(self, width, height, max_v):
        self.position = np.array([np.random.randint(0, width), np.random.randint(0, height)]).astype("float64")
        self.velocity = (np.random.rand(2) - 0.5) * 0.1
        self.max_velocity = max_v
        self.acceleration = (np.random.rand(2) - 0.5) * 0.1

        self.sprite = [pygame.transform.rotate(pygame.transform.scale(pygame.image.load("static/boid.png"), (30, 30)), 90), "boid"]

    def update(self):
        # + dx, dy; + ddx, ddy
        self.position += self.velocity
        self.velocity += self.acceleration

        if np.linalg.norm(self.velocity) > self.max_velocity:
            self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.max_velocity
            self.acceleration = np.zeros(2)


# Game Client
class game():
    def __init__(self, max_v, n_boids, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.max_v = max_v
        self.n_boids = n_boids

        self.background = tuple(np.array(wc.hex_to_rgb('#D9D8D3')))
        self.flock = [boid(self.width, self.height, self.max_v) for i in range(0, self.n_boids)]

    def show_flock(self):
        for boid in self.flock:
            self.screen.blit(boid.sprite[0], ((boid.position[0] + self.width) % self.width, (boid.position[1] + self.height) % self.height))
            boid.update()