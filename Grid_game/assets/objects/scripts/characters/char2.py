from assets.objects.scripts.classes.magicstudent import MagicStudent
from assets.objects.scripts.characters.heroes import Heroes
import pygame.transform


class Char2(Heroes):

    def __init__(self, path: str) -> None:
        super().__init__('Char2', 3, path)
        self.set_x(0)
        self.set_y(32)
        self._blit('magic_place_holder.png')
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft=(self.get_x(), self.get_y()))
        self._classe = MagicStudent()
        self.set_skills_list(self._classe.select_skills([2]))
        self._get_Atributes()
