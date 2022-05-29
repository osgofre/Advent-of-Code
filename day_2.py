# --- Day 2: Dive! ---

# Functions

def file_to_array(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [(entry.strip()) for entry in lines]


def get_final_position1(movements):
    horizontal, depth = 0, 0
    for row in movements:
        direction, amount = row.split(' ')[0], int(row.split(' ')[1])
        if direction == 'forward':
            horizontal += amount
        elif direction == 'up':
            depth -= amount
        elif direction == 'down':
            depth += amount
    return horizontal*depth


def get_final_position2(movements):
    horizontal, depth, aim = 0, 0, 0
    for row in movements:
        direction, amount = row.split(' ')[0], int(row.split(' ')[1])
        if direction == 'forward':
            horizontal += amount
            depth += aim * amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount
    return horizontal*depth


# Code
# Part 1
movements = file_to_array('input02.txt')
final_position = get_final_position1(movements)
print('Your final position is: ', final_position)

# Part 2
final_position = get_final_position2(movements)
print('Your final position is: ', final_position)
