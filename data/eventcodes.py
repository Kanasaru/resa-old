""" This module provides game event codes

:project: resa
:source: https://github.com/Kanasaru/resa
:license: CC-BY-SA-4.0
"""

import pygame

""" pygame.USEREVENTs """
RESA_TITLE_EVENT = pygame.USEREVENT + 1
RESA_MUSIC_ENDED_EVENT = pygame.USEREVENT + 2
RESA_AUTOSAVE_EVENT = pygame.USEREVENT + 3
RESA_GAME_EVENT = pygame.USEREVENT + 4
# pygame.USEREVENT + 5
# pygame.USEREVENT + 6
# pygame.USEREVENT + 7
# pygame.USEREVENT + 8
# pygame.USEREVENT

""" Resa TITLE EVENTs """
# BUTTON & SWITCH EVENTS  | 1xxx
RESA_BTN_STARTGAME = 1000
RESA_BTN_QUITGAME = 1001
RESA_BTN_LOADGAME = 1002
RESA_BTN_LEAVEGAME = 1003
RESA_BTN_SAVEGAME = 1004
RESA_BTN_OPTIONS = 1005
RESA_BTN_MAINMENU = 1006
RESA_BTN_CHG_RESOLUTION = 1007
RESA_BTN_EDITOR = 1008
RESA_SWT_FULLSCREEN = 1009
# MESSAGEBOX EVENTs | 2xxx
RESA_MSG_OK = 2000
RESA_MSG_NO = 2001
RESA_QUITGAME_TRUE = 2002
RESA_QUITGAME_FALSE = 2003

""" Resa GAME EVENTs """
# CONTROL EVENTs | 5xxx
RESA_CTRL_MAP_MOVE = 5000

RESA_EDITOR_SELECT = 70000
RESA_EDITOR_PLACE = 70001
RESA_EDITOR_LEAVE = 70002
RESA_EDITOR_LOAD = 70003
RESA_EDITOR_SAVE = 70004
