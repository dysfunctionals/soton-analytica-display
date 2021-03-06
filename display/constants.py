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
default_address = "https://ecs.pizza/api/data"
input_valid_time_seconds = 1
input_update_interval = 0.25
GETINPUT = USEREVENT+2
SENDPROJECTILE = USEREVENT+4
MUSIC_DEATH = USEREVENT+3

move_speed = 10

game_title = "Soton Analytica"

user_url = "https://ecs.pizza"

dataTypes = ['Address', "Name", "Message History", "Contacts", "Date of Birth", "Bank Account Number", "Genome"]
icons = ['like', 'wa', 'ig']
