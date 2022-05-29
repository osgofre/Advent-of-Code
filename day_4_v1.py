# --- Day 4: Giant Squid ---

import numpy as np

# Functions


def file_to_array(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [(entry.replace('  ', ' ').strip()) for entry in lines]


def get_boards(input):
    numbers = [int(number) for number in input[0].split(',')]
    boards = np.zeros([5, 5, 1], dtype=int)
    board = []
    for line in input[2:-1]:
        if line != '':
            board.append([int(number) for number in line.split(' ')])
        else:
            boards = np.concatenate((boards, np.expand_dims(
                np.array(board), axis=2)), axis=2)
            board = []
    board.append([int(number) for number in input[-1].split(' ')])
    boards = np.concatenate((boards, np.expand_dims(
        np.array(board), axis=2)), axis=2)
    return numbers, boards


def play(numbers, boards):
    for number in numbers:
        for board in boards.T[1:, :, :]:
            if number in board:
                i, j = np.where(board == number)
                board[i, j] = 0
                if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
                    return np.sum(board) * number


def last_winner(numbers, boards):
    winners = [False]*(boards.shape[2]-1)
    for number in numbers:
        w = 0
        for board in boards.T[1:, :, :]:
            if winners[w] == True:
                pass
            else:
                if number in board:
                    i, j = np.where(board == number)
                    board[i, j] = 0
                    if 0 in np.sum(board, axis=0) or 0 in np.sum(board, axis=1):
                        winners[w] = True
                        if sum(winners) == (boards.shape[2]-1):
                            return np.sum(board) * number
            w += 1


# Code
# Part 1
input = file_to_array('input04.txt')
numbers, boards = get_boards(input)
# score = play(numbers, boards)
# print('Score:', score)

# Part 2
score = last_winner(numbers, boards)
print('Score:', score)
