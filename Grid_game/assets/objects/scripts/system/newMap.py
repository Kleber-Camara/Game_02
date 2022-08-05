from assets.objects.scripts.tiles.ground import Ground
from assets.objects.scripts.tiles.poison import Poison
from assets.objects.scripts.tiles.water import Water
from assets.objects.scripts.tiles.rock import Rock
from typing import Any
from PIL import Image
import os.path


class Map:

    def __init__(self, path: str) -> None:
        self.path = path

    def new_map(self, level: str) -> list:
        self.__get_map(level)
        width = self.sprite.width
        height = self.sprite.height
        tiles = []
        try:
            for y in range(height):
                for x in range(width):
                    pixel = self.__get_pixel(x, y, self.sprite)
                    if pixel == {0, 0, 0}:
                        print('preto')
                        tile = Ground(x * 32, y * 32, 32, 32, self.path)
                        tiles.append(tile)
                    elif pixel == {94, 27, 161}:
                        tile = Poison(x * 32, y * 32, 32, 32, self.path)
                        tiles.append(tile)
                        print('roxo')
                    elif pixel == {27, 161, 105}:
                        tile = Water(x * 32, y * 32, 32, 32, self.path)
                        tiles.append(tile)
                        print('verde')
                    elif pixel == {161, 27, 27}:
                        tile = Rock(x * 32, y * 32, 32, 32, self.path)
                        tiles.append(tile)
                        print('vermelho')
                    else:
                        print('qualquer')
        except Exception as exception:
            print(exception)
            exit()
        return tiles

    def __get_map(self, level: str) -> None:
        new_level = os.path.join(self.path, 'map')
        new_level = os.path.join(new_level, level)
        try:
            self.sprite = Image.open(new_level).convert('RGB')
        except Exception as exception:
            print(exception)
            exit()

    @staticmethod
    def __get_pixel(x: int, y: int, image: any) -> set[Any]:
        r, g, b = image.getpixel((x, y))
        color = {r, g, b}
        return color
