import os.path
import pygame
from assets.objects.scripts.tile import Tile
#import threading


class Player(pygame.sprite.Sprite):

    def __init__(self, path: str, group: pygame.sprite.Group) -> None:
        super().__init__(group)
        pygame.sprite.Sprite.__init__(self)
        self.__dir = 2
        self.__pos_x = 0
        self.__pos_y = 0
        self.__spd = 2.4

        #CONTROLERS
            #BOOEANS
        self.__moving = False
        self.__attacking = False
        self.__rolling = False
        self.__can_roll = False
        self.hold_weapon = False
        self.cameraLock = True
        self.collision = {'up': False, 'down': False, 'right': False, 'left': False}
            #COOLDOWNS
        self.atk_cooldown = 600
        self.roll_cooldown = 1200
        self.roll_time = None
        self.atk_time = None

        #ANIMATIONS LISTS
        self.__walk_down = []
        self.__walk_up = []
        self.__walk_side = []
        self.__roll_down = []
        self.__roll_up = []
        self.__roll_side = []
        self.__atk_down = []
        self.__atk_up = []
        self.__atk_side = []
        self.__idle_down = []
        self.__idle_up = []
        self.__idle_side = []

        self.path = path
        self.__blit_sprites(self.path)

        self.index = 0
        self.image = self.__idle_down[self.index]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.__pos_x, self.__pos_y

    def player_update(self) -> None:
        if self.get_moving():
            if self.get_dir() == 8 and not self.collision['up']:
                self.set_yPos((self.get_yPos() - self.get_spd()))
                self.collision['down'] = False
                self.collision['right'] = False
                self.collision['left'] = False
            elif self.get_dir() == 2 and not self.collision['down']:
                self.set_yPos((self.get_yPos() + self.get_spd()))
                self.collision['up'] = False
                self.collision['left'] = False
                self.collision['right'] = False
            elif self.get_dir() == 4 and not self.collision['left']:
                self.set_xPos((self.get_xPos() - self.get_spd()))
                self.collision['right'] = False
                self.collision['up'] = False
                self.collision['down'] = False
            elif self.get_dir() == 6 and not self.collision['right']:
                self.set_xPos((self.get_xPos() + self.get_spd()))
                self.collision['left'] = False
                self.collision['up'] = False
                self.collision['down'] = False
        elif self.get_roll():
            if self.get_dir() == 8 and not self.collision['up']:
                self.set_yPos((self.get_yPos() - (2 * self.get_spd())))
            elif self.get_dir() == 2 and not self.collision['down']:
                self.set_yPos((self.get_yPos() + (2 * self.get_spd())))
            elif self.get_dir() == 4 and not self.collision['left']:
                self.set_xPos((self.get_xPos() - (2 * self.get_spd())))
            elif self.get_dir() == 6 and not self.collision['right']:
                self.set_xPos((self.get_xPos() + (2 * self.get_spd())))

    def verify_cooldowns(self) -> int:
        atual = pygame.time.get_ticks()
        if self.get_can_roll():
            if atual - self.roll_time >= self.roll_cooldown:
                self.set_can_roll(False)
                self.roll_time = None
                return 1
        if self.__attacking:
            if atual - self.atk_time >= self.atk_cooldown:
                self.__attacking = False
                self.atk_time = None
                return 2
        else:
            return 0


    def is_free(self, world: list[Tile]) -> None:
        for c in range(len(world)):
            if self.rect.colliderect(world[c].rect):
                if world[c].type == 'WALL':
                    if self.__dir == 4 or self.__dir == 6:
                        if world[c].rect.x > self.rect.x and world[c].rect.y > self.rect.y:
                            self.set_xPos(self.get_xPos() - 4)
                            self.collision['right'] = True
                        elif world[c].rect.x > self.rect.x and world[c].rect.y < self.rect.y:
                            self.set_xPos(self.get_xPos() - 4)
                            self.collision['right'] = True
                        elif world[c].rect.x < self.rect.x and world[c].rect.y > self.rect.y:
                            self.set_xPos(self.get_xPos() + 4)
                            self.collision['left'] = True
                        elif world[c].rect.x < self.rect.x and world[c].rect.y < self.rect.y:
                            self.set_xPos(self.get_xPos() + 4)
                            self.collision['left'] = True
                        elif world[c].rect.x > self.rect.x:
                            self.set_xPos(self.get_xPos() - 4)
                            self.collision['right'] = True
                        elif world[c].rect.x < self.rect.x:
                            self.set_xPos(self.get_xPos() + 4)
                            self.collision['left'] = True
                        elif world[c].rect.y > self.rect.y:
                            self.set_yPos(self.get_yPos() - 4)
                            self.collision['down'] = True
                        elif world[c].rect.y < self.rect.y:
                            self.set_yPos(self.get_yPos() + 4)
                            self.collision['up'] = True
                    else:
                        if world[c].rect.x > self.rect.x and world[c].rect.y > self.rect.y:
                            self.set_yPos(self.get_yPos() - 4)
                        elif world[c].rect.x > self.rect.x and world[c].rect.y < self.rect.y:
                            self.set_yPos(self.get_yPos() + 4)
                        elif world[c].rect.x < self.rect.x and world[c].rect.y > self.rect.y:
                            self.set_yPos(self.get_yPos() - 4)
                        elif world[c].rect.x < self.rect.x and world[c].rect.y < self.rect.y:
                            self.set_yPos(self.get_yPos() + 4)
                        elif world[c].rect.x > self.rect.x:
                            self.set_xPos(self.get_xPos() - 4)
                        elif world[c].rect.x < self.rect.x:
                            self.set_yPos(self.get_yPos() + 4)
                        elif world[c].rect.y > self.rect.y:
                            self.set_yPos(self.get_yPos() - 4)
                        elif world[c].rect.y < self.rect.y:
                            self.set_yPos(self.get_yPos() + 4)

    def player_render(self) -> None:
        if self.get_moving():
            if self.get_dir() == 8:
                if self.index >= len(self.__walk_up) - 1:
                    self.index = 0
                self.index += 0.5
                self.image = self.__walk_up[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 2:
                if self.index >= len(self.__walk_down) - 1:
                    self.index = 0
                self.index += 0.5
                self.image = self.__walk_down[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 4:
                if self.index >= len(self.__walk_side) - 1:
                    self.index = 0
                self.index += 0.5
                self.image = self.__walk_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 6:
                if self.index >= len(self.__walk_side) - 1:
                    self.index = 0
                self.index += 0.5
                self.image = self.__walk_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect.topleft = self.get_xPos(), self.get_yPos()
        elif self.get_roll():
            if self.get_dir() == 8:
                if self.index >= len(self.__roll_up) - 1:
                    self.index = 0
                    self.set_roll(False)
                self.index += 0.5
                self.image = self.__roll_up[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 2:
                if self.index >= len(self.__roll_down) - 1:
                    self.index = 0
                    self.set_roll(False)
                self.index += 0.5
                self.image = self.__roll_down[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 4:
                if self.index >= len(self.__roll_side) - 1:
                    self.index = 0
                    self.set_roll(False)
                    self.set_move(False)
                self.index += 0.5
                self.image = self.__roll_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 6:
                if self.index >= len(self.__roll_side) - 1:
                    self.index = 0
                    self.set_roll(False)
                    self.set_move(False)
                self.index += 0.5
                self.image = self.__roll_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect.topleft = self.get_xPos(), self.get_yPos()
        elif self.get_attack():
            if self.get_dir() == 8:
                pass
            elif self.get_dir() == 2:
                pass
            elif self.get_dir() == 4:
                pass
            elif self.get_dir() == 6:
                pass
        else:
            if self.get_dir() == 8:
                if self.index >= len(self.__idle_up) - 1:
                    self.index = 0
                self.index += 0.5
                self.image = self.__idle_up[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 2:
                if self.index >= len(self.__idle_down) - 1:
                    self.index = 0
                self.index += 0.08
                self.image = self.__idle_down[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 4:
                if self.index >= len(self.__idle_side) - 1:
                    self.index = 0
                self.index += 0.08
                self.image = self.__idle_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.rect.topleft = self.get_xPos(), self.get_yPos()
            elif self.get_dir() == 6:
                if self.index >= len(self.__idle_side) - 1:
                    self.index = 0
                self.index += 0.08
                self.image = self.__idle_side[int(self.index)]
                self.image = pygame.transform.scale(self.image, (64, 64))
                self.image = pygame.transform.flip(self.image, True, False)
                self.rect.topleft = self.get_xPos(), self.get_yPos()

    def __blit_sprites(self, path: str) -> None:
        try:
            roll = os.path.join(path, "roll_place_holder.png")
            self.sprite = pygame.image.load(roll).convert_alpha()

            for i in range(8):
                self.__roll_down.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
                self.__roll_up.append(self.sprite.subsurface((i * 32, 64), (32, 32)))
            for i in range(7):
                self.__roll_side.append(self.sprite.subsurface((i * 32, 32), (32, 32)))

            walk = os.path.join(path, "walk_placeHolder.png")
            self.sprite = pygame.image.load(walk).convert_alpha()
            for i in range(10):
                self.__walk_down.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
                self.__walk_side.append(self.sprite.subsurface((i * 32, 32), (32, 32)))
                self.__walk_up.append(self.sprite.subsurface((i * 32, 64), (32, 32)))

            idle = os.path.join(path, "idle_place_holder.png")
            self.sprite = pygame.image.load(idle).convert_alpha()
            for i in range(3):
                self.__idle_down.append(self.sprite.subsurface((i * 32, 0), (32, 32)))
                self.__idle_side.append(self.sprite.subsurface((i * 32, 32), (32, 32)))
                self.__idle_up.append(self.sprite.subsurface((i * 32, 64), (32, 32)))

        except Exception as exception:
            print(exception)

    def reseter_map(self, x: float, y: float) -> None:
        self.set_xPos(x)
        self.set_yPos(y)
        self.rect.topleft = x, y

    #GETTERS
    def get_moving(self) -> bool:
        return self.__moving

    def get_dir(self) -> int:
        return self.__dir

    def get_attack(self) -> bool:
        return self.__attacking

    def get_roll(self) -> bool:
        return self.__rolling

    def get_xPos(self) -> float:
        return self.__pos_x

    def get_yPos(self) -> float:
        return self.__pos_y

    def get_spd(self) -> float:
        return self.__spd

    def get_can_roll(self) -> bool:
        return self.__can_roll

    def get_holdweapon(self) -> bool:
        return self.hold_weapon

    #SETTERS
    def set_roll_time(self, time: float) -> None:
        self.roll_time = time

    def set_atk_time(self, time: float) -> None:
        self.atk_time = time

    def set_dir(self, direction: int) -> None:
        self.__dir = direction

    def set_move(self, move: bool) -> None:
        self.__moving = move

    def set_attack(self, atk: bool) -> None:
        self.__attacking = atk

    def set_roll(self, roll: bool) -> None:
        self.__rolling = roll

    def set_xPos(self, x: float) -> None:
        self.__pos_x = x

    def set_yPos(self, y: float) -> None:
        self.__pos_y = y

    def set_spd(self, spd: float) -> None:
        self.__spd = spd

    def set_can_roll(self, canroll: bool) -> None:
        self.__can_roll = canroll

    def set_holdweapon(self, hw: bool) -> None:
        self.hold_weapon = hw
