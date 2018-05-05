import yaml

BACKGROUND = (131, 175, 241)

with open("assets/backgrounds/city/scroll/info.yml", "r") as file:
    try:
        BGINFO = yaml.load(file)
    except yaml.YAMLError as exc:
        print(exc)

screen_width = 1920
screen_height = 1080
PIXEL_MULTIPLIER = 10

# Background
GROUND_HEIGHT = 100

game_title = "Soton Analytica"