from assets.objects.scripts.skill.skill import Skill


class ShortHeal(Skill):

    def __init__(self, x: int, y: int) -> None:
        super().__init__('shortheal.png', 1, 5, x, y, 0, 0, False, False)
        self._id = 3
        self.set_name('Short Heal')
        self.set_damage(45)
        self.set_mana_cost(45)
        self.set_range_atk(1)
        self.set_act_range(3)
        self.set_hit(100)
        self.set_type('FISICAL')
        self.set_target('ALLY')
        print('CURANDO')
