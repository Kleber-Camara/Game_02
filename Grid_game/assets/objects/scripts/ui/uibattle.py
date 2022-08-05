from assets.objects.scripts.ui.selectarrow import SelectArrow
from assets.objects.scripts.ui.selectmove import SelectMove
from assets.objects.scripts.ui.button import Button
from assets.objects.scripts.system.player import Player
import pygame.sprite
import pygame


class UiBattle(pygame.sprite.Sprite):

    def __init__(self, player: Player) -> None:
        super().__init__()
        self.player = player
        self.btns = []
        self.__box_action = pygame.Rect(0, 400, (pygame.display.get_surface().get_size()[0]),
                                        (pygame.display.get_surface().get_size()[1]-400))
        self.__selected_btn = None
        self._arrow = SelectArrow(self.player.path, 0, 0)
        self.__move_target = SelectMove(self.player.path, 0, 0)
        self.__can_see_target = False
        self.__selected_tile = None

    def draw(self) -> None:

        if self.__selected_btn is not None:
            self._arrow.move(self.__selected_btn.get_x()-5, self.__selected_btn.get_y()+5)
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), self.__box_action)
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), self.__box_action, 2)
        pygame.draw.rect(pygame.display.get_surface(), (255, 125, 0), (self.__box_action.x+5,
                                                                       self.__box_action.y+3, 200,
                                                                       self.__box_action.height-10), 2)
        if self.player.get_selected():
            if not self.btns:
                btn1 = Button(35, 410, 120, 30, 'Mover', (255, 255, 255), 24)
                btn2 = Button(35, 450, 120, 30, 'Atacar', (255, 255, 255), 24)
                btn3 = Button(35, 490, 120, 30, 'Itens', (255, 255, 255), 24)
                btn4 = Button(35, 530, 120, 30, 'Fugir', (255, 255, 255), 24)
                self.btns.append(btn1)
                self.btns.append(btn2)
                self.btns.append(btn3)
                self.btns.append(btn4)
        else:
            self.btns.clear()

        for btn in self.btns:
            btn.render()

        if self.__selected_btn is not None:
            self._arrow.render()

        if self.__can_see_target:
            self.__move_target.render()

    def navigate_ui(self, direction: bool) -> None:

        if self.__selected_btn is not None:
            for i in range(len(self.btns)):
                if self.__selected_btn == self.btns[i]:
                    if direction:
                        if i+1 >= len(self.btns):
                            self.__selected_btn = self.btns[0]
                            break
                        else:
                            self.__selected_btn = self.btns[i+1]
                            break
                    else:
                        if i-1 < 0:
                            self.__selected_btn = self.btns[len(self.btns)-1]
                            break
                        else:
                            self.__selected_btn = self.btns[i-1]
                            break
        else:
            self.__selected_btn = self.btns[0]

    def select_keyboard_options(self) -> str:
        if self.__selected_btn is not None:
            return self.__selected_btn.name

    def end_arrow(self) -> None:
        self.__selected_btn = None
        self.__can_see_target = False

    def get_selected_button(self) -> Button:
        return self.__selected_btn

    @staticmethod
    def get_min_max_moveY(tile_list: list) -> tuple:
        min_y = 9999
        max_y = 0
        for i in range(len(tile_list)):
            if tile_list[i].get_can_move():
                if tile_list[i].get_y() < min_y:
                    min_y = tile_list[i].get_y()
                elif tile_list[i].get_y() > max_y:
                    max_y = tile_list[i].get_y()
        return min_y, max_y

    @staticmethod
    def get_min_max_moveX(tile_list: list) -> tuple:
        min_x = 9999
        max_x = 0
        for i in range(len(tile_list)):
            if tile_list[i].get_can_move():
                if tile_list[i].get_x() < min_x:
                    min_x = tile_list[i].get_x()
                elif tile_list[i].get_x() > max_x:
                    max_x = tile_list[i].get_x()
        return min_x, max_x

    def move_target(self, x: int, y: int) -> None:
        self.__move_target.move(x, y)

    def get_move_target_x(self) -> int:
        return self.__move_target.get_x()

    def get_move_target_y(self) -> int:
        return self.__move_target.get_y()

    def change_can_see(self, target: bool) -> None:
        self.__can_see_target = target

    def get_can_see(self) -> bool:
        return self.__can_see_target
