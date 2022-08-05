from assets.objects.scripts.classes.classe import Classe


class Archer(Classe):

    def __init__(self) -> None:
        super().__init__()
        self.dodge = 50
        self.health = 30
        self.mana = 10
        self.damage = 25
        self.defense = 20
        self.speed = 55
        self.def_Fire = 15
        self.def_Water = 15
        self.def_Earth = 15
        self.def_Wind = 15
        self.def_Lightning = 5
