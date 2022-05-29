# --- Day 1: Sonar Sweep ---

import numpy as np

# Functions


def file_to_list(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [int(entry.strip()) for entry in lines]


def count_increments(measurements):
    prev_entry = measurements[0]
    increases = 0
    for entry in measurements[1:]:
        if entry > prev_entry:
            increases += 1
        prev_entry = entry
    return increases


def list_to_window(measurements):
    return np.convolve(measurements, np.ones(3), 'valid')


# Code
# Part 1
measurements = file_to_list('input01.txt')
increases = count_increments(measurements)
print('Increases: ', increases)


# Part 2
windows = list_to_window(measurements)
increases = count_increments(windows)
print('Increases window: ', increases)
