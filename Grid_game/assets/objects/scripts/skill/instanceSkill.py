from assets.objects.scripts.skill.slash import Slash
from assets.objects.scripts.skill.skill import Skill
from assets.objects.scripts.skill.fireBall import FireBall


class InstanceSkills:

    def __init__(self, name: str) -> None:
        self.__name = name

    def instanceSkill(self, x: int, y: int) -> Skill:
        if self.__name == 'Slash':
            return Slash(x, y)
        elif self.__name == 'Fire Ball':
            return FireBall(x, y)
