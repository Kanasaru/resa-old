import random
import pygame
from src.handler import RESA_CH, RESA_EH, RESA_SSH, RESA_GDH

BROADLEAF = 1
PALM = 2
EVERGREEN = 3


class Tree(pygame.sprite.Sprite):
    def __init__(self, position: tuple[int, int], tree_type: int) -> None:
        """ Initializes a field

        :param position: position on world surface
        :param tree_type: tree type
        """
        pygame.sprite.Sprite.__init__(self)

        # basic settings
        tree_grow = random.randrange(0, 100, 1)
        if tree_grow <= RESA_CH.tree_grow[2]:
            self.growth = 0
        elif tree_grow <= RESA_CH.tree_grow[2]:
            self.growth = 1
        else:
            self.growth = 2

        self.planted = 0
        self.grow_speed = 40
        self.grow_factor = 1.0
        self.sprite_id = {}
        if tree_type == BROADLEAF:
            self.sprite_id = {
                0: 0,
                1: 1,
                2: 2
            }
        elif tree_type == PALM:
            self.sprite_id = {
                0: 17,
                1: 18,
                2: 19
            }
        else:
            self.sprite_id = {
                0: 9,
                1: 10,
                2: 11
            }
        self.sprite_sheet_id = 'Trees'
        self.position = position
        self.images = {0: None, 1: None, 2: None}

        # image and sprite settings
        self.image = RESA_SSH.image_by_index(self.sprite_sheet_id, self.sprite_id[0])
        self.size = RESA_SSH.aspect_ratio(self.image.get_rect().size, RESA_CH.grid_zoom * 2)
        self.images[0] = pygame.transform.scale(self.image, self.size).convert_alpha()
        self.image = RESA_SSH.image_by_index(self.sprite_sheet_id, self.sprite_id[1])
        self.size = RESA_SSH.aspect_ratio(self.image.get_rect().size, RESA_CH.grid_zoom * 2)
        self.images[1] = pygame.transform.scale(self.image, self.size).convert_alpha()
        self.image = RESA_SSH.image_by_index(self.sprite_sheet_id, self.sprite_id[2])
        self.size = RESA_SSH.aspect_ratio(self.image.get_rect().size, RESA_CH.grid_zoom * 2)
        self.images[2] = pygame.transform.scale(self.image, self.size).convert_alpha()

        self.image = self.images[self.growth]

        # positions
        self.rect = self.image.get_rect()
        self.rect.bottomleft = self.position

    def update(self, event: pygame.event.Event = None) -> None:
        """ Updates tree by its position

        :param event: optional event
        :return: None
        """
        if event is not None:
            if event.type == RESA_EH.GAME_EVENT:
                if event.code == RESA_EH.CTRL_MAP_MOVE:
                    pos_x = self.position[0] + event.move[0]
                    pox_y = self.position[1] + event.move[1]
                    self.position = (pos_x, pox_y)
            if event.type == RESA_EH.GAME_CLOCK:
                if self.growth < 2:
                    if self.planted >= self.grow_speed * self.grow_factor:
                        self.planted = 0
                        self.growth += 1
                        self.image = self.images[self.growth]
                    else:
                        self.planted += 1

        self.rect.bottomleft = self.position

    def delete(self) -> None:
        """ Deletes the tree

        :return: None
        """
        self.kill()

    def __str__(self):
        return f'Tree - ' \
               f'Pos: {self.position} | ' \
               f'Solid: {self.growth} | '

    def __repr__(self):
        return f'Tree - ' \
               f'Pos: {self.position} | ' \
               f'Solid: {self.growth} | '
