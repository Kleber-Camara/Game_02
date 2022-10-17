from assets.objects.scripts.classes.classe import Classe
from assets.objects.scripts.skill.skillAtribuition import SkillAtribuition


class MagicStudent(Classe):

    def __init__(self) -> None:
        super().__init__()
        self._dodge = 15
        self._health = 30
        self._mana = 100
        self._damage = 65
        self._defense = 15
        self._speed = 40
        self._def_Fire = 50
        self._def_Water = 40
        self._def_Earth = 40
        self._def_Wind = 40
        self._def_Lightning = 30
        self._skill_list = SkillAtribuition('student').get_Skill_List()
