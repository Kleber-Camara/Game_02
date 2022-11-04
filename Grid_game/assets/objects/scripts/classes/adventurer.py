from assets.objects.scripts.skill.skillAtribuition import SkillAtribuition
from assets.objects.scripts.classes.classe import Classe


class Adventurer(Classe):

    def __init__(self) -> None:
        super().__init__()
        self._dodge = 15
        self._health = 100
        self._mana = 20
        self._damage = 40
        self._defense = 35
        self._speed = 30
        self._def_Fire = 45
        self._def_Water = 35
        self._def_Earth = 45
        self._def_Wind = 45
        self._def_Lightning = 15
        self._skill_list = SkillAtribuition('adventurer').get_Skill_List()
