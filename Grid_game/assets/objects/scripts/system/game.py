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
        self.clock = pygame.time.Clock()
        self.__run = True
        self.__state = {'battle': True, 'management': False}
        self._turn = False

        # variables to test
        self.char = Char1(self.__sprites_path)
        self.char2 = Char2(self.__sprites_path)
        self.mouse = Mouse(self.__sprites_path)
        self.map = Map(self.__sprites_path)
        self.enemy_list = []
        self.tile_list = self.map.new_map('map_test1.png', self.enemy_list)
        self.player = Player(self.__sprites_path)
        self.player.append_group(self.char)
        self.player.append_group(self.char2)
        self.__ui_b = UiBattle(self.player)
        self.__move_arrow = SelectMove(self.__sprites_path, 0, 0)
        self.__can_see_arrow = False
        self.__tile_select = None

    def game_loop(self) -> None:
        while self.__run:
            self.clock.tick(30)
            self.__game_render()
            self.__game_update()

    def __game_render(self) -> None:
        self.__display.fill((0, 0, 0))
        for n in range(len(self.tile_list)):
            self.tile_list[n].render()
        if self.enemy_list is not None:
            for enemy in self.enemy_list:
                enemy.render()
        self.player.render()
        self.__ui_b.draw()
        self.mouse.render()
        pygame.display.update()

    def __game_update(self) -> None:
        if self.turn_verify():
            self.__get_input()
        else:
            for enemy in self.enemy_list:
                enemy.update()
            self.player.all_unmoved()
            self.turn_verify()
        self.mouse.update_mouse()
        self.player.update(self.tile_list, self.enemy_list)
        if self.__ui_b.get_can_see():
            for i in range(len(self.tile_list)):
                if self.mouse.rect.colliderect(self.tile_list[i]):
                    if self.tile_list[i].get_can_move():
                        self.__ui_b.move_target(self.tile_list[i].get_x(), self.tile_list[i].get_y())

    def __get_input(self) -> None:
        for event in pygame.event.get():    # Recebe os eventos que estão acontecendo no loop do jogo
            if event.type == pygame.QUIT:   # Verifica se o usuario fechou o jogo e finaliza os processos
                pygame.quit()               # Fecha a aplicação
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:    # Verifica se os botões do mouse foram pressionados
                if self.player.get_selected() is not None:  # Verifica se há algum heroi selecionado
                    if self.__ui_b.btns is not None:    # Verifica se a lista de botões de ações esta vazia
                        for i in range(len(self.__ui_b.btns)):  # Cria uma lista de botões com as ações do player
                            if self.mouse.rect.colliderect(self.__ui_b.btns[i].rect):   # Verifica se o mouse esta colidindo com algum botão
                                if self.__ui_b.btns[i].name == 'Mover':     # Verifica se o nome do botão é mover
                                    self.player.get_selected().set_moving(True) # Marca o heroi selecionado como um heroi em movimento
                                    self.__ui_b.change_can_see(True)
                    self.player.verify_selection(self.mouse.rect)
                    for i in range(len(self.tile_list)):
                        if self.mouse.rect.colliderect(self.tile_list[i].rect) and self.tile_list[i].get_can_move():
                            if self.player.get_selected() is not None:
                                if self.player.get_selected().get_moving():
                                    self.player.move_hero(self.tile_list[i].get_x(), self.tile_list[i].get_y())
                                    self.__ui_b.end_arrow()
                else:
                    self.player.verify_selection(self.mouse.rect)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if self.__ui_b.get_can_see():
                        min_y, max_y = self.__ui_b.get_min_max_moveY(self.tile_list)
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

                    elif self.player.get_selected() is None:
                        self.player.nextSelection(True)
                    else:
                        self.__ui_b.navigate_ui(True)
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if self.__ui_b.get_can_see():
                        min_y, max_y = self.__ui_b.get_min_max_moveY(self.tile_list)
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
                    elif self.player.get_selected() is None:
                        self.player.nextSelection(False)
                    else:
                        self.__ui_b.navigate_ui(False)
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if self.__ui_b.get_can_see():
                        min_x, max_x = self.__ui_b.get_min_max_moveX(self.tile_list)
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
                        min_x, max_x = self.__ui_b.get_min_max_moveX(self.tile_list)
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
                        self.player.get_selected().set_moving(False)
                        self.__ui_b.change_can_see(False)
                        self.player.move_hero(self.__ui_b.get_move_target_x(), self.__ui_b.get_move_target_y())
                        self.__ui_b.end_arrow()
                        self.player.clean_selection()
                        self.player.nextSelection(True)
                        break
                    elif self.__ui_b.get_selected_button() is None and self.player.get_selected() is not None:
                        self.__ui_b.navigate_ui(True)
                    elif self.player.get_present_selection() is None:
                        self.player.nextSelection(True)
                        self.player.real_select()
                    else:
                        self.player.real_select()
                        if self.__ui_b.get_selected_button() is not None:
                            if self.__ui_b.get_selected_button().name == 'Mover':
                                self.__ui_b.change_can_see(True)
                                self.__ui_b.move_target(self.player.get_selected().get_x(),
                                                        self.player.get_selected().get_y())
                                self.player.get_selected().set_moving(True)
                                break

                if event.key == pygame.K_ESCAPE:
                    if self.__can_see_arrow:
                        self.__can_see_arrow = False
                        self.player.get_selected().set_moving(False)
                    elif self.player.get_selected():
                        self.player.clean_selection()
                        if self.__ui_b.get_selected_button() is not None:
                            self.__ui_b.end_arrow()

    def turn_verify(self) -> bool:
        if not self.player.all_moved():
            self._turn = True
        else:
            self._turn = False
        return self._turn

    def __pos_verify(self, x: int, y: int) -> bool:
        for i in range(len(self.tile_list)):
            if self.tile_list[i].get_x() == x and self.tile_list[i].get_y() == y:
                if self.tile_list[i].get_can_move() is False:
                    return True
                else:
                    return False

    def __get_paths(self) -> None:
        self.__assets_path = os.path.join('assets')
        self.__objects_path = os.path.join(self.__assets_path, 'objects')
        self.__sprites_path = os.path.join(self.__assets_path, 'sprites')
        self.__map_path = os.path.join(self.__sprites_path, 'map')
        self.__scripts_path = os.path.join(self.__objects_path, 'scripts')
