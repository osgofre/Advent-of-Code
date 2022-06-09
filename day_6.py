# Functions
def file_to_list(file):
    with open(file, 'r') as f:
        line = f.readlines()
        entry = line[0].strip().split(',')
        return [int(element) for element in entry]


def count_day(input):
    for i in range(len(input)):
        if (input[i] > 0):
            input[i] -= 1
        else:
            input[i] = 6
            input.append(8)
    return input


def simulate(input, days):
    aux = input
    for i in range(days):
        aux = count_day(aux)
        print('Day', i, 'Fish:', len(aux))
    return len(aux)


def simulate_2(input, days):
    for i in range(days):
        expired_fish = input.pop(0)
        input[6] += expired_fish
        input.append(expired_fish)
    return sum(input)


# Code
# Part 1
input = file_to_list('input.txt')
# fish = simulate(input, 256)
# print('Number of fish:', fish)


# Part 2
input = file_to_list('input06.txt')
stages = [input.count(i) for i in range(9)]
fish = simulate_2(stages, 256)
print('Number of fish:', fish)
