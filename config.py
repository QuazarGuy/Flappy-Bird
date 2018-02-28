DISPLAY_WIDTH = 430
DISPLAY_HEIGHT = 410
GAME_SPEED = 1  # Ground breaks at any speed > 1

# Pipe constants
PIPE_DISTANCE = 150
PIPE_GAP = 360 + 60  # no gap = 360
if DISPLAY_WIDTH % PIPE_DISTANCE == 0:
    numPipes = DISPLAY_WIDTH // PIPE_DISTANCE + 1
else:
    numPipes = DISPLAY_WIDTH // PIPE_DISTANCE + 2

# Ground constants
GROUND_WIDTH = 336
#numGround = 2
if DISPLAY_WIDTH % GROUND_WIDTH == 0:
    numGround = DISPLAY_WIDTH // GROUND_WIDTH + 1
else:
    numGround = DISPLAY_WIDTH // GROUND_WIDTH + 2
