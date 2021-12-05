from settings import *

text_map = [
    'WWWWWWWWWWWWW',
    'W.W.....WW..W',
    'W.W......W..W',
    'W.WWWW...W..W',
    'W....W......W',
    'WWWW.W.....WW',
    'W.........WWW',
    'WWWWWWWWWWWWW'
]

world_map = set()
for j,row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))