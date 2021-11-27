""" This module provides handlers for the game

:project: resa
:source: https://github.com/Kanasaru/resa
:license: GNU General Public License v3
"""

__version__ = '1.1'

from ast import literal_eval
import pygame
import xml.etree.ElementTree as ETree

from data.helpers.time import seconds_to_clock


class DebugHandler(object):
    def __init__(self, mode: int = 0):
        self.QUIET = 0
        self.LOUD = 1
        self._mode = mode
        self._play_time = pygame.time.get_ticks()

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if value == self.QUIET or value == self.LOUD:
            self._mode = value
        else:
            raise ValueError('Given debug mode is not available.')

    @property
    def play_time(self) -> int:
        return self._play_time

    @play_time.setter
    def play_time(self, time: int) -> None:
        self._play_time = time // 1000

    def update(self) -> None:
        self.play_time = pygame.time.get_ticks()

    def toggle(self):
        if self.mode == self.QUIET:
            self.mode = self.LOUD
        else:
            self.mode = self.QUIET

        print(self.mode)

    def __bool__(self):
        if self.mode == self.LOUD:
            return True
        return False


class GameDataHandler(object):
    def __init__(self) -> None:
        self._resources = {
            "Wood": 0,
            "Stone": 0,
            "Marble": 0,
            "Tools": 0,
            "Gold": 0,
        }
        self._world_data = None
        self._game_time = 0
        self._game_timer = pygame.time.Clock()
        self._game_time_speed = 1

    @property
    def game_time_speed(self):
        return self._game_time_speed

    @game_time_speed.setter
    def game_time_speed(self, value: int):
        if value >= 1:
            self._game_time_speed = value
        else:
            raise ValueError("Game time speed must be 1 or higher.")

    @property
    def resources(self) -> dict:
        return self._resources

    @resources.setter
    def resources(self, res: dict) -> None:
        for key, value in res.items():
            if key in self._resources:
                self._resources[key] = int(value)
            else:
                raise KeyError(f"'{key}' with '{value}' not in resources")

    @property
    def game_time(self) -> int:
        return self._game_time

    @game_time.setter
    def game_time(self, time: int) -> None:
        self._game_time = time

    def get_game_time(self):
        day = ((self.game_time // 1000) * self.game_time_speed) // (24 * 3600)
        return f'Day {day}'

    @property
    def world_data(self) -> tuple[pygame.Rect, dict]:
        return self._world_data

    @world_data.setter
    def world_data(self, data: tuple[pygame.Rect, dict]) -> None:
        self._world_data = data

    def update(self) -> None:
        self._game_timer.tick()
        self.game_time += self._game_timer.get_time()

    def read_from_file(self, filepath: str) -> None:
        tree = ETree.parse(filepath)
        root = tree.getroot()

        res = {}
        rect = None
        fields = []
        for child in root:
            # read in-game time
            if child.tag == 'general':
                for gen_data in child.iter('gametime'):
                    self.game_time = literal_eval(gen_data.attrib['milliseconds'])
            # read resources
            if child.tag == 'resources':
                for res_data in child.iter('res'):
                    res[res_data.attrib['name']] = int(res_data.text)
            # read world
            if child.tag == 'world':
                # basic data
                for rect_data in child.iter('rect'):
                    rect = pygame.Rect(literal_eval(rect_data.text))
                for sub_child in child:
                    # read field data
                    if sub_child.tag == 'fields':
                        for field in sub_child.iter('field'):
                            pos = literal_eval(field.attrib['pos'])
                            sprite_data = literal_eval(field.attrib['sprite_data'])
                            solid = literal_eval(field.attrib['solid'])
                            fields.append([pos, sprite_data, solid])

        self.resources = res
        self.world_data = (rect, fields)

    def save_to_file(self, filepath: str):
        root = ETree.Element("data")

        # general
        general = ETree.SubElement(root, "general")
        ETree.SubElement(general, "gametime", milliseconds=str(self.game_time))
        # save resources
        resources = ETree.SubElement(root, "resources")
        for key, value in self.resources.items():
            ETree.SubElement(resources, "res", name=key).text = str(value)

        # save world
        world = ETree.SubElement(root, "world")
        ETree.SubElement(world, "rect").text = str((self.world_data[0].topleft, self.world_data[0].size))
        fields = ETree.SubElement(world, "fields")
        for raw_field in self.world_data[1]:
            ETree.SubElement(fields, "field",
                             pos=str(raw_field[0]),
                             sprite_data=str(raw_field[1]),
                             solid=str(raw_field[2]))

        # write file
        tree = ETree.ElementTree(root)
        ETree.indent(tree, space="\t", level=0)
        tree.write(filepath, encoding="utf-8", xml_declaration=True)
