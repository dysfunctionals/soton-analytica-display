import pygame
from display.constants import *
from display.state import StateMachine, StateCode

import argparse

parser = argparse.ArgumentParser(description="Z U C C will consume Y O U.")
parser.add_argument("--keyboard", help="Use the keyboard to control Z U C C", action='store_true')
parser.add_argument("--nointro", help="L O R D  Z U C C requires you to view the intro", action='store_true')
args = parser.parse_args()

pygame.init()
pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width, screen_height))


state = StateMachine()


while state.state != StateCode.END:
    if not args.nointro:
        if state.state == StateCode.LOGO:
            state.state = StateMachine.playLogo(screen)
        elif state.state == StateCode.MENU:
            state.state = StateMachine.playMenu(screen)
        elif state.state == StateCode.INTRO:
            state.state = StateMachine.playIntro(screen)
        elif state.state == StateCode.PLAYING:
            state.state = StateMachine.playGame(screen, args.keyboard)
        elif state.state == StateCode.ZUCC_WIN:
            state.state = StateMachine.zucc_win(screen)
        elif state.state == StateCode.HUMAN_WIN:
            state.state = StateMachine.human_win(screen)
        else:
            raise EnvironmentError
    else:
        state.state = StateMachine.playGame(screen, args.keyboard)


pygame.quit()
