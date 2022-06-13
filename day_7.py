# --- Day 7: The Treachery of Whales ---


from re import M
import numpy as np


# Functions
def file_to_list(file):
    with open(file, 'r') as f:
        line = f.readlines()
        entry = line[0].strip().split(',')
        return [int(element) for element in entry]


def fuel_cost_1(input):
    min_cost = np.infty
    for i in range(min(input), max(input)+1):
        cost = sum([abs(element-i) for element in input])
        if cost > min_cost:
            return min_cost
        else:
            min_cost = cost


def fuel_cost_2(input):
    min_cost = np.infty
    for i in range(min(input), max(input)+1):
        cost = sum([sum(range(abs(element-i)+1)) for element in input])
        if cost > min_cost:
            return min_cost
        else:
            min_cost = cost


# Code
# Part 1
input = file_to_list('input07.txt')
cost = fuel_cost_1(input)
print('Fuel cost:', cost)


# Part 2
input = file_to_list('input07.txt')
cost = fuel_cost_2(input)
print('Fuel cost:', cost)
