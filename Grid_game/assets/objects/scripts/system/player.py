from assets.objects.scripts.ui.selectarrow import SelectArrow
from assets.objects.scripts.characters.heroes import Heroes
from assets.objects.scripts.tiles.rock import Rock
from assets.objects.scripts.skill.skill import Skill
import pygame


class Player:

    def __init__(self, path: str) -> None:
        self.__selected = None
        self.__heroes_list = []
        self.__menu_action = []
        self.__arrow = SelectArrow(path, 0, 0)
        self.__present_selection = None
        self.path = path

    def update(self, tiles: list, enemys: list) -> None:
        can_move = True
        if self.__present_selection is not None:
            self.__arrow.move(self.__present_selection.get_x(), self.__present_selection.get_y() - 10)
        if self.__selected and self.__selected.get_moving():
            for i in range(len(tiles)):
                if self.__selected.get_x() >= tiles[i].get_x() >= self.__selected.get_x() - (
                        32 * self.__selected.get_move()) \
                        and self.__selected.get_y() <= tiles[i].get_y() <= self.__selected.get_y() + (
                        32 * self.__selected.get_move()):
                    for enemy in enemys:
                        if enemy.get_x() == tiles[i].get_x() and enemy.get_y() == tiles[i].get_y():
                            can_move = False
                            break
                        else:
                            can_move = True
                    if not isinstance(tiles[i], Rock) and can_move:
                        tiles[i].set_can_move()
                    for hero in self.__heroes_list:
                        if hero.get_x() == tiles[i].get_x() and hero.get_y() == tiles[i].get_y():
                            tiles[i].set_cannot_move()
                if self.__selected.get_x() >= tiles[i].get_x() >= self.__selected.get_x() - (
                        32 * self.__selected.get_move()) \
                        and self.__selected.get_y() >= tiles[i].get_y() >= self.__selected.get_y() - (
                        32 * self.__selected.get_move()):
                    for enemy in enemys:
                        if enemy.get_x() == tiles[i].get_x() and enemy.get_y() == tiles[i].get_y():
                            can_move = False
                            break
                        else:
                            can_move = True
                    if not isinstance(tiles[i], Rock) and can_move:
                        tiles[i].set_can_move()
                    for hero in self.__heroes_list:
                        if hero.get_x() == tiles[i].get_x() and hero.get_y() == tiles[i].get_y():
                            tiles[i].set_cannot_move()
                if self.__selected.get_x() < tiles[i].get_x() <= self.__selected.get_x() + (
                        32 * self.__selected.get_move()) \
                        and self.__selected.get_y() <= tiles[i].get_y() <= self.__selected.get_y() + (
                        32 * self.__selected.get_move()):
                    for enemy in enemys:
                        if enemy.get_x() == tiles[i].get_x() and enemy.get_y() == tiles[i].get_y():
                            can_move = False
                            break
                        else:
                            can_move = True
                    if not isinstance(tiles[i], Rock) and can_move:
                        tiles[i].set_can_move()
                    for hero in self.__heroes_list:
                        if hero.get_x() == tiles[i].get_x() and hero.get_y() == tiles[i].get_y():
                            tiles[i].set_cannot_move()
                if self.__selected.get_x() < tiles[i].get_x() <= self.__selected.get_x() + (
                        32 * self.__selected.get_move()) \
                        and self.__selected.get_y() > tiles[i].get_y() >= self.__selected.get_y() - (
                        32 * self.__selected.get_move()):
                    for enemy in enemys:
                        if enemy.get_x() == tiles[i].get_x() and enemy.get_y() == tiles[i].get_y():
                            can_move = False
                            break
                        else:
                            can_move = True
                    if not isinstance(tiles[i], Rock) and can_move:
                        tiles[i].set_can_move()
                    for hero in self.__heroes_list:
                        if hero.get_x() == tiles[i].get_x() and hero.get_y() == tiles[i].get_y():
                            tiles[i].set_cannot_move()
                for n in range(len(self.__heroes_list)):
                    if self.__heroes_list[n].get_x() == tiles[i].get_x():
                        if self.__heroes_list[n].get_y() == tiles[i].get_y():
                            tiles[i].set_cannot_move()
        else:
            for i in range(len(tiles)):
                tiles[i].set_cannot_move()
        for i in range(len(self.__heroes_list)):
            self.__heroes_list[i].update_hero()

    def render(self) -> None:
        for i in range(len(self.__heroes_list)):
            self.__heroes_list[i].render()
        if self.__present_selection is not None:
            self.__arrow.render()

    def move_hero(self, x: int, y: int) -> None:
        if self.__selected is not None:
            self.__selected.set_x(x)
            self.__selected.set_y(y)
            self.__selected.set_moving(False)
            self.__selected.set_moved(True)
            self.clean_selection()

    def verify_selection(self, rect: pygame.rect) -> None:
        for i in range(len(self.__heroes_list)):
            if self.__heroes_list[i].rect.colliderect(rect) and not self.__heroes_list[i].get_moved():
                if self.__selected:
                    self.__selected = None
                else:
                    self.__selected = self.__heroes_list[i]
                    self.__present_selection = self.__heroes_list[i]

    def append_group(self, hero: Heroes) -> None:
        if len(self.__heroes_list) <= 4:
            self.__heroes_list.append(hero)

    def clean_selection(self) -> None:
        self.__selected = None

    def nextSelection(self, direction: bool) -> None:
        if self.__present_selection is not None:
            for i in range(len(self.__heroes_list)):
                if self.__present_selection == self.__heroes_list[i]:
                    if direction:
                        if i+1 >= len(self.__heroes_list) and self.__heroes_list[i].get_moved():
                            self.__present_selection = self.__heroes_list[0]
                            break
                        else:
                            if (i + 1) < len(self.__heroes_list):
                                if self.__heroes_list[i + 1].get_moved():
                                    if i + 1 > len(self.__heroes_list):
                                        self.__present_selection = self.__heroes_list[0]
                                    else:
                                        self.__present_selection = self.__heroes_list[i + 1]
                                    self.nextSelection(direction)
                                else:
                                    self.__present_selection = self.__heroes_list[i + 1]
                            else:
                                self.__present_selection = self.__heroes_list[0]
                                if self.__present_selection.get_moved():
                                    self.nextSelection(direction)
                            break
                    else:
                        if i-1 < 0 and self.__heroes_list[i].get_moved():
                            self.__present_selection = self.__heroes_list[len(self.__heroes_list) - 1]
                            break
                        else:
                            if i-1 <= 0:
                                if self.__heroes_list[len(self.__heroes_list) - 1].get_moved():
                                    if i-1 < 0:
                                        self.__present_selection = self.__heroes_list[len(self.__heroes_list) - 1]
                                        if self.__present_selection.get_moved():
                                            self.nextSelection(direction)
                                    else:
                                        self.__present_selection = self.__heroes_list[i - 1]
                                    if self.__present_selection.get_moved():
                                        self.nextSelection(direction)
                                else:
                                    self.__present_selection = self.__heroes_list[i - 1]
                                    if self.__present_selection.get_moved():
                                        self.nextSelection(direction)
                            else:
                                self.__present_selection = self.__heroes_list[len(self.__heroes_list) - 1]
                                if self.__present_selection.get_moved():
                                    self.nextSelection(direction)
                            break
        else:
            self.__present_selection = self.__heroes_list[0]

    def real_select(self) -> None:
        if self.__present_selection is not None:
            self.__selected = self.__present_selection

    def get_selected(self) -> Heroes:
        return self.__selected

    def get_present_selection(self) -> Heroes:
        return self.__present_selection

    def all_unmoved(self) -> None:
        for char in self.__heroes_list:
            char.set_moved(False)

    def all_moved(self) -> bool:
        count = 0
        for char in self.__heroes_list:
            if char.get_moved():
                count += 1
                print(count)
        if count >= len(self.__heroes_list):
            return True
        else:
            return False

    def set_floor_target(self, tiles: list, skill: Skill) -> None:

        for tile in tiles:
            if self.__selected.get_x() >= tile.get_x() >= self.__selected.get_x() - (32 * skill.get_act_range()):
                tile.set_can_atk()


