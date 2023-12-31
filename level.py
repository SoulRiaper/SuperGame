import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from slow_tile import SlowTile


class Level:

    def __init__(self):

        # display
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = YSortCameraGroup()
        self.slowness_sprites = YSortCameraGroup()

    def create_map(self):

        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE

                if column == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                elif column == "s":
                    SlowTile((x, y), [self.visible_sprites, self.slowness_sprites])
                elif column == "p":
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.slowness_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - (self.offset)
            self.display_surface.blit(sprite.image, offset_rect)