import pygame.font


class Label:

    def __init__(self, text: str, x: int, y: int, width: int, height: int, color: tuple, fontSize: int) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', fontSize)
        self.__text = font.render(text, True, color)
        self.__rect = pygame.Rect(x, y, width, height)

    def render(self) -> None:
        pygame.display.get_surface().blit(self.__text, self.__rect)

