RESOLUTION = 800,600
#FOR CLASS BACKGROUND
BORDER_SKY_GROUND_Y = 2 * int(RESOLUTION[1] / 3)
RECTANGLE_GROUND = 0, BORDER_SKY_GROUND_Y, RESOLUTION[0], RESOLUTION[1]-BORDER_SKY_GROUND_Y
##TREE COORDINATES
#TREE_X = RESOLUTION[0]//5
TREE_X = RESOLUTION[0]//2
TREE_Y = RESOLUTION[1]*4//5

#FOR CLASS TREE
##SIZES
TREE_WIDTH = 140
TREE_HEIGHT = 200

#FOR CLASS NEST
NEST_WIDTH = int(TREE_WIDTH /3)
NEST_HEIGHT = int(NEST_WIDTH /2)
NEST_X = TREE_X - int(30*TREE_WIDTH/100)
NEST_Y = TREE_Y - int(78*TREE_HEIGHT/100)
NEST_XY = NEST_X, NEST_Y

#FOR CLASS BIRD
BIRD_WIDTH = 78
BIRD_HEIGHT = 60
BODY_RADIUS = 20
TUPLE_Y_LEVELS = TREE_Y + int(BIRD_HEIGHT/2), NEST_Y, int(5*NEST_Y/8), int(NEST_Y/4) #3 levels, 0 - ground, 1 - nest, 3 - maximum

#CLASS WORM
WORM_SIZE = 40, 5
WORM_TIME_MIN = 100
WORM_TIME_MAX = 400

#CLASS CAT
CAT_SIZE = 110, 80
CAT_TIME_MIN = 1000
CAT_TIME_MAX = 4000
CAT_BODY_RECT = (30,30,80,22)

#FOR CLASS GAME
WORM_CREATE_MIN = 100
WORM_CREATE_MAX = 400
CAT_CREATE_MIN = 10
CAT_CREATE_MAX = 400

#FOR CLASS BOMB
BOMB_WIDTH = 10
BOMB_HEIGHT = 20

#ENERGY CONSUMPTION
ENERGY_LIVE = 1
ENERGY_FLY_UP = 30
ENERGY_FLY_IN_PLACE = 15
ENERGY_FLY = 5
ENERGY_RUN = 5
ENERGY_MAXIMUM = 10000


#SHIT
SHIT_MAXIMUM = 1000
SHIT_IN_BOMB = 200
#FOOD
FOOD_MAXIMUM = 1000
FOOD_TO_ENERGY = 10
WORM_TO_FOOD = 333

#GRAVITY
ANIMATION_DIVIDER = 12
GRAVITATION = 1.2
TIME_AFTER_END = 200
'''
#SIZES

BIRD_BODY_RADIUS = 20
BIRD_WIDTH = BIRD_BODY_RADIUS*2
BIRD_HEIGHT = BIRD_BODY_RADIUS*2

#COORDINATS
SKY_XYWH = 0, 0, RESOLUTION[0], 2*RESOLUTION[1]//3
GROUND_XYWH = 0, 2*RESOLUTION[1]//3, RESOLUTION[0], RESOLUTION[1]/3

TREE_X_RANGE = 16

BIRD_ON_GROUND_Y = TREE_Y
BIRD_FLIGHT_Y2 = RESOLUTION[1]//7
BIRD_FLIGHT_Y1 = 2*RESOLUTION[1]//7
BIRD_Y = BIRD_ON_GROUND_Y, NEST_Y, BIRD_FLIGHT_Y1, BIRD_FLIGHT_Y2
BELLY_CAPACITY = 1000
ENERGY_CAPACITY = 1000
'''
