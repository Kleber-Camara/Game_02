import pygame.sprite


class HealthBar(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, width: int, height: int, type: str) -> None:
        if type == 'MAX':
            self.__blit('assets/sprites/ui/max_health.png')
        elif type == 'MANA':
            self.__blit('assets/sprites/ui/present_mana.png')
        else:
            self.__blit('assets/sprites/ui/present_health.png')
        self.image = self.sprite.subsurface((0, 0), (128, 32))
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.__type = type


    def updade(self) -> None:
        pass

    def render(self) -> None:
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def __blit(self, path: str) -> None:
        try:
            self.sprite = pygame.image.load(path).convert_alpha()
        except Exception as e:
            print(e)

