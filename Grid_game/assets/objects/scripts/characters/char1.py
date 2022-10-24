from assets.objects.scripts.characters.heroes import Heroes
from assets.objects.scripts.classes.thief import Thief
import pygame


class Char1(Heroes):

    def __init__(self, path: str) -> None:
        super().__init__('Char1', 2, path)
        self._blit('thief_place_holder.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(self._x, self._y))
        self._classe = Thief()
        self.set_skills_list(self._classe.select_skills([1]))
        self._get_Atributes()

    def update_hero(self) -> None:
        super().update_hero()

    def render(self) -> None:
        super().render()
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 255), (self.get_x(), self.get_y(), 32, 32), 2)
