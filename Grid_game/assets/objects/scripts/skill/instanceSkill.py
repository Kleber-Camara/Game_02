from assets.objects.scripts.skill.slash import Slash
from assets.objects.scripts.skill.skill import Skill


class InstanceSkills:

    def __init__(self, name: str) -> None:
        self.__name = name

    def instanceSkill(self, x: int, y: int) -> Skill:
        if self.__name == 'Slash':
            return Slash(x, y)
