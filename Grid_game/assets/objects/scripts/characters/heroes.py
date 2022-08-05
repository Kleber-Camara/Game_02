from assets.objects.scripts.classes.classe import Classe
import pygame.sprite
import os.path


class Heroes(pygame.sprite.Sprite):

    def __init__(self, name: str, lv: int, path: str) -> None:
        super().__init__()
        self._path = path
        # UTILITIES
        self._x = 0
        self._y = 0
        # ATTRIBUTES
        self._def_Wind = 0
        self._def_Lightning = 0
        self._def_Earth = 0
        self._def_Water = 0
        self._def_Fire = 0
        self._speed = 0
        self._defense = 0
        self._damage = 0
        self._mana = 0
        self._dodge = 0
        self._health = 0
        self._name = name
        self._lv = lv
        self._xp = 0
        self._max_Xp = 100
        self._can_move = 2
        self._classe = Classe()
        self._select = False
        self._moved = False
        self._moving = False

        # SKILLS
        self.__skills_selected = []

    def update_hero(self) -> None:
        self.rect.topleft = self._x, self._y

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def _get_Atributes(self) -> None:
        self._health = self._health + self._classe.get_health()
        self._dodge = self._dodge + self._classe.get_dodge()
        self._mana = self._mana + self._classe.get_mana()
        self._damage = self._damage + self._classe.get_damage()
        self._defense = self._defense + self._classe.get_defense()
        self._speed = self._speed + self._classe.get_speed()
        self._def_Fire = self._def_Fire + self._classe.get_fire()
        self._def_Water = self._def_Water + self._classe.get_water()
        self._def_Earth = self._def_Earth + self._classe.get_earth()
        self._def_Wind = self._def_Wind + self._classe.get_wind()
        self._def_Lightning = self._def_Lightning + self._classe.get_lighting()

    def _blit(self, sprite_path: str) -> None:
        image_path = os.path.join(self._path, sprite_path)
        try:
            self.sprite = pygame.image.load(image_path).convert_alpha()
            self.image = self.sprite.subsurface((0, 0), (16, 16))
        except Exception as exception:
            print(exception)
            exit()

    # SETTERS
    def set_x(self, x: int) -> None:
        self._x = x

    def set_y(self, y: int) -> None:
        self._y = y

    def set_move(self, move: int) -> None:
        self._can_move = move

    def set_moving(self, moving: bool) -> None:
        self._moving = moving

    # GETTERS
    def get_move(self) -> int:
        return self._can_move

    def get_moving(self) -> bool:
        return self._moving

    def get_x(self) -> int:
        return self._x

    def get_y(self) -> int:
        return self._y

    def get_name(self) -> str:
        return self._name

    def get_health(self) -> float:
        return self._health

    def get_mana(self) -> float:
        return self._mana

    def get_dodge(self) -> int:
        return self._dodge

    def get_damage(self) -> int:
        return self._damage

    def get_defense(self) -> int:
        return self._defense

    def get_speed(self) -> int:
        return self._speed

    def get_fire(self) -> int:
        return self._def_Fire

    def get_water(self) -> int:
        return self._def_Water

    def get_earth(self) -> int:
        return self._def_Earth

    def get_wind(self) -> int:
        return self._def_Wind

    def get_lighting(self) -> int:
        return self._def_Lightning

    def get_classe(self) -> Classe:
        return self._classe
