import pygame
from display.constants import *
from display.characters import ZUCC, Human
from display.background import Background
from comms.InputEvent import InputEvent
from threading import Thread
from display.state import State

import argparse

parser = argparse.ArgumentParser(description="Z U C C will consume Y O U.")
parser.add_argument("--keyboard", help="Use the keyboard to control Z U C C", action='store_true')
args = parser.parse_args()

pygame.init()
pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))


state = State(screen, args.keyboard)
state.playIntro()
state.playGame()