from assets.objects.scripts.enemys.enemy import Enemy


class Slime(Enemy):

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self._blit('slime_green.png')
        self._name = 'Green Slime'
        self.index = 0
        self.image = self._animation[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self._atk = False
        self._x, self._y = x, y
        self.set_max_health(80)
        self.set_max_mana(40)
        self.set_atk(25)
        self.set_def(20)
        self.set_dodge(35)
        self.set_lightning_def(10)
        self.set_fire_def(20)
        self.set_wind_def(20)
        self.set_earth_def(15)
        self.set_water_def(15)

    def render(self) -> None:
        if not self.get_attacking():
            if self.index > len(self._animation) - 1:
                self.index = 0
            self.index += 0.3
            self.image = self._animation[int(self.index)]
            self.rect.topleft = (self._x, self._y)
            #print(self._present_health)

        super().render()

    def update(self) -> None:
        print("Slime andando")
        #print(self.get_present_health())
        super().update()

    def get_atk(self) -> bool:
        return self._atk
