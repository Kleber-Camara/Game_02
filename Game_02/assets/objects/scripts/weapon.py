import os.path
import pygame.sprite


class Weapon(pygame.sprite.Sprite):

    def __init__(self, path: str, x: int, y: int, direction: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.__blit(path, direction)
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        if direction == 4:
            self.rect.topright = x + 8, y + 10
        elif direction == 6:
            self.rect.topleft = x + 52, y + 24
        elif direction == 2:
            self.rect.topleft = x + 12, y + 48
        elif direction == 8:
            self.rect.bottomleft = x + 20, y + 6

    def render(self, offset: pygame.math.Vector2) -> None:
        self.rect.topleft = self.rect.x - offset.x, self.rect.y - offset.y
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def __blit(self, path: str, dir: int) -> None:
        w_path = os.path.join(path, 'sword.png')

        try:

            self.sprite = pygame.image.load(w_path)

        except Exception as ex:
            print(ex)
            exit()
        if dir == 2:
            self.image = self.sprite.subsurface((16, 0), (16, 16))
            self.image = pygame.transform.flip(self.image, False, True)
        elif dir == 8:
            self.image = self.sprite.subsurface((16, 0), (16, 16))
        elif dir == 4:
            self.image = self.sprite.subsurface((0, 0), (16, 16))
        elif dir == 6:
            self.image = self.sprite.subsurface((0, 0), (16, 16))
            self.image = pygame.transform.flip(self.image, True, False)
