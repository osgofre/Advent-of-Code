# --- Day 7: The Treachery of Whales ---


import statistics as stat


# Functions
def file_to_list(file):
    with open(file, 'r') as f:
        line = f.readlines()
        entry = line[0].strip().split(',')
        return [int(element) for element in entry]


def fuel_cost_1(input):
    cost = [sum([abs(element) for element in input])]
    for i in range(1, len(input)):
        coste = sum([abs(element-i) for element in input])
        if coste > cost[i-1]:
            return cost[i-1]
        else:
            cost.append(coste)


def fuel_cost_2(input):
    cost = [sum([sum(range(abs(element)+1)) for element in input])]
    for i in range(1, len(input)):
        coste = sum([sum(range(abs(element-i)+1)) for element in input])
        if coste > cost[i-1]:
            return cost[i-1]
        else:
            cost.append(coste)

# Code
# Part 1
# input = file_to_list('input07.txt')
# cost = fuel_cost_1(input)
# print('Fuel cost:', cost)


# Part 2
input = file_to_list('input07.txt')
cost = fuel_cost_2(input)
print('Fuel cost:', cost)
