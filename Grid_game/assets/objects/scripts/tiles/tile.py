import pygame.sprite
import os.path


class Tile(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, path: str) -> None:
        pygame.sprite.Sprite.__init__(self)
        self._x = x
        self._y = y
        self._path = path
        self._width = width
        self._height = height
        self._name = 'NONE'
        self._can_move = False
        self._can_atk = False

    def update_tile(self, offset: pygame.math.Vector2) -> None:
        pass

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)
        if self._can_move:
            pygame.draw.rect(pygame.display.get_surface(), (255, 0, 0), (self._x, self._y, self._width, self._height), 3)
        if self._can_atk:
            pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), (self._x, self._y, self._width, self._height),
                             3)

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_can_move(self) -> bool:
        return self._can_move

    def get_can_atk(self) -> bool:
        return self._can_atk
    def set_can_move(self) -> None:
        self._can_move = True

    def set_cannot_move(self) -> None:
        self._can_move = False

    def set_cannot_atk(self) -> None:
        self._can_atk = False

    def set_can_atk(self) -> None:
        self._can_atk = True

    def _blit(self, path: str) -> None:
        new_path = os.path.join(path, 'sprite_sheet_placeholder.png')
        try:
            self.sprite = pygame.image.load(new_path).convert()
            if self._name == 'NONE' or self._name == 'FLOOR':
                self.image = self.sprite.subsurface((96, 0), (32, 32))
            elif self._name == 'ROCK':
                self.image = self.sprite.subsurface((0, 0), (32, 32))
            elif self._name == 'POISON':
                self.image = self.sprite.subsurface((64, 0), (32, 32))
            elif self._name == 'WATER':
                self.image = self.sprite.subsurface((32, 0), (32, 32))
        except Exception as exception:
            print(exception)
            exit()
