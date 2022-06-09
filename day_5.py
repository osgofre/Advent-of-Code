# --- Day 5: Hydrothermal Venture ---

import numpy as np


class Line:
    def __init__(self):
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0

    def line_coordinates(self, coordinates):
        self.x1 = int(coordinates[0])
        self.y1 = int(coordinates[1])
        self.x2 = int(coordinates[2])
        self.y2 = int(coordinates[3])

    def get_orientation(self):
        if self.x1 == self.x2:
            return 'vertical'
        elif self.y1 == self.y2:
            return 'horizontal'
        else:
            if abs(self.x1 - self.x2) == abs(self.y1 - self.y2):
                return 'diagonal'
            else:
                return 'other diagonal'

    def draw_line_1(self):
        orientation = self.get_orientation()
        if orientation == 'vertical':
            y_coordinates = []
            [y_coordinates.append(i) for i in range(self.y1, self.y2 + 1)] if self.y2 > self.y1 else [
                y_coordinates.append(i) for i in range(self.y1, self.y2 - 1, -1)]
            x_coordinates = [self.x1] * len(y_coordinates)
        elif orientation == 'horizontal':
            x_coordinates = []
            [x_coordinates.append(i) for i in range(self.x1, self.x2 + 1)] if self.x2 > self.x1 else [
                x_coordinates.append(i) for i in range(self.x1, self.x2 - 1, -1)]
            y_coordinates = [self.y1] * len(x_coordinates)
        else:
            return 0, 0
        return x_coordinates, y_coordinates

    def get_max(self):
        return max([self.x1, self.y1, self.x2,  self.y2])

    def print(self):
        print('(', self.x1, ',', self.y1, ') , (', self.x2, ',', self.y2, ')')

    def draw_line_2(self):
        orientation = self.get_orientation()
        if orientation == 'vertical':
            y_coordinates = []
            [y_coordinates.append(i) for i in range(self.y1, self.y2 + 1)] if self.y2 > self.y1 else [
                y_coordinates.append(i) for i in range(self.y1, self.y2 - 1, -1)]
            x_coordinates = [self.x1] * len(y_coordinates)
        elif orientation == 'horizontal':
            x_coordinates = []
            [x_coordinates.append(i) for i in range(self.x1, self.x2 + 1)] if self.x2 > self.x1 else [
                x_coordinates.append(i) for i in range(self.x1, self.x2 - 1, -1)]
            y_coordinates = [self.y1] * len(x_coordinates)
        elif orientation == 'diagonal':
            x_coordinates, y_coordinates = [], []
            [y_coordinates.append(i) for i in range(self.y1, self.y2 + 1)] if self.y2 > self.y1 else [
                y_coordinates.append(i) for i in range(self.y1, self.y2 - 1, -1)]
            [x_coordinates.append(i) for i in range(self.x1, self.x2 + 1)] if self.x2 > self.x1 else [
                x_coordinates.append(i) for i in range(self.x1, self.x2 - 1, -1)]
        else:
            return 0, 0
        return x_coordinates, y_coordinates

# Functions


def file_to_array(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [(entry.replace(' -> ', ',').strip().split(',')) for entry in lines]


def get_lines(input):
    lines = dict()
    for i in range(len(input)):
        lines[i] = Line()
        lines[i].line_coordinates(input[i])
    return lines


def get_max(lines):
    maximum = 0
    for i in lines:
        if lines[i].get_max() > maximum:
            maximum = lines[i].get_max()
    return maximum


def get_diagram_1(lines):
    maximum = get_max(lines) + 1
    board = np.zeros([maximum, maximum], dtype=int)
    for line in lines:
        x, y = lines[line].draw_line_1()
        if x != 0 and y != 0:
            board[y, x] += 1
    return board


def get_diagram_2(lines):
    maximum = get_max(lines) + 1
    board = np.zeros([maximum, maximum], dtype=int)
    for line in lines:
        x, y = lines[line].draw_line_2()
        if x != 0 and y != 0:
            board[y, x] += 1
    return board


def print_line(x, y):
    print('x: ', end='')
    [print(element, end='') for element in x]
    print('\ny: ', end='')
    [print(element, end='') for element in y]


def get_overlap(diagram):
    return np.count_nonzero(diagram > 1)


# Code
# Part 1
input = file_to_array('input.txt')
lines = get_lines(input)
diagram = get_diagram_1(lines)
# print(diagram)
overlap = get_overlap(diagram)
print('Overlap count =', overlap)


# Part 2
input = file_to_array('input.txt')
lines = get_lines(input)
diagram = get_diagram_2(lines)
# print(diagram)
overlap = get_overlap(diagram)
print('Overlap count =', overlap)
