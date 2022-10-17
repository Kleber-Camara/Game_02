import os.path
import pygame.sprite


class Skill(pygame.sprite.Sprite):

    def __init__(self, spritesheet: str, lv: int, end_time: int, x: int, y: int) -> None:
        super().__init__()
        self._id = -1
        self._skils_animation = os.path.join('assets/sprites/skills')
        self._skils_animation = os.path.join(self._skils_animation, spritesheet)
        self._animation = []
        self._blit(self._skils_animation)
        self.image = self._animation[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self._name = 'none'
        self._damage = 0
        self._range_atk = 0
        self._act_range = 0
        self._mana_cost = 0
        self._type_skill = 'STANDART'
        self._lvl_required = lv
        self._present_time = 0
        self._end_time = end_time
        self._destrutible = False
        self._can_damage = True
        self._x = x
        self._y = y

    def update_skill(self) -> None:
        if self._present_time > self._end_time:
            self._destrutible = True
        else:
            self._present_time += 0.3

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def set_name(self, name: str) -> None:
        self._name = name

    def set_type(self, type: str) -> None:
        self._type_skill = type

    def set_damage(self, damage: int) -> None:
        self._damage = damage

    def set_range_atk(self, range_atk: int) -> None:
        self._range_atk = range_atk

    def set_mana_cost(self, cost: int) -> None:
        self._mana_cost = cost

    def set_damage_status(self, status: bool) -> None:
        self._can_damage = status

    def set_act_range(self, act: int) -> None:
        self._act_range = act

    def get_name(self) -> str:
        return self._name

    def get_damage(self) -> int:
        return self._damage

    def get_range(self) -> int:
        return self._range_atk

    def get_act_range(self) -> int:
        return self._act_range

    def get_mana_cost(self) -> int:
        return self._mana_cost

    def get_id(self) -> int:
        return self._id

    def get_destruction(self) -> bool:
        return self._destrutible

    def get_can_damage(self) -> bool:
        return self._can_damage

    def get_type(self) -> str:
        return self._type_skill

    def _blit(self, path: str) -> None:
        try:
            self.sprite = pygame.image.load(path).convert_alpha()

            w = self.sprite.get_width() // 32

            for i in range(w):
                self._animation.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
        except Exception as e:
            print(e)
