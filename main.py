import pygame as pg
from settings import *
from player import Player
import math

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

    pg.draw.circle(sc, GREEN, player.pos, 12)
    pg.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math.sin(player.angle)))

    pg.display.flip()
    clock.tick(FPS)

