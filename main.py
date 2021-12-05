import pygame as pg
import pygame.draw

from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

pg.init()
sc = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
player = Player()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
    player.movement()
    sc.fill(BLACK)

    pygame.draw.rect(sc, BLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    ray_casting(sc, player.pos, player.angle)

   # pg.draw.circle(sc, GREEN, (int(player.x),int(player.y)), 12)
   # pg.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math.sin(player.angle)))

   #  for x, y in world_map:
   #      pygame.draw.rect(sc, DARKGRAY, (x, y, TILE, TILE), 2)

    pg.display.flip()
    clock.tick(FPS)

