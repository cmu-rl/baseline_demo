"""
config.py -- The main configuration store for the behavioral cloning demo.

Version 2.0

Featrues added since v1:
Added hot-bar state to recording
Added new network output to select hotbar item
Added sneak and drop commands
Added crafting commands for planks, sticks, pickaxe

"""
# 
GYM_RESOLUTION = (96*2, 128*2)
#TODO this can have more than one port
MALMO_IP = ('127.0.0.1', 10000)


################################ 
# Version Number for Recording #
################################

# DO NOT CHANGE THE ORDER OF BINDINGS
# IT WILL INVALIDATE OLD DATA!
BINDINGS = [
    #Length 10 one-hot
        ({
        "1": 'hotbar.1 1',
        "2": 'hotbar.2 1',
        "3": 'hotbar.3 1',
        "4": 'hotbar.4 1',
        "5": 'hotbar.5 1',
        "6": 'hotbar.6 1',
        "7": 'hotbar.7 1',
        "8": 'hotbar.8 1',
        "9": 'hotbar.9 1'
    }, '#HOTBAR#'),
    # Length 3 one-hot
    ({'w': 'move 1',
    "s": 'move -1'}, "move 0"),
    ({"a": 'strafe -1',
    "d": 'strafe 1'}, "strafe 0"),
    ({ "k": 'pitch 1',
    "i": 'pitch -1'}, "pitch 0"),
    ({"l": 'turn 1',
    "j": 'turn -1'}, "turn 0"),
    #Length 2 one-hot
    ({'space': 'jump 1'}, "jump 0"),
    ({"n": 'attack 1'}, "attack 0"),
    ({"m": 'use 1'}, "use 0"),
    ({"q": 'discardCurrentItem'}, 'noop'),
    ({'left shift': 'crouch 1'}, 'crouch 0')
    ]

PRESS_EVERY_TIME = ['/', '*', 'z', 'x', 'c', 'end', 'down', 'page down', 'insert', 'delete', 'home', 'up', 'page up', 'left', 'clear', 'right']
SINGLE_USE_ACTIONS = []
for KMAP in BINDINGS:
    for key in PRESS_EVERY_TIME:
        if key in KMAP[0]:
            SINGLE_USE_ACTIONS.append(KMAP[0][key])


    
SHARD_SIZE = 5000
RECORD_INTERVAL = 1.0/10.0
SAVE_INTERVAL = 1000
EPISODE_LENGTH = 5000
RETRAIN = True
DATA_DIR = "./"


# HYPERPARAMETERS
SMALLEST_FEATURE_MAP = 9
FC_SIZES =[768, 400]
FC_FINAL_SIZES = [256, 128]
LEARNING_RATE = 0.00025
DROPOUT=0.5
BATCH_SIZE = 64
PIXEL_RESOLUTION = 255.0
LSTM_HIDDEN = 1024
MAX_SEQ_LEN = 50
REGULARIZATION_SCALE = 0.00001
DAGGER_BUFFER_SIZE = 5000

VERSION = "v1"