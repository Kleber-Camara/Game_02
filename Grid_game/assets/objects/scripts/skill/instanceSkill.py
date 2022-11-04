from assets.objects.scripts.skill.shortHeal import ShortHeal
from assets.objects.scripts.skill.fireBall import FireBall
from assets.objects.scripts.skill.slash import Slash
from assets.objects.scripts.skill.skill import Skill


class InstanceSkills:

    def __init__(self, name: str) -> None:
        self.__name = name

    def instanceSkill(self, x: int, y: int, player_x: int, player_y: int) -> Skill:
        if self.__name == 'Slash':
            return Slash(x, y)
        elif self.__name == 'Fire Ball':
            return FireBall(x, y, player_x, player_y)
        elif self.__name == 'Short Heal':
            return ShortHeal(x, y)
