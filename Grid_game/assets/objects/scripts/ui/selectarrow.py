import pygame.sprite
import os.path


class SelectArrow(pygame.sprite.Sprite):

    def __init__(self, path: str, x: int, y: int) -> None:
        super().__init__()
        self.__x = x
        self.__y = y
        new_path = os.path.join(path, 'select_arrow.png')
        try:
            self.sprite = pygame.image.load(new_path).convert_alpha()
            self.image = self.sprite.subsurface((0, 0), (16, 16))
        except Exception as exception:
            print(exception)
            exit()

        self.rect = self.image.get_rect(topleft=(self.__x, self.__y))

    def move(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y
        self.rect.topleft = self.__x, self.__y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)
