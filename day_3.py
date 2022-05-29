# --- Day 3: Binary Diagnostic ---

# Functions
def file_to_array(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        return [(entry.strip()) for entry in lines]


def get_gamma(diagnostic):
    gamma = []
    n = len(diagnostic[0])
    for i in range(0, n):
        count_0, count_1 = 0, 0
        for number in diagnostic:
            if number[i] == '0':
                count_0 += 1
            elif number[i] == '1':
                count_1 += 1
        if count_0 > count_1:
            gamma.append('0')
        else:
            gamma.append('1')
    binary = bin(int(''.join(map(str, gamma)), 2) << 1)
    return int(binary, 2)//2, n


def get_epsilon(gamma, n):
    list = [1]*n
    binary = bin(int(''.join(map(str, list)), 2) << 1)
    xor_operator = int(binary, 2)//2
    return gamma ^ xor_operator


def get_oxygen(diagnostic):
    for i in range(len(diagnostic[0])):
        if len(diagnostic) == 1:
            return int(diagnostic[0], base=2)
        all_entries_at_pos = [entry[i] for entry in diagnostic]
        common_bit = '1' if all_entries_at_pos.count(
            '1') >= len(diagnostic)/2 else '0'
        diagnostic = [entry for entry in diagnostic if entry[i] == common_bit]
    return int(diagnostic[0], base=2)


def get_co2(diagnostic):
    for i in range(len(diagnostic[0])):
        if len(diagnostic) == 1:
            return int(diagnostic[0], base=2)
        all_entries_at_pos = [entry[i] for entry in diagnostic]
        less_common_bit = '1' if all_entries_at_pos.count(
            '1') < len(diagnostic)/2 else '0'
        diagnostic = [
            entry for entry in diagnostic if entry[i] == less_common_bit]
    return int(diagnostic[0], base=2)


# Code
# Part 1
diagnostic = file_to_array('input03.txt')
gamma, n = get_gamma(diagnostic)
epsilon = get_epsilon(gamma, n)
print('Gamma:', gamma)
print('Epsilon:', epsilon)
print('Power consuption:', gamma * epsilon)


# Part 2
diagnostic = file_to_array('input03.txt')
oxygen = get_oxygen(diagnostic)
co2 = get_co2(diagnostic)
print('Oxygen:', oxygen)
print('CO2:', co2)
print('Life support rating:', oxygen * co2)
