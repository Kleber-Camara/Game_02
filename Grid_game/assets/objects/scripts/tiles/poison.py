from assets.objects.scripts.tiles.tile import Tile
import pygame.draw


class Poison(Tile):

    def __init__(self, x: int, y: int, width: int, height: int, path: str) -> None:
        super().__init__(x, y, width, height, path)
        self._name = 'POISON'
        self._blit(path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_tile(self, offset: pygame.math.Vector2) -> None:
        pass

    def render(self) -> None:
        super().render()
        pygame.draw.rect(pygame.display.get_surface(), (20, 229, 54),
                         (self._x, self._y, self._width, self._height), 1)
