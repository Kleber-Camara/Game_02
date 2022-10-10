from assets.objects.scripts.classes.classe import Classe
from assets.objects.scripts.skill.skillAtribuition import SkillAtribuition


class Thief(Classe):

    def __init__(self) -> None:
        super().__init__()
        self.dodge = 50
        self.health = 30
        self.mana = 15
        self.damage = 20
        self.defense = 20
        self.speed = 45
        self.def_Fire = 20
        self.def_Water = 20
        self.def_Earth = 25
        self.def_Wind = 25
        self.def_Lightning = 10
        self.skills = SkillAtribuition('thief')
