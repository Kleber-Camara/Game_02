from assets.objects.scripts.skill.skill import Skill


class Slash(Skill):

    def __init__(self, x: int, y: int) -> None:
        super().__init__('slash.png', 0, 1, x, y)
        self._id = 1
        self.set_name('Slash')
        self.set_damage(32)
        self.set_mana_cost(0)
        self.set_range_atk(1)
