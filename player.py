import pygame
from settings import *


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load("./graphics/test/player1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

        self.hit_box = pygame.rect.Rect((0,0), (TILESIZE // 1.5, TILESIZE // 1.2))
        self.hit_box.midtop = self.rect.midtop

    def input(self):
        keys = pygame.key.get_pressed()

        # up down movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # left right movement
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * speed
        self.rect.midtop = self.hit_box.midtop
        self.collision("horizontal")
        self.hit_box.y += self.direction.y * speed
        self.rect.midtop = self.hit_box.midtop
        self.collision("vertical")


        # self.rect.center += self.direction * speed


    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hit_box):
                    if self.direction.x > 0:
                        self.hit_box.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hit_box.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.hit_box):
                    if self.direction.y > 0:
                        self.hit_box.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hit_box.top = sprite.rect.bottom

    def update(self):
        self.move(self.speed)
        self.input()