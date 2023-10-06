import pygame
from settings import *
from tile import Tile
from player import Player


class Level:

    def __init__(self):

        # display
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def create_map(self):

        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE

                if column == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif column == "p":
                    Player((x, y), [self.visible_sprites])

    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)