import yaml

from pygame import USEREVENT

BACKGROUND = (131, 175, 241)

with open("assets/backgrounds/city/scene.yml", "r") as file:
    try:
        BGINFO = yaml.load(file)
    except yaml.YAMLError as exc:
        print(exc)

with open("assets/charstates.yaml", "r") as file:
    try:
        CHARSTATES = yaml.load(file)
    except yaml.YAMLError as exc:
        print(exc)

screen_width = 1920
screen_height = 1080
PIXEL_MULTIPLIER = 10

# Background
GROUND_HEIGHT = 100

# Input
default_address = "http://10.9.174.43/data"
input_valid_time_seconds = 1
input_update_interval = 0.25
GETINPUT = USEREVENT+2

game_title = "Soton Analytica"
