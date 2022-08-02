import os.path
import pygame.sprite
from assets.objects.scripts.tile import Tile
from assets.objects.scripts.player import Player


class projectile(pygame.sprite.Sprite):

    def __init__(self, path: str, type: str, dx: float, dy: float, player: Player) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.size = 0
        self.type = type
        self.animation = []
        self.__blit(path, self.type, self.size)
        self.image = pygame.transform.scale(self.image, (16 * 2, 16 * 2))
        self.spd = 0.9
        self.x = player.get_xPos() + dx
        self.y = player.get_yPos() + dy
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.destroyer = False
        #self.rect.topleft = self.x * self.spd, self.y * self.spd
        print(self.x, self.y)

    def update_projectile(self, offset: pygame.Vector2) -> None:
        self.x = (self.x * self.spd)
        self.y = (self.y * self.spd)

    def verify_collision(self, world: list[Tile]) -> None:
        for n in range(len(world)):
            if self.rect.colliderect(world[n]):
                if world[n].type == 'WALL':
                    self.kill()

    def render(self) -> None:
        self.rect.topleft = self.x, self.y
        pygame.draw.rect(pygame.display.get_surface(),'yellow',self.rect,4)
        pygame.display.get_surface().blit(self.image, self.rect.topleft)

    def __blit(self, path: str, type: str, size: int) -> None:
        sprite = os.path.join(path, type)

        try:
            self.sprite = pygame.image.load(sprite).convert_alpha()
        except Exception as ex:
            print(ex)
            exit()

        self.image = self.sprite.subsurface((0, 0), (16, 16)).convert_alpha()

        #for n in range(size):
        #self.animation.append(self.sprite.subsurface((n * 16, 0), (16, 16)))
