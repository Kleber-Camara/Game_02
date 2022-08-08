import pygame.sprite


class Skill(pygame.sprite.Sprite):

    def __init__(self, path: str) -> None:
        super().__init__()
        self._blit(path)
        self._name = 'none'
        self._animation = []
        self._damage = 0
        self._range_atk = 0
        self._act_range = 0
        self._mana_cost = 0
        self._type_skill = 'STANDART'

    def set_name(self, name: str) -> None:
        self._name = name

    def set_damage(self, damage: int) -> None:
        self._damage = damage

    def set_range_atk(self, range_atk: int) -> None:
        self._range_atk = range_atk

    def set_mana_cost(self, cost: int) -> None:
        self._mana_cost = cost

    def set_act_range(self, act: int) -> None:
        self._act_range = act

    def get_name(self) -> str:
        return self._name

    def get_damage(self) -> int:
        return self._damage

    def get_range(self) -> int:
        return self._range_atk

    def get_act_range(self) -> int:
        return self._act_range

    def get_mana_cost(self) -> int:
        return self._mana_cost

    def _blit(self, path: str) -> None:
        pass
