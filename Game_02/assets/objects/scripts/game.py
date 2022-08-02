import os
import pygame
from pygame.locals import *
from assets.objects.scripts.player import Player
from assets.objects.scripts.world import World
from assets.objects.scripts.camera import Camera
from assets.objects.scripts.config import Configuration
from assets.objects.scripts.mouse import Mouse

class Game:

    def __init__(self) -> None:
        pygame.init()
        self.__load_assets()
        self.config = Configuration(self.__objects_dir)
        self.__screen_width, self.__screen_height = 800, 600
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        self.__game_clock = pygame.time.Clock()
        self.__game_running = True
        self.__cameraLock = True
        pygame.display.set_caption('Game_02D')

        self.__camera = Camera(self.get_Width(), self.get_Height(), self.__sprites_dir)
        self.__player = Player(self.__sprites_dir, self.__camera)
        self.__mouse = Mouse(self.__sprites_dir)
        self.new_world = World(self.__world_dir)
        self.world_list = self.new_world.new_world("map_test.png", self.__player)
        self.__camera.add(self.__mouse)
        self.__camera.add(self.world_list)
        #self.__enemys = []

    def game_loop(self) -> None:
        while self.__game_running:
            self.__game_clock.tick(30)
            self.__game_update()
            self.__game_render()

    def __game_render(self) -> None:
        self.__screen.fill((0, 0, 0))
        self.__player.player_render()
        self.__camera.update()
        self.__camera.custom_draw(self.__player, self.world_list, self.__mouse)
        pygame.display.flip()

    def __game_update(self) -> None:
        if self.__mouse.clicked:
            self.__mouse.clicked = False
            self.__camera.atk(self.__sprites_dir, self.__player)
        self.__get_events()
        self.__player.player_update()
        self.__player.is_free(self.world_list)
        self.__mouse.update_mouse()
        self.__camera.camera_update(self.__player.verify_cooldowns())


    def __get_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == MOUSEBUTTONDOWN:
                if not self.__mouse.clicked and not self.__player.get_attack() and not self.__player.get_holdweapon():
                    self.__mouse.clicked = True
                    self.__player.set_attack(True)
                    self.__player.set_atk_time(pygame.time.get_ticks())
                elif not self.__mouse.clicked and self.__player.get_holdweapon():
                    self.__camera.create_projectile(self.__mouse, self.__player)
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_q]:
                    if self.__player.cameraLock:
                        self.__player.cameraLock = False
                    else:
                        self.__player.cameraLock = True
                if pygame.key.get_pressed()[K_1]:
                    if not self.__player.get_holdweapon():
                        self.__player.set_holdweapon(True)
                    else:
                        self.__player.set_holdweapon(False)
                if pygame.key.get_pressed()[K_SPACE] and not self.__player.get_can_roll():
                    self.__player.set_roll(True)
                    self.__player.set_can_roll(True)
                    self.__player.set_roll_time(pygame.time.get_ticks())
                    #self.__player.index = 0
                elif event.key == K_w and not self.__player.get_roll():
                    if self.__player.get_roll():
                        self.__player.set_move(False)
                    else:
                        self.__player.set_dir(8)
                        self.__player.set_move(True)
                elif event.key == K_s:
                    if self.__player.get_roll():
                        self.__player.set_move(False)
                    else:
                        self.__player.set_dir(2)
                        self.__player.set_move(True)
                elif event.key == K_a:
                    if self.__player.get_roll():
                        self.__player.set_move(False)
                    else:
                        self.__player.set_dir(4)
                        self.__player.set_move(True)
                elif event.key == K_d:
                    if self.__player.get_roll():
                        self.__player.set_move(False)
                    else:
                        self.__player.set_dir(6)
                        self.__player.set_move(True)
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_SPACE] and not self.__player.get_roll():
                 print('pressed')
            if event.type == KEYUP:
                if event.key == K_w:
                    self.__player.set_move(False)
                elif event.key == K_s:
                    self.__player.set_move(False)
                elif event.key == K_a:
                    self.__player.set_move(False)
                elif event.key == K_d:
                    self.__player.set_move(False)

    def __load_assets(self) -> None:
        self.__assets_dir = os.path.join("assets")
        self.__objects_dir = os.path.join(self.__assets_dir, "objects")
        self.__world_dir = os.path.join(self.__objects_dir, "map")
        self.__sprites_dir = os.path.join(self.__objects_dir, "sprites")

    def get_Width(self) -> int:
        return self.__screen_width

    def get_Height(self) -> int:
        return self.__screen_height
