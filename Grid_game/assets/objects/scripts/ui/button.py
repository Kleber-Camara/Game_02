import pygame.font


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, text: str, text_color: tuple, box_color: tuple,
                 size_font: int,
                 sprite_path: str) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', size_font)
        self.__text = font.render(text, True, text_color)
        self.__rect = pygame.Rect(x, y, width, height)
        self.__sizeFont = size_font
        self.__name = text
        self.__box_color = box_color
        self.__path = sprite_path
        
    def __init__(self, x: int, y: int, width: int, height: int, text: str, text_color: tuple, box_color: tuple, size_font: int) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', size_font)
        self.__text = font.render(text, True, text_color)
        self.__rect = pygame.Rect(x, y, width, height)
        self.__sizeFont = size_font
        self.__name = text
        self.__box_color = box_color

    def render(self) -> None:
        pygame.draw.rect(pygame.display.get_surface(), self.__box_color, self.__rect)
        if self.__sizeFont == 16:
            new_rect = (self.__rect.x + 10, self.__rect.y+2)
        else:
            new_rect = (self.__rect.x + 25, self.__rect.y - 5)
        pygame.display.get_surface().blit(self.__text, new_rect)
    
    def get_name(self) -> str:
        return self.__name
    
    def get_x(self) -> int:
        return self.__rect.x

    def get_y(self) -> int:
        return self.__rect.y

    def get_rect(self):
        return self.__rect
