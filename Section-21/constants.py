#Screen
APP_TITLE = "Snake Game"
SCREEN_HEIGHT = 1000
SCREEN_WIDTH = 1000
SCREEN_BGCOLOR = "black"
SCREEN_GAP=40
SCREEN_LIMIT_HEIGHT = int(SCREEN_HEIGHT/2 - SCREEN_GAP)
SCREEN_LIMIT_WIDTH = int(SCREEN_WIDTH/2 - SCREEN_GAP)

#Snake
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
SNAKE_COLOR = "white"
SNAKE_SHAPE = "square"
SNAKE_SPEED= 0.2

#Food
SPEED_MAP = {
    "fastest": 0,
    "fast": 1,
    "normal": 3,
    "slow": 6,
    "slowest": 10
}

FOOD_SHAPE = "circle"
FOOD_COLOR = "blue"
FOOD_SPEED = SPEED_MAP["fastest"]
FOOD_LEN=0.5
FOOD_WID=0.5

#Socreboard
SCORE_POSITION = (0, (SCREEN_WIDTH/2))
SCORE_ALIGNMENT = "center"
SCORE_FONT = ("Courier", 24, "normal")