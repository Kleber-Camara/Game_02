from assets.objects.scripts.skill.skill import Skill


class FireBall(Skill):

    def __init__(self, x: int, y: int, player_x: int, player_y: int) -> None:
        super().__init__('fireball.png', 1, 10, x, y, player_x, player_y, True)
        self._id = 2
        self.set_name('Fire Ball')
        self.set_damage(20)
        self.set_range_atk(1)
        self.set_act_range(3)
        self.set_mana_cost(20)
        self.set_hit(10)
        self.set_type('FIRE')
        print(self._ranged)
