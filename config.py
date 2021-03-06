# Game constants
DISPLAY_WIDTH = 460
DISPLAY_HEIGHT = 410
GAME_SPEED = 1  # Ground breaks at any speed > 1

# Bird constants
START_HEIGHT = 120
OFFSET = 50
MAX_FALL = 3
MAX_RISE = -3

# Pipe constants
PIPE_HEIGHT = -280           # Height of top of upper pipe image
PIPE_HEIGHT_VARIANCE = 15    # Between 0 and 15
PIPE_DISTANCE = 150          # Distance between one set of pipes and the next
PIPE_GAP = 360 + 50          # no gap = 360
if DISPLAY_WIDTH % PIPE_DISTANCE == 0:
    numPipes = DISPLAY_WIDTH // PIPE_DISTANCE + 1
else:
    numPipes = DISPLAY_WIDTH // PIPE_DISTANCE + 2

# Ground constants
GROUND_WIDTH = 336
if DISPLAY_WIDTH % GROUND_WIDTH == 0:
    numGround = DISPLAY_WIDTH // GROUND_WIDTH + 1
else:
    numGround = DISPLAY_WIDTH // GROUND_WIDTH + 2

# Background constants
BACKGROUND_WIDTH = 276
numBackgrounds = DISPLAY_WIDTH // BACKGROUND_WIDTH + 1
