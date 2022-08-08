from assets.objects.scripts.skill.skill import Skill


class Slash(Skill):

    def __init__(self, path: str) -> None:
        super().__init__(path)
        self.set_name('Slash')
        self.set_damage(32)
        self.set_mana_cost(0)
        self.set_range_atk(1)
