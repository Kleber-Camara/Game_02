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

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

    def _blit(self) -> None:
        pass

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
