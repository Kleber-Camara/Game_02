from abc import ABC, abstractmethod
import pygame.sprite


class Enemy_interface(ABC, pygame.sprite.Sprite):

    @abstractmethod
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)

    @abstractmethod
    def get_xPos(self) -> float:
        pass

    @abstractmethod
    def get_yPos(self) -> float:
        pass

    @abstractmethod
    def __blit_sprites(self, path: str) -> None:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def render(self) -> None:
        pass
