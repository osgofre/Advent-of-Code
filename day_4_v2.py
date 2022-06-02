# --- Day 4: Giant Squid ---

import numpy as np


# Class


class Board:
    def __init__(self):
        self.board = np.zeros([5, 5], dtype=int)
        self.marked = np.ones([5, 5])

    def fill_board(self, line):
        for i in range(1, len(line)):
            self.board[i-1] = [int(number) for number in line[i].split(' ')]

    def check_number(self, number):
        if number in self.board:
            i, j = np.where(self.board == number)
            self.marked[i, j] = 0
            return True
        else:
            return False

    def check_win(self):
        if 0 in np.sum(self.marked, axis=0) or 0 in np.sum(self.marked, axis=1):
            return True
        else:
            return False

# Functions


def file_to_array(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [(entry.replace('  ', ' ').strip()) for entry in lines]


def get_boards(input):
    numbers = [int(number) for number in input[0].split(',')]
    boards = dict()
    num_boards = (len(input)-1)//6
    for i in range(num_boards):
        boards[i] = Board()
        boards[i].fill_board(input[1+i*6:7+i*6])
    return numbers, boards


def get_first_winner(numbers, boards):
    for number in numbers:
        for i in range(len(boards)):
            if boards[i].check_number(number):
                if boards[i].check_win():
                    return number, boards[i]


def get_score(number, winner):
    sum_board = np.sum(np.multiply(winner.board, winner.marked))
    return int(number * sum_board)


# Code
# Part 1
input = file_to_array('input.txt')
numbers, boards = get_boards(input)
number, winner = get_first_winner(numbers, boards)
score = get_score(number, winner)
print('Score of the first winner:', score)
