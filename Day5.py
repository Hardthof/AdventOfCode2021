import cProfile
from itertools import product
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.points = self.get_points()

    def get_points(self):
        x_range = [self.start.x, self.end.x]
        y_range = [self.start.y, self.end.y]
        x_range.sort()
        y_range.sort()
        return [Point(*t) for t in product(range(x_range[0], (x_range[1]+1)), range(y_range[0], (y_range[1]+1)))]


class Dline:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.points = self.get_points()

    def get_points(self):
        length = abs(self.start.x - self.end.x)
        slopex = 1
        if self.start.x > self.end.x: slopex = -1
        slopey = 1
        if self.start.y > self.end.y: slopey = -1
        return [Point(self.start.x + i * slopex, self.start.y+i * slopey) for i in range(length + 1)]


class Decoder1:
    def __init__(self, seq):
        lines = []
        dlines = []
        max_x = 0
        max_y = 0
        for line in seq:
            points =  line.split(' -> ')
            p1 = self.str_point_to_point(points[0])
            p2 = self.str_point_to_point(points[1])
            max_x = max(max_x, p1.x, p2.x)
            max_y = max(max_y, p1.y, p2.y)
            if p1.x == p2.x or p1.y == p2.y:
                lines.append(Line(p1, p2))
            else: # make dlines
                dlines.append(Dline(p1, p2))
        
        card = np.zeros(((max_x+1), (max_y+1)))

        for l in lines:
            for p in l.points:
                card[p.x][p.y] += 1

        print('part1')
        print(len(card[card > 1]))

        for l in dlines:
            for p in l.points:
                card[p.x][p.y] += 1

        print('part2')
        print(len(card[card > 1]))

    def str_point_to_point(self, str_point):
        coords = [int (n) for n in str_point.split(',')]
        return Point(coords[0], coords[1])

if __name__ == '__main__':

    f = open('Day5.txt', mode='r')
    seq = [x for x in f.read().split('\n')]
    cProfile.run('Decoder1(seq)')
