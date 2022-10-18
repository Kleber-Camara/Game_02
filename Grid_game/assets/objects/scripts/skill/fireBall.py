from assets.objects.scripts.skill.skill import Skill


class FireBall(Skill):

    def __init__(self, x: int, y: int) -> None:
        super().__init__('fireball.png', 1, 10, x, y)
        self._id = 2
        self.set_name('Fire Ball')
        self.set_damage(45)
        self.set_range_atk(1)
        self.set_act_range(3)
        self.set_mana_cost(20)
        self.set_type('FIRE')