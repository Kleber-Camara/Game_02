import pygame.font


class Button:

    def __init__(self, x: int, y: int, width: int, height: int, text: str, color: tuple, size_font: int) -> None:
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', size_font)
        self.text = font.render(text, True, color)
        self.rect = pygame.Rect(x, y, width, height)
        self.name = text

    def render(self) -> None:
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), self.rect)
        new_rect = (self.rect.x + 25, self.rect.y - 5)
        pygame.display.get_surface().blit(self.text, new_rect)

    def get_x(self) -> int:
        return self.rect.x

    def get_y(self) -> int:
        return self.rect.y
