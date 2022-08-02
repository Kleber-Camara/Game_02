import os.path
import pygame.sprite

class Tile(pygame.sprite.Sprite):

    def __init__(self, type: str, path: str, x: int, y: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.path = os.path.join(path, 'tile_set/tileset_placeholder.png')
        self.blit_tile(self.path)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.x = x
        self.y = y

    def render(self, offset: pygame.math.Vector2) -> None:
        self.rect.topleft = self.x - offset.x, self.y - offset.y

    def blit_tile(self, path: str) -> None:
        try:

            self.sprite = pygame.image.load(path)

        except Exception as exception:
            print(exception)
            exit()

        if self.type == 'GROUND':
            self.image = self.sprite.subsurface((32, 32), (32, 32))
        elif self.type == 'WALL':
            self.image = self.sprite.subsurface((160, 160), (32, 32))
