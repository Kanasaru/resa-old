""" This module provides the GamePanel class

:project: resa
:source: https://github.com/Kanasaru/resa
:license: GNU General Public License v3
"""

from data.settings import conf
import logging
import pygame
from data.handlers.spritesheet import SpriteSheetHandler
from data.interfaces.interface import Interface
from data.forms.label import Label
from data.forms.title import Title
from data.forms.button import Button
from data.helpers.event import Event
import data.eventcodes as ecodes
import data.helpers.color as colors


class GamePanel(Interface):
    def __init__(self, sheet_handler: SpriteSheetHandler, sheet_key):
        super().__init__()

        self.sheet_handler = sheet_handler
        self.sheet_key = sheet_key

        self.name = 'panel'
        self.rect = pygame.Rect((0, 0), (conf.resolution[0], 30))
        self.bg_color = colors.COLOR_BLACK
        self.bg_image = None
        self._resources = f'Wood: 0 | Stone: 0 | Marble: 0 | Tools: 0 | Gold: 0'

        self.title = Title(self.name, self.rect, self.bg_color, self.bg_image)

        # labels
        tf_resources = Label('tf_resources', (self.title.width() // 2, 5), self.resources, 14, self.update_resources)
        tf_resources.set_font(conf.std_font)
        tf_resources.font_color(colors.COLOR_WHITE)
        tf_resources.align(tf_resources.CENTER)
        # buttons
        b_quit = Button(
            'b_quit',
            pygame.Rect(self.title.width() - 5, 3, 70, 24),
            self.sheet_handler,
            self.sheet_key,
            'Quit',
            Event(ecodes.STOPGAME, ecodes.STOPGAME)
        )
        b_quit.align(b_quit.RIGHT)
        b_quit.set_font(conf.std_font, 13)
        b_save = Button(
            'b_save',
            pygame.Rect(self.title.width() - 80, 3, 70, 24),
            self.sheet_handler,
            self.sheet_key,
            'Save',
            Event(ecodes.SAVEGAME, ecodes.SAVEGAME)
        )
        b_save.align(b_save.RIGHT)
        b_save.set_font(conf.std_font, 13)

        self.title.add(tf_resources)
        self.title.add([b_save, b_quit])

    @property
    def resources(self) -> str:
        return self._resources

    @resources.setter
    def resources(self, res: dict) -> None:
        try:
            self._resources = f"Wood: {res['Wood']} | Stone: {res['Stone']} | Marble: {res['Marble']}" \
                              f" | Tools: {res['Tools']} | Gold: {res['Gold']}"
        except KeyError:
            logging.warning('Failed to set resources in GamePanel')
        finally:
            pass

    def update_resources(self):
        return self.resources
