from assets.objects.scripts.classes.classe import Classe


class MagicStudent(Classe):

    def __init__(self) -> None:
        super().__init__()
        self.dodge = 15
        self.health = 30
        self.mana = 100
        self.damage = 65
        self.defense = 15
        self.speed = 40
        self.def_Fire = 50
        self.def_Water = 40
        self.def_Earth = 40
        self.def_Wind = 40
        self.def_Lightning = 30
