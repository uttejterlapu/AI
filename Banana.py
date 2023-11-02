# Define the room and initial positions
room = [[0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 2, 3, 0],
        [0, 0, 0, 0, 0]]

# 0 represents an empty cell, 1 is the monkey, 2 is the banana, and 3 is an obstacle (box).

# Monkey's initial position
monkey_x, monkey_y = 2, 2
bananas_collected = 0

# Define functions to move the monkey
def move_up():
    global monkey_x
    monkey_x -= 1

def move_down():
    global monkey_x
    monkey_x += 1

def move_left():
    global monkey_y
    monkey_y -= 1

def move_right():
    global monkey_y
    monkey_y += 1

# Main loop to collect bananas
while bananas_collected == 0:
    if room[monkey_x][monkey_y] == 2:
        bananas_collected = 1
        print("Monkey collected the banana!")
    elif monkey_x > 0 and (room[monkey_x - 1][monkey_y] != 3):
        move_up()
        print("Monkey moved up")
    elif monkey_y < len(room[0]) - 1 and (room[monkey_x][monkey_y + 1] != 3):
        move_right()
        print("Monkey moved right")
    else:
        print("Monkey is stuck! Cannot collect the banana.")
        break
