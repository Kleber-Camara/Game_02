from assets.objects.scripts.classes.classe import Classe


class Archer(Classe):

    def __init__(self) -> None:
        super().__init__()
        self._dodge = 50
        self._health = 30
        self._mana = 10
        self._damage = 25
        self._defense = 20
        self._speed = 55
        self._def_Fire = 15
        self._def_Water = 15
        self._def_Earth = 15
        self._def_Wind = 15
        self._def_Lightning = 5
