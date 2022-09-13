import math

import pygame.sprite
from assets.objects.scripts.mouse import Mouse
from assets.objects.scripts.player import Player
from assets.objects.scripts.tile import Tile
from assets.objects.scripts.weapon import Weapon
from assets.objects.scripts.projectile import projectile


class Camera(pygame.sprite.Group):

    def __init__(self, w: int, h: int, path: str) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_h = h / 2
        self.half_w = w / 2
        self.camera_border = {'left': 125, 'top': 150, 'bottom': 150, 'right': 125}
        left = self.camera_border['left']
        top = self.camera_border['top']
        width = self.display_surface.get_size()[0] - (self.camera_border['right'] + self.camera_border['left'])
        height = self.display_surface.get_size()[1] - (self.camera_border['top'] + self.camera_border['bottom'])
        self.box_camera = pygame.Rect(left, top, width, height)
        self.path = path
        self.weapon = None
        self.projetiles = []

    def custom_draw(self, player: Player, world: list[Tile], mouse: Mouse) -> None:
        self.__center_camera(player)
        offset_pos = (player.get_xPos() - self.offset.x, player.get_yPos() - self.offset.y)
        player.rect.topleft = offset_pos
        for n in range(len(world)):
            world[n].render(self.offset)
            self.display_surface.blit(world[n].image, world[n].rect.topleft)
            #pygame.draw.rect(self.display_surface, 'red', world[n].rect, 4)  # Tile box collide debug

        self.display_surface.blit(player.image, offset_pos)
        mouse.render(self.offset)
        pygame.draw.rect(self.display_surface, 'blue', player.rect, 4)  # Player box collide debug
        if self.weapon is not None:
            self.weapon.render(self.offset)
            #pygame.draw.rect(self.display_surface, 'red', self.weapon.rect, 4)
        if self.projetiles is not None:
            for n in range(len(self.projetiles)):
                self.projetiles[n].verify_collision(world)
                self.projetiles[n].render()

    def camera_update(self, op: int) -> None:
        if op == 2:
            self.__delete_atk()
        if self.projetiles is not None:
            for n in range(len(self.projetiles)):
                self.projetiles[n].update_projectile(self.offset)


    def create_projectile(self, mouse: Mouse, player: Player) -> None:
        #angle = math.degrees(math.atan(mouse.get_x() - (player.get_xPos() - self.offset.x)))
        #angle1 = math.degrees(math.atan(mouse.get_y() - (player.get_yPos() - self.offset.y)))
        angle = math.atan2(player.get_yPos() - (mouse.get_y() - self.offset.y), player.get_xPos() - (mouse.get_x() - self.offset.x))
        #print(angle)
        dx = math.cos(angle)
        dy = math.sin(angle)
        #print(dx, dy)
        self.projetiles.append(projectile(self.path, 'simple_arrow_placeholder.png', dx, dy, player))

    def atk(self, dir: str, player: Player) -> None:
        self.weapon = Weapon(dir, player.get_xPos() - self.offset.x, player.get_yPos() - self.offset.y, player.get_dir())
        player.set_atk_time(pygame.time.get_ticks())

    def __delete_atk(self) -> None:
        if self.weapon:
            self.weapon.kill()
        self.weapon = None

    def __center_camera(self, target: Player) -> None:
        if not target.cameraLock:
            if target.rect.left < self.box_camera.left:
                self.box_camera.left = target.rect.left + 1
            elif target.rect.right > self.box_camera.right:
                self.box_camera.right = target.rect.right + 1
            elif target.rect.top < self.box_camera.top:
                self.box_camera.top = target.rect.top - 1
            elif target.rect.bottom > self.box_camera.bottom:
                self.box_camera.bottom = target.rect.bottom + 1
            self.offset.x = self.box_camera.x - self.camera_border['left']
            self.offset.y = self.box_camera.y - self.camera_border['top']
        else:
            self.offset.x = target.rect.centerx - self.half_w
            self.offset.y = target.rect.centery - self.half_h
