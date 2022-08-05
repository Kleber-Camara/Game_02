import pygame.mouse
import os.path


class Mouse(pygame.sprite.Sprite):

    def __init__(self, path: str) -> None:
        self.__blit(path)
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect(topleft=(pygame.mouse.get_pos()))

    def update_mouse(self) -> None:
        self.rect.topleft = pygame.mouse.get_pos()

    @staticmethod
    def render() -> None:
        x, y = pygame.mouse.get_pos()
        pygame.draw.rect(pygame.display.get_surface(), (255, 248, 32), (x, y, 16, 16))

    def __blit(self, path: str) -> None:
        new_path = os.path.join(path, 'mouse_place_holder.png')
        try:
            self.sprite = pygame.image.load(new_path).convert_alpha()
            self.image = self.sprite.subsurface((0, 0), (16, 16))
        except Exception as exception:
            print(exception)
            exit()

    @staticmethod
    def get_pos() -> tuple:
        return pygame.mouse.get_pos()
