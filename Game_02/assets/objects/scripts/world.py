import os.path
from PIL import Image
from assets.objects.scripts.tile import Tile
from assets.objects.scripts.player import Player

class World:
    def __init__(self, path: str) -> None:
        self.path_general = path

    def new_world(self, level: str, player: Player) -> list:
        global world_list, heigth, width, sprite
        try:
            new_level = os.path.join(self.path_general, level)
            sprite = Image.open(new_level).convert('RGB')
            width = sprite.width
            heigth = sprite.height
            world_list = []
        except Exception as exception:
            print(exception)
            exit()
        try:
            for y in range(heigth):
                for x in range(width):
                    pixel = self.__get_rgb(sprite, x, y)
                    if pixel == {0}: #BLACK
                        tile = Tile('GROUND', self.path_general, x * 64, y * 64)
                        world_list.append(tile)
                    elif pixel == {255}: #WITHE
                        tile = Tile('WALL', self.path_general, x * 64, y * 64)
                        world_list.append(tile)
                    elif pixel == {0, 110, 255}: #BLUE
                        tile = Tile('GROUND', self.path_general, x * 64, y * 64)
                        world_list.append(tile)
                        player.reseter_map(x * 64, y * 64)
                    elif pixel == {0, 8, 255}: #RED
                        tile = Tile('GROUND', self.path_general, x * 64, y * 64)
                        world_list.append(tile)
                    elif pixel == {0, 251, 255}: #Yellow
                        tile = Tile('GROUND', self.path_general, x * 64, y * 64)
                        world_list.append(tile)
        except Exception as exception:
            print(exception)
            exit()
        return world_list

    def __get_rgb(self, image: any, x: int, y: int) -> list:
        r, g, b = image.getpixel((x, y))
        color = {r, g, b}
        return color


