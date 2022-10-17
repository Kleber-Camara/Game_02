from assets.objects.scripts.classes.classe import Classe
from assets.objects.scripts.skill.skillAtribuition import SkillAtribuition


class Thief(Classe):

    def __init__(self) -> None:
        super().__init__()
        self._dodge = 50
        self._health = 30
        self._mana = 15
        self._damage = 20
        self._defense = 20
        self._speed = 45
        self._def_Fire = 20
        self._def_Water = 20
        self._def_Earth = 25
        self._def_Wind = 25
        self._def_Lightning = 10
        self._skill_list = SkillAtribuition('thief').get_Skill_List()
