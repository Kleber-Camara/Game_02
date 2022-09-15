import os.path
import pygame.sprite


class Enemy(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self._lv = 0
        self._max_health = 0
        self._present_health = 0
        self._max_mana = 0
        self._present_mana = 0
        self._atk = 0
        self._def = 0
        self._dodge = 0
        self._speed = 0
        self._def_fire = 0
        self._def_water = 0
        self._def_wind = 0
        self._def_earth = 0
        self._def_lightning = 0
        self._animation = []
        self._moved = True
        self._x = 0
        self._y = 0

    def update(self) -> None:
        self._moved = True

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def _blit(self, path: str) -> None:
        enemy = os.path.join('assets\sprites\enemy_sprites', path)
        try:
            self.sprite = pygame.image.load(enemy).convert_alpha()
            w = (self.sprite.get_width()) // 32
            for i in range(w):
                self._animation.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
        except Exception as e:
            print(e)
            exit()

    def set_moved(self) -> None:
        self._moved = True

    def unset_moved(self) -> None:
        self._moved = False

    def set_max_health(self, health: int) -> None:
        self._max_health = health

    def set_present_health(self, health: int) -> None:
        self._present_health = health

    def set_max_mana(self, mana: int) -> None:
        self._max_mana = mana

    def set_present_mana(self, mana: int) -> None:
        self._present_mana = mana

    def set_atk(self, atk: int) -> None:
        self._atk = atk

    def set_def(self, defense: int) -> None:
        self._def = defense

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y
