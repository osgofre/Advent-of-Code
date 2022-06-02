# --- Day 5: Hydrothermal Venture ---


class Line:
    def __init__(self):
        self.x1, self.x2, self.y1, self.y2 = 0, 0, 0, 0

    def line_coordinates(self, coordinates):
        self.x1 = coordinates[0]
        self.y1 = coordinates[1]
        self.x2 = coordinates[2]
        self.y2 = coordinates[3]

    def draw_line(self):
        if self.x1 == self.x2:
            y_coordinates = []
            for i in range(self.y1, self.y2 + 1):
                y_coordinates.append(i)
            x_coordinates = [self.x1] * len(y_coordinates)
        elif self.y1 == self.y2:
            x_coordinates = []
            for i in range(self.x1, self.x2 + 1):
                y_coordinates.append(i)
            y_coordinates = [self.y1] * len(x_coordinates)
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


def get_diagram():
    pass


# Code
# Part 1
input = file_to_array('input.txt')
lines = get_lines(input)
print(lines[0].x1)
