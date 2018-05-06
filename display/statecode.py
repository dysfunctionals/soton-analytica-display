from enum import Enum


class StateCode(Enum):
    LOGO = 0
    MENU = 1
    INTRO = 2
    PLAYING = 3
    END = 4
    ZUCC_WIN = 5
    HUMAN_WIN = 6