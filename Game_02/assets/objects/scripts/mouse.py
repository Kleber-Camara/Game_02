import math
import os.path
import pygame.mouse


class Mouse(pygame.sprite.Sprite):
    def __init__(self, path: str) -> None:
        pygame.sprite.Sprite.__init__(self)

        # VISUAL INTERACTIVE
        pygame.mouse.set_visible(False)
        self.path = path
        self.__blit(self.path)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.x, self.y = pygame.mouse.get_pos()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

        # EVENT CONTROLERS
        self.clicked = False

    def render(self, offset: pygame.math.Vector2) -> None:
        self.rect.center = self.x - offset.x, self.y - offset.y
        pygame.display.get_surface().blit(self.image, self.rect.center)

    def update_mouse(self) -> None:
        self.x, self.y = pygame.mouse.get_pos()

    def get_angle(self) -> float:
        angle = math.degrees(math.atan2(self.y, self.x))
        return angle

    def __blit(self, path: str) -> None:
        mouse = os.path.join(path, 'mouse_placeholder.png')
        try:
            self.sprite = pygame.image.load(mouse).convert_alpha()
            self.image = self.sprite.subsurface((0, 0), (32, 32))
        except Exception as ex:
            print(ex)
            exit()

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y
