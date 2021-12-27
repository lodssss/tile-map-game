from pygame.draw import rect
from settings import *
import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game    # to be able to acess all_sprites
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites  # adding player to all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)    # hard to use super() on classes from imported modules
        
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if not self.collision(dx, dy):
            self.x += dx
            self.y += dy

    def collision(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False
        

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls # game.walls for wall objects
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE