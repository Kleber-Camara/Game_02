from assets.objects.scripts.ui.selectarrow import SelectArrow
from assets.objects.scripts.ui.selectmove import SelectMove
from assets.objects.scripts.ui.button import Button
from assets.objects.scripts.system.player import Player
from assets.objects.scripts.enemys.enemy import Enemy
from assets.objects.scripts.ui.healthBar import HealthBar
from assets.objects.scripts.ui.label import Label
from assets.objects.scripts.characters.heroes import Heroes
import pygame.sprite
import pygame


class UiBattle(pygame.sprite.Sprite):

    def __init__(self, player: Player) -> None:
        super().__init__()
        self.player = player
        self.btns = []
        self.__skills_btns = []
        self.__box_action = pygame.Rect(0, 400, (pygame.display.get_surface().get_size()[0]),
                                        (pygame.display.get_surface().get_size()[1] - 400))
        self.__selected_btn = None
        self._arrow = SelectArrow(self.player.path, 0, 0)
        self.__move_target = SelectMove(self.player.path, 0, 0)
        self.__can_see_target = False
        self.__selected_tile = None
        self.__options_button = Button(760, 0, 40, 40, 'op', (255, 255, 255), (255, 0, 0), 16)
        # Enemys info
        self.__max_enemy_hp = None
        self._present_enemy_hp = None
        self.__label_enemy = None
        self.__label_enemy_hp = None

        # Player info
        self.__hero_max_hp = None
        self.__hero_present_hp = None
        self.__hero_label_name = None
        self.__hero_label_hp = None
        self.__hero_max_mana = None
        self.__hero_present_mana = None
        self.__hero_label_mana = None

        # General info
        self.__label_damage_info = None
        self.__damage_durability = 0


    def draw(self) -> None:     # Desenha na tela a interface

        if self.__label_damage_info is not None:
            self.__label_damage_info.update()
            self.__label_damage_info.render()
            self.__damage_durability += 0.3

        if self.__selected_btn is not None:
            self._arrow.move(self.__selected_btn.get_x() - 5, self.__selected_btn.get_y() + 5)
        pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), self.__box_action)
        pygame.draw.rect(pygame.display.get_surface(), (0, 0, 0), self.__box_action, 2)
        pygame.draw.rect(pygame.display.get_surface(), (255, 125, 0), (self.__box_action.x + 5,
                                                                       self.__box_action.y + 3, 200,
                                                                       self.__box_action.height - 10), 2)
        if self.player.get_selected():
            if not self.btns:
                btn1 = Button(35, 410, 120, 30, 'Mover', (255, 255, 255), (0, 0, 255), 24)
                btn2 = Button(35, 450, 120, 30, 'Atacar', (255, 255, 255), (0, 0, 255), 24)
                btn3 = Button(35, 490, 120, 30, 'Itens', (255, 255, 255), (0, 0, 255), 24)
                btn4 = Button(35, 530, 120, 30, 'Fugir', (255, 255, 255), (0, 0, 255), 24)
                self.btns.append(btn1)
                self.btns.append(btn2)
                self.btns.append(btn3)
                self.btns.append(btn4)
        else:
            self.__skills_btns.clear()
            self.btns.clear()

        if self.__skills_btns is not None:
            for btn in self.__skills_btns:
                btn.render()

        for btn in self.btns:
            btn.render()

        if self.__selected_btn is not None:
            self._arrow.render()

        if self.__can_see_target:
            self.__move_target.render()
        # RENDER ENEMY STUFF
        if self.__max_enemy_hp is not None:
            self.__max_enemy_hp.render()
        if self._present_enemy_hp is not None:
            self._present_enemy_hp.render()
        if self.__label_enemy is not None:
            self.__label_enemy.render()
        if self.__label_enemy_hp is not None:
            self.__label_enemy_hp.render()

        # RENDER PLAYER STUFF
        if self.__hero_label_name is not None and self.__hero_max_hp is not None and self.__hero_present_hp is not None:
            self.__hero_label_name.render()
            self.__hero_max_hp.render()
            self.__hero_present_hp.render()
        if self.__hero_label_hp is not None and self.__hero_max_mana is not None and self.__hero_present_mana is not None:
            self.__hero_label_hp.render()
            self.__hero_max_mana.render()
            self.__hero_present_mana.render()
        if self.__hero_label_mana is not None:
            self.__hero_label_mana.render()

        if self.__damage_durability >= 10:
            self.__damage_durability = 0
            self.__label_damage_info = None

        self.__options_button.render()

    def skills_btns_create(self, skills: list) -> None:  # Cria botões baseados na lista de skills do heroi selecionado
        i = 1
        for btn in skills:
            if len(btn.get_name()) > 6:
                b = Button(240, i * 410, 120, 30, btn.get_name(), (255, 255, 255), (0, 0, 255), 16)
            else:
                b = Button(240, i * 410, 120, 30, btn.get_name(), (255, 255, 255), (0, 0, 255), 24)
            self.__skills_btns.append(b)

    def navigate_ui(self, direction: bool) -> None:     # Navega entre os botões de ações

        if self.__selected_btn is not None:
            for i in range(len(self.btns)):
                if self.__selected_btn == self.btns[i]:
                    if direction:
                        if i + 1 >= len(self.btns):
                            self.__selected_btn = self.btns[0]
                            break
                        else:
                            self.__selected_btn = self.btns[i + 1]
                            break
                    else:
                        if i - 1 < 0:
                            self.__selected_btn = self.btns[len(self.btns) - 1]
                            break
                        else:
                            self.__selected_btn = self.btns[i - 1]
                            break
        else:
            self.__selected_btn = self.btns[0]

    def select_keyboard_options(self) -> str:   # Retorna o nome do botao selecionado
        if self.__selected_btn is not None:
            return self.__selected_btn.name

    def end_arrow(self) -> None:    # Faz a seta de seleção não aparecer mais
        self.__selected_btn = None
        self.__can_see_target = False

    def get_selected_button(self) -> Button:    # retorna o botao selecionado
        return self.__selected_btn

    @staticmethod
    def get_min_max_moveY(tile_list: list) -> tuple:    # Verifica e retorna o tamanho minimo e maximo da lista de tiles
        min_y = 99999                                   # no eixo y
        max_y = 0
        for i in range(len(tile_list)):
            if tile_list[i].get_can_move():
                if tile_list[i].get_y() < min_y:
                    min_y = tile_list[i].get_y()
                elif tile_list[i].get_y() > max_y:
                    max_y = tile_list[i].get_y()
        return min_y, max_y

    @staticmethod
    def get_min_max_moveX(tile_list: list) -> tuple:    # Verifica e retorna o tamanho maximo e minimo da lista de tiles
        min_x = 9999                                    # no eixo x
        max_x = 0
        for i in range(len(tile_list)):
            if tile_list[i].get_can_move():
                if tile_list[i].get_x() < min_x:
                    min_x = tile_list[i].get_x()
                elif tile_list[i].get_x() > max_x:
                    max_x = tile_list[i].get_x()
        return min_x, max_x

    def move_target(self, x: int, y: int) -> None:  # Movimenta o heroi selecionado para uma determinada area
        self.__move_target.move(x, y)

    def get_move_target_x(self) -> int:     # Retorna o alvo no eixo x, de para onde o jogador quer move-lo
        return self.__move_target.get_x()

    def get_move_target_y(self) -> int:     # Retorna o alvo no eixo y, de para onde o jogador quer move-lo
        return self.__move_target.get_y()

    def change_can_see(self, target: bool) -> None:     # Altera a disponibilidade de visibilidade
        self.__can_see_target = target

    def get_can_see(self) -> bool:  # Retorna se esta disponivel para que o jogador veja
        return self.__can_see_target

    def get_skills_b(self) -> list:
        return self.__skills_btns

    def set_skills_Bfree(self) -> None:
        if self.__skills_btns is not None:
            self.__skills_btns.clear()

    def end_ui(self) -> None:
        self.btns.clear()
        if self.__selected_btn is not None:
            self.__selected_btn = None
        self.set_skills_Bfree()

    def draw_enemy_life(self, rect1: pygame.rect, enemy: Enemy) -> None:
        if rect1.colliderect(enemy.rect):
            self.__max_enemy_hp = HealthBar(600, 420, 16, 100, 'MAX')
            self._present_enemy_hp = HealthBar(600, 420, 16, (enemy.get_present_health() / enemy.get_max_health()) * 100,'other')
            self.__label_enemy = Label(enemy.get_name(), 600, 400, 40, 40, (0, 0, 0), 14)
            self.__label_enemy_hp = Label('HP: {}/{}'.format(enemy.get_present_health(), enemy.get_max_health()), 600,
                                          430, 40, 40, (0, 0, 0), 14)
        else:
            self.erase_enemy_bar()

    def draw_player_info(self, hero: Heroes) -> None:
        if hero is not None:
            self.__hero_label_name = Label(hero.get_name(), 450, 400, 40, 40, (0, 0, 0), 14)
            self.__hero_max_hp = HealthBar(450, 420, 16, 100, 'MAX')
            self.__hero_present_hp = HealthBar(450, 420, 16, (hero.get_present_health() / hero.get_max_health()) * 100, 'other')
            self.__hero_label_hp = Label('HP: {}/{}'.format(hero.get_present_health(), hero.get_max_health()), 450, 430, 40,
                                         40, (0, 0, 0), 14)
            self.__hero_max_mana = HealthBar(450, 450, 16, 100, 'MAX')
            self.__hero_present_mana = HealthBar(450, 450, 16, (hero.get_present_mana() / hero.get_max_mana()) * 100, 'MANA')
            self.__hero_label_mana = Label('MP: {}/{}'.format(hero.get_present_mana(), hero.get_max_mana()), 450, 460, 40,
                                           40, (0, 0, 0), 14)

    def draw_damage(self, damage: int, x: int, y: int) -> None:
        if damage <= 0:
            self.__label_damage_info = Label('MISS', x, y, 40, 40, (255, 255, 255), 12)
        else:
            self.__label_damage_info = Label('{}'.format(damage), x, y, 40, 40, (255, 255, 255), 12)

    def erase_enemy_bar(self) -> None:
        self.__max_enemy_hp = None
        self._present_enemy_hp = None
        self.__label_enemy = None
        self.__label_enemy_hp = None

    def erase_player_info(self) -> None:
        self.__hero_max_hp = None
        self.__hero_present_hp = None
        self.__hero_label_name = None
        self.__hero_label_hp = None
        self.__hero_max_mana = None
        self.__hero_present_mana = None
        self.__hero_label_mana = None
