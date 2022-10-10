from assets.objects.scripts.enemys.enemy import Enemy


class Slime(Enemy):

    def __init__(self, x: int, y: int) -> None:
        super().__init__()
        self._blit('slime_green.png')
        self.index = 0
        self.image = self._animation[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self._atk = False
        self._x, self._y = x, y

    def render(self) -> None:
        if not self.get_atk():
            if self.index > len(self._animation) - 1:
                self.index = 0
            self.index += 0.3
            self.image = self._animation[int(self.index)]
            self.rect.topleft = (self._x, self._y)
        super().render()

    def update(self) -> None:
        print("Slime andando")
        super().update()

    def get_atk(self) -> bool:
        return self._atk
