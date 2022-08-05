from assets.objects.scripts.classes.classe import Classe


class Adventurer(Classe):

    def __init__(self) -> None:
        super().__init__()
        self.dodge = 15
        self.health = 100
        self.mana = 20
        self.damage = 40
        self.defense = 35
        self.speed = 30
        self.def_Fire = 45
        self.def_Water = 35
        self.def_Earth = 45
        self.def_Wind = 45
        self.def_Lightning = 15
