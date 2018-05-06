from pygame import event
from display import constants
from comms.CrowdInput import CrowdInput
from time import sleep

class InputEvent:
    def __init__(self, game_playing):
        self.input_source = CrowdInput(constants.default_address)
        self.game_playing = game_playing

    def run(self):
        while self.game_playing:
            movement = self.input_source.democracy(constants.input_valid_time_seconds)
            move_event = event.Event(constants.GETINPUT, zucc=movement['zucc'], human=movement['user'])
            event.post(move_event)
            sleep(constants.input_update_interval)
