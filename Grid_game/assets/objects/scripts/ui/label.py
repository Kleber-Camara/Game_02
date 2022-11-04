import pygame.font


class Label:

    def __init__(self, text: str, x: int, y: int, width: int, height: int, color: tuple, fontSize: int, direction: str) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', fontSize)
        self.__text = font.render(text, True, color)
        self.__rect = pygame.Rect(x, y, width, height)
        self.__x = x
        self.__y = y
        self.__direction = direction

    def update(self) -> None:
        if self.__direction == 'RIGHT':
            self.__y -= 0.6
            self.__x += 0.3
        elif self.__direction == 'LEFT':
            self.__y -= 0.6
            self.__x -= 0.3
        else:
            self.__x = self.__x
            self.__y = self.__y
        self.__rect.topleft = (int(self.__x), int(self.__y))

    def render(self) -> None:
        pygame.display.get_surface().blit(self.__text, self.__rect)

