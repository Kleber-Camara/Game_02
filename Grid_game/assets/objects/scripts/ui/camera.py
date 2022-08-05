from assets.objects.scripts.system.mouse import Mouse
import pygame.sprite


class Camera(pygame.sprite.Group):

    def __init__(self) -> None:
        super().__init__()
        self.__box_collide = {'top': 300, 'bottom': 300, 'left': 150, 'right': 150}
        self.__box_camera = pygame.Rect(self.__box_collide['left'], self.__box_collide['top'],
                                        (pygame.display.get_surface().get_size()[0] - (
                                                    self.__box_collide['right'] + self.__box_camera['left'])),
                                        (pygame.display.get_surface().get_size()[1] - (
                                                    self.__box_collide['top'] + self.__box_camera['bottom'])))

    def custom_render(self, mouse: Mouse) -> None:
        self.center_camera(mouse)

    def center_camera(self, mouse: Mouse) -> None:
        if mouse.rect.left < self.__box_collide['left']:
            self.__box_collide['left'] = self.__box_collide['left'] - 1
        elif mouse.rect.right > self.__box_collide['right']:
            self.__box_collide['right'] = self.__box_collide['right'] + 1
        elif mouse.rect.top < self.__box_collide['top']:
            self.__box_collide['top'] = self.__box_collide['top'] - 1
        elif mouse.rect.bottom > self.__box_collide['bottom']:
            self.__box_collide['bottom'] = self.__box_collide['bottom'] + 1
        self.__offset.x = self.__box_camera.x - self.__box_collide['left']
        self.__offset.y = self.__box_camera.y - self.__box_collide['top']
