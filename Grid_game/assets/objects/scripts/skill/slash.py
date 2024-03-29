from assets.objects.scripts.skill.skill import Skill


class Slash(Skill):

    def __init__(self, x: int, y: int) -> None:
        super().__init__('slash.png', 0, 5, x, y, 0, 0, False, False)
        self._id = 1
        self.set_name('Slash')
        self.set_damage(15)
        self.set_mana_cost(0)
        self.set_range_atk(1)
        self.set_act_range(1)
        self.set_hit(20)
        self.set_type('FISICAL')

