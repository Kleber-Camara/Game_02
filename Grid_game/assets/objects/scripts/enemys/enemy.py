import pygame.sprite
import os.path


class Enemy(pygame.sprite.Sprite):

    def __init__(self) -> None:
        super().__init__()
        self._name = 'standart'
        self._lv = 0
        self._max_health = 0
        self._present_health = 0
        self._max_mana = 0
        self._present_mana = 0
        self._atk = 0
        self._def = 0
        self._dodge = 0
        self._def_fire = 0
        self._def_water = 0
        self._def_wind = 0
        self._def_earth = 0
        self._def_lightning = 0
        self._animation = []
        self._moved = True
        self._attacking = False
        self._x = 0
        self._y = 0

    def update(self) -> None:
        self._moved = True

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def _blit(self, path: str) -> None:
        enemy = os.path.join('assets\sprites\enemy_sprites', path)
        try:
            self.sprite = pygame.image.load(enemy).convert_alpha()
            w = (self.sprite.get_width()) // 32
            for i in range(w):
                self._animation.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
        except Exception as e:
            print(e)
            exit()

    def set_moved(self) -> None:
        self._moved = True

    def set_attacking(self, atk: bool) -> None:
        self._attacking = atk
    def unset_moved(self) -> None:
        self._moved = False

    def set_max_health(self, health: int) -> None:
        self._max_health = health
        self.set_present_health(health)

    def set_present_health(self, health: int) -> None:
        self._present_health = health

    def set_max_mana(self, mana: int) -> None:
        self._max_mana = mana

    def set_present_mana(self, mana: int) -> None:
        self._present_mana = mana

    def set_atk(self, atk: int) -> None:
        self._atk = atk

    def set_def(self, defense: int) -> None:
        self._def = defense

    def set_dodge(self, dodge: int) -> None:
        self._dodge = dodge

    def set_fire_def(self, fire: int) -> None:
        self._def_fire = fire

    def set_water_def(self, water: int) -> None:
        self._def_water = water

    def set_wind_def(self, wind: int) -> None:
        self._def_wind = wind

    def set_earth_def(self, earth: int) -> None:
        self._def_earth = earth

    def set_lightning_def(self, light: int) -> None:
        self._def_lightning = light

    def get_x(self) -> int:
        return self._x

    def get_max_health(self) -> int:
        return self._max_health

    def get_dodge(self) -> int:
        return self._dodge

    def get_present_health(self) -> int:
        return self._present_health

    def get_y(self) -> int:
        return self._y

    def get_attacking(self) -> bool:
        return self._attacking

    def get_name(self) -> str:
        return self._name

    def get_witch_def(self, type: str) -> int:
        if type == 'FISICAL':
            return self._def
        elif type == 'FIRE':
            return self._def_fire
        elif type == 'WATER':
            return self._def_water
        elif type == 'WIND':
            return self._def_wind
        elif type == 'EARTH':
            return self._def_earth
        elif type == 'LIGHTNING':
            return self._def_lightning

    def make_damage(self, damage: int, type: str) -> None:
        if type == 'FISICAL':
            if (damage - self._def) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def)
        elif type == 'FIRE':
            if (damage - self._def_fire) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def_fire)
        elif type == 'WATER':
            if (damage - self._def_water) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def_water)
        elif type == 'WIND':
            if (damage - self._def_wind) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def_wind)
        elif type == 'EARTH':
            if (damage - self._def_earth) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def_earth)
        elif type == 'LIGHTNING':
            if (damage - self._def_lightning) <= 0:
                self._present_health -= 0
            else:
                self._present_health -= (damage - self._def_lightning)
