from settings import *
import pygame as pg
import math

class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
            print('W')
        if keys[pg.K_s]:
            self.y += -player_speed * sin_a
            self.x += -player_speed * cos_a
            print('S')
        if keys[pg.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            print('A')
        if keys[pg.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
            print('D')
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02

