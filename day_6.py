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
    return len(aux)


# Code
# Part 1
input = file_to_list('input06.txt')
print(input)
fish = simulate(input, 80)
print('Number of fish:', fish)
