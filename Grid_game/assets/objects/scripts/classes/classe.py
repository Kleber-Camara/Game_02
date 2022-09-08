import os.path


class Classe:

    def __init__(self) -> None:
        self._dodge = 0
        self._health = 0
        self._mana = 0
        self._damage = 0
        self._defense = 0
        self._speed = 0
        self._def_Fire = 0
        self._def_Water = 0
        self._def_Earth = 0
        self._def_Wind = 0
        self._def_Lightning = 0
        self._skill_list = []
        self._path = os.path.join('assets/objects/scripts/')
        #self._skill_list.append(Slash())

    def get_health(self) -> float:
        return self._health

    def get_mana(self) -> float:
        return self._mana

    def get_dodge(self) -> int:
        return self._dodge

    def get_damage(self) -> int:
        return self._damage

    def get_defense(self) -> int:
        return self._defense

    def get_speed(self) -> int:
        return self._speed

    def get_fire(self) -> int:
        return self._def_Fire

    def get_water(self) -> int:
        return self._def_Water

    def get_earth(self) -> int:
        return self._def_Earth

    def get_wind(self) -> int:
        return self._def_Wind

    def get_lighting(self) -> int:
        return self._def_Lightning
