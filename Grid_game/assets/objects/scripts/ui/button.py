import pygame.font


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, text: str, text_color: tuple, box_color: tuple,
                 size_font: int,
                 sprite_path: str) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', size_font)
        self.__text = font.render(text, True, text_color)
        self.__rect = pygame.Rect(x, y, width, height)
        self.__rect_text = self.__text.get_rect()
        self.__sizeFont = size_font
        self.__name = text
        self.__box_color = box_color
        self.__path = sprite_path
        
    def __init__(self, x: int, y: int, width: int, height: int, text: str, text_color: tuple, box_color: tuple,
                 size_font: int, target: str) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', size_font)
        self.__text = font.render(text, True, text_color)
        self.__rect = pygame.Rect(x, y, width, height)
        self.__rect_text = self.__text.get_rect()
        self.__sizeFont = size_font
        self.__name = text
        self.__box_color = box_color
        self._target = target

    def render(self) -> None:
        pygame.draw.rect(pygame.display.get_surface(), self.__box_color, self.__rect)   # Fundo do botão
        self.__rect_text.center = (self.__rect.topleft[0] + (self.__rect.width / 2),
                                   self.__rect.topleft[1] + (self.__rect.height / 2))   # Posição do texto
        pygame.display.get_surface().blit(self.__text, self.__rect_text.topleft)        # Desenho do texto
    
    def get_name(self) -> str:
        return self.__name
    
    def get_x(self) -> int:
        return self.__rect.x

    def get_y(self) -> int:
        return self.__rect.y

    def get_rect(self):
        return self.__rect

    def get_target(self) -> str:
        return self._target
