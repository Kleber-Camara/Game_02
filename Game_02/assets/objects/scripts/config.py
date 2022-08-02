import os.path
import pygame.display


class Configuration:

    def __init__(self, path: str) -> None:
        self.screen = pygame.display.list_modes()
        self.conf = '{}'.format(self.screen)
        txt = os.path.join(path, 'config.txt')
        with open(txt, 'w') as config:
            config.write(str(self.conf))
