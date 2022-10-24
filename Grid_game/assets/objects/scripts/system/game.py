import random

from assets.objects.scripts.skill.instanceSkill import InstanceSkills
from assets.objects.scripts.ui.selectmove import SelectMove
from assets.objects.scripts.characters.char1 import Char1
from assets.objects.scripts.characters.char2 import Char2
from assets.objects.scripts.ui.uibattle import UiBattle
from assets.objects.scripts.system.player import Player
from assets.objects.scripts.system.mouse import Mouse
from assets.objects.scripts.system.newMap import Map
import pygame.display
import os.path


class Game:

    def __init__(self) -> None:
        self.__get_paths()
        self.__sWidth, self.__sHeight = 800, 600
        self.__display = pygame.display.set_mode((self.__sWidth, self.__sHeight))
        self.__clock = pygame.time.Clock()
        self.__run = True
        self.__game_mode = {'battle': True, 'management': False}
        self.__status = {'ingame': True, 'menu': False}
        self.__turn = False

        # variables to test
        self.__char = Char1(self.__sprites_path)
        self.__char2 = Char2(self.__sprites_path)
        self.__mouse = Mouse(self.__sprites_path)
        self.__map = Map(self.__sprites_path)
        self.__enemy_list = []
        self.__tile_list = self.__map.new_map('map_test1.png', self.__enemy_list)
        self.__player = Player(self.__sprites_path)
        self.__player.append_group(self.__char)
        self.__player.append_group(self.__char2)
        self.__ui_b = UiBattle(self.__player)
        self.__move_arrow = SelectMove(self.__sprites_path, 0, 0)
        self.__can_see_arrow = False
        self.__tile_select = None
        self.__skill = None

    def game_loop(self) -> None:
        while self.__run:
            self.__clock.tick(30)
            self.__game_render()
            self.__game_update()

    def __game_render(self) -> None:
        self.__display.fill((0, 0, 0))
        if self.__status['ingame']:
            for n in range(len(self.__tile_list)):
                self.__tile_list[n].render()
            if self.__enemy_list is not None:
                for enemy in self.__enemy_list:
                    enemy.render()
            self.__player.render()
            if self.__skill is not None:
                self.__skill.render()
            self.__ui_b.draw()
            for enemy in self.__enemy_list:
                self.__ui_b.draw_enemy_life(self.__mouse.rect, enemy)
            if not self.__enemy_list:
                self.__ui_b.erase_enemy_bar()
        self.__mouse.render()
        pygame.display.update()

    def __game_update(self) -> None:
        if self.__status['ingame']:
            if self.__turn_verify():
                self.__get_input()
            else:
                for enemy in self.__enemy_list:
                    enemy.update()
                self.__player.all_unmoved()
                self.__turn_verify()
            self.__mouse.update_mouse()
            self.__player.update(self.__tile_list, self.__enemy_list)
            if self.__ui_b.get_can_see():
                for i in range(len(self.__tile_list)):
                    if self.__mouse.rect.colliderect(self.__tile_list[i]):
                        if self.__tile_list[i].get_can_move():
                            self.__ui_b.move_target(self.__tile_list[i].get_x(), self.__tile_list[i].get_y())
            if self.__skill is not None:
                self.__skill.update_skill()
                if self.__skill.get_destruction():
                    self.__skill = None
            for enemy_s in self.__enemy_list:
                if enemy_s.get_present_health() <= 0:
                    self.__enemy_list.remove(enemy_s)

    def __get_input(self) -> None:
        for event in pygame.event.get():    # Recebe os eventos que estão acontecendo no loop do jogo
            if event.type == pygame.QUIT:   # Verifica se o usuario fechou o jogo e finaliza os processos
                pygame.quit()               # Fecha a aplicação
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    # Verifica se os botões do __mouse foram pressionados
                if self.__player.get_selected() is not None:  # Verifica se há algum heroi selecionado
                    if self.__ui_b.btns is not None:    # Verifica se a lista de botões de ações esta vazia
                        for i in range(len(self.__ui_b.btns)):  # Cria uma lista de botões com as ações do player
                            if self.__mouse.rect.colliderect(self.__ui_b.btns[i].get_rect()):   # Verifica se o __mouse esta colidindo com algum botão
                                if self.__ui_b.btns[i].get_name() == 'Mover':     # Verifica se o nome do botão é mover
                                    self.__changeButtonMove(True)
                                    if self.__ui_b.get_skills_b():
                                        self.__ui_b.set_skills_Bfree()
                                elif self.__ui_b.btns[i].get_name() == 'Atacar':
                                    self.__changeButtonMove(False)
                                    self.__ui_b.skills_btns_create(self.__player.get_selected().get_skills_list())
                        for btn in self.__ui_b.get_skills_b():
                            if self.__mouse.rect.colliderect(btn.get_rect()):
                                self.__player.get_selected().set_atacking(True)
                                self.__player.set_floor_target(self.__tile_list,
                                                               InstanceSkills(btn.get_name()).instanceSkill(0, 0))

                    self.__player.verify_selection(self.__mouse.rect)
                    for i in range(len(self.__tile_list)):
                        if self.__mouse.rect.colliderect(self.__tile_list[i].rect) and self.__tile_list[i].get_can_move():
                            if self.__player.get_selected() is not None:
                                if self.__player.get_selected().get_moving():
                                    self.__player.move_hero(self.__tile_list[i].get_x(), self.__tile_list[i].get_y())
                                    self.__ui_b.end_arrow()
                        if self.__mouse.rect.colliderect(self.__tile_list[i].rect) and self.__tile_list[i].get_can_atk():
                            if self.__player.get_selected() is not None:
                                if self.__player.get_selected().get_atk_status():
                                    self.__skill = InstanceSkills(btn.get_name()).instanceSkill(
                                        self.__tile_list[i].get_x(), self.__tile_list[i].get_y())
                                    self.__player.get_selected().set_atacking(False)
                                    self.__player.setting_tiles_not_atk(self.__tile_list)
                                    self.__ui_b.end_arrow()
                                    self.__ui_b.end_ui()
                                    self.__player.get_selected().set_moved(True)
                                    self.__calculate_damage()
                                    self.__player.clean_selection()
                else:
                    self.__player.verify_selection(self.__mouse.rect)
                    self.__ui_b.draw_player_info(self.__player.get_selected())
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.__ui_b.get_can_see():
                        min_y, max_y = self.__ui_b.get_min_max_moveY(self.__tile_list)
                        move = 32
                        while self.__pos_verify(self.__ui_b.get_move_target_x(),
                                                self.__ui_b.get_move_target_y() + move):
                            move += 32
                        if (self.__ui_b.get_move_target_y() + move) > max_y:
                            if self.__pos_verify(self.__ui_b.get_move_target_x(), max_y):
                                move = 0
                                while self.__pos_verify(self.__ui_b.get_move_target_x(), min_y + move):
                                    move += 32
                                self.__ui_b.move_target(self.__ui_b.get_move_target_x(), min_y + move)
                            else:
                                self.__ui_b.move_target(self.__ui_b.get_move_target_x(), min_y)
                            break
                        else:
                            self.__ui_b.move_target(self.__ui_b.get_move_target_x(),
                                                    self.__ui_b.get_move_target_y() + move)
                            break

                    elif self.__player.get_selected() is None:
                        self.__player.nextSelection(True)
                    else:
                        self.__ui_b.navigate_ui(True)
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.__ui_b.get_can_see():
                        min_y, max_y = self.__ui_b.get_min_max_moveY(self.__tile_list)
                        move = 32
                        while self.__pos_verify(self.__ui_b.get_move_target_x(),
                                                self.__ui_b.get_move_target_y() - move):
                            move += 32
                        if (self.__ui_b.get_move_target_y() - move) < min_y:
                            if self.__pos_verify(self.__ui_b.get_move_target_x(), max_y):
                                move = 0
                                while self.__pos_verify(self.__ui_b.get_move_target_x(), max_y - move):
                                    move += 32
                                self.__ui_b.move_target(self.__ui_b.get_move_target_x(), max_y - move)
                            else:
                                self.__ui_b.move_target(self.__ui_b.get_move_target_x(), max_y)
                            break
                        else:
                            self.__ui_b.move_target(self.__ui_b.get_move_target_x(),
                                                    self.__ui_b.get_move_target_y() - move)
                            break
                    elif self.__player.get_selected() is None:
                        self.__player.nextSelection(False)
                    else:
                        self.__ui_b.navigate_ui(False)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.__ui_b.get_can_see():
                        min_x, max_x = self.__ui_b.get_min_max_moveX(self.__tile_list)
                        move = 32
                        while self.__pos_verify(self.__ui_b.get_move_target_x() + move,
                                                self.__ui_b.get_move_target_y()):
                            move += 32
                        if (self.__ui_b.get_move_target_x() + move) > max_x:
                            if self.__pos_verify(min_x, self.__ui_b.get_move_target_y()):
                                move = 0
                                while self.__pos_verify(min_x + move, self.__ui_b.get_move_target_y()):
                                    move += 32
                                self.__ui_b.move_target(min_x + move, self.__ui_b.get_move_target_y())
                            else:
                                self.__ui_b.move_target(min_x, self.__ui_b.get_move_target_y())
                            break
                        else:
                            self.__ui_b.move_target(self.__ui_b.get_move_target_x() + move,
                                                    self.__ui_b.get_move_target_y())
                            break
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if self.__ui_b.get_can_see():
                        min_x, max_x = self.__ui_b.get_min_max_moveX(self.__tile_list)
                        move = 32
                        while self.__pos_verify(self.__ui_b.get_move_target_x() - move,
                                                self.__ui_b.get_move_target_y()):
                            move += 32
                        if (self.__ui_b.get_move_target_x() - move) < min_x:
                            if self.__pos_verify(max_x, self.__ui_b.get_move_target_y()):
                                move = 0
                                while self.__pos_verify(max_x - move, self.__ui_b.get_move_target_y()):
                                    move += 32
                                self.__ui_b.move_target(max_x - move, self.__ui_b.get_move_target_y())
                            else:
                                self.__ui_b.move_target(max_x, self.__ui_b.get_move_target_y())
                            break
                        else:
                            self.__ui_b.move_target(self.__ui_b.get_move_target_x() - move,
                                                    self.__ui_b.get_move_target_y())
                            break
                if event.key == pygame.K_RETURN:
                    if self.__ui_b.get_can_see():
                        self.__player.get_selected().set_moving(False)
                        self.__ui_b.change_can_see(False)
                        self.__player.move_hero(self.__ui_b.get_move_target_x(), self.__ui_b.get_move_target_y())
                        self.__ui_b.end_arrow()
                        self.__player.clean_selection()
                        self.__player.nextSelection(True)
                        break
                    elif self.__ui_b.get_selected_button() is None and self.__player.get_selected() is not None:
                        self.__ui_b.navigate_ui(True)
                    elif self.__player.get_present_selection() is None:
                        self.__player.nextSelection(True)
                        self.__player.real_select()
                    else:
                        self.__player.real_select()
                        if self.__ui_b.get_selected_button() is not None:
                            if self.__ui_b.get_selected_button().get_name() == 'Mover':
                                self.__ui_b.change_can_see(True)
                                self.__ui_b.move_target(self.__player.get_selected().get_x(),
                                                        self.__player.get_selected().get_y())
                                self.__player.get_selected().set_moving(True)
                                break

                if event.key == pygame.K_ESCAPE:
                    if self.__can_see_arrow:
                        self.__can_see_arrow = False
                        self.__player.get_selected().set_moving(False)
                    elif self.__player.get_selected():
                        self.__player.clean_selection()
                        if self.__ui_b.get_selected_button() is not None:
                            self.__ui_b.end_arrow()

    def __turn_verify(self) -> bool:
        if not self.__player.all_moved():
            self.__turn = True
        else:
            self.__turn = False
        return self.__turn

    def __pos_verify(self, x: int, y: int) -> bool:
        for i in range(len(self.__tile_list)):
            if self.__tile_list[i].get_x() == x and self.__tile_list[i].get_y() == y:
                if self.__tile_list[i].get_can_move() is False:
                    return True
                else:
                    return False

    def __changeButtonMove(self, status: bool) -> None:
        if self.__player.get_selected() is not None:
            self.__player.get_selected().set_moving(status)  # Marca o heroi selecionado como um heroi em movimento
            self.__ui_b.change_can_see(status)
            self.__player.get_selected().set_atacking(not status)
            if status:
                self.__player.setting_tiles_not_atk(self.__tile_list)

    def get_collide_detection(self, rect1: pygame.rect, rect2: pygame.rect) -> bool:
        if rect1.colliderect(rect2):
            return True
        else:
            return False

    def __calculate_damage(self) -> None:
        if self.__skill is not None:
            for enemy_collide in self.__enemy_list:
                if self.get_collide_detection(self.__skill.rect, enemy_collide.rect):
                    if self.__skill.get_can_damage():
                        self.__skill.set_damage_status(False)
                        if self.__player.get_selected() is not None:
                            print(self.__player.get_selected().get_damage())
                            if random.randrange(1, 100) <= enemy_collide.get_dodge():
                                enemy_collide.make_damage(self.__skill.get_damage() + self.__player.get_selected().get_damage(), self.__skill.get_type())

    def __get_paths(self) -> None:
        self.__assets_path = os.path.join('assets')
        self.__objects_path = os.path.join(self.__assets_path, 'objects')
        self.__sprites_path = os.path.join(self.__assets_path, 'sprites')
        self.__map_path = os.path.join(self.__sprites_path, 'map')
        self.__scripts_path = os.path.join(self.__objects_path, 'scripts')
