""" This module provides Field class

:project: resa
:source: https://github.com/Kanasaru/resa
:license: GNU General Public License v3
"""

import pygame


class Field(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], image: pygame.image) -> None:
        """ Initializes a field

        :param position: position on world surface
        :param size: field size
        :param image: field image
        """
        pygame.sprite.Sprite.__init__(self)

        self._position = position
        self._size = size
        self._visible = True
        self._temperature = 20
        self._solid = False
        self.image = pygame.transform.scale(image, self.size)
        self.rect = self.image.get_rect()
        self.rect.topleft = self._position
        self.sprite_sheet_id = None
        self.sprite_id = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def solid(self):
        return self._solid

    @solid.setter
    def solid(self, value):
        self._solid = value

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def update(self) -> None:
        """ Updates field by its position

        :return: None
        """
        self.rect.topleft = self.position

    def move(self, movement: tuple[int, int]) -> None:
        """ Changes the fields position by calculating a new position by given movement

        :param movement: integer of pixel shift for x and y axis
        :return: None
        """
        pos_x = self._position[0] + movement[0]
        pox_y = self._position[1] + movement[1]
        self.position = (pos_x, pox_y)

    def delete(self) -> None:
        """ Deletes the field

        :return: None
        """
        self.kill()

    def __str__(self):
        return f'Field - ' \
               f'Pos: {self.position} | ' \
               f'Solid: {self.solid} | ' \
               f'Temp: {self.temperature} | ' \
               f'Visible: {self.visible}'

    def __repr__(self):
        return f'Field - ' \
               f'Pos: {self.position} | ' \
               f'Solid: {self.solid} | ' \
               f'Temp: {self.temperature} | ' \
               f'Visible: {self.visible}'