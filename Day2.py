import cProfile

class Decoder1:
    def __init__(self, seq):
        self.horizontal = 0
        self.depth = 0
        for m in seq:
            self.move(m)

        print(self.horizontal, self.depth)
        print("result is:", self.horizontal * self.depth)

    def move(self, m):
        c,v = m.split()
        v = int(v)
        if c == 'forward':
            self.horizontal = self.horizontal + v
            return
        elif c == 'up':
            v = v * -1
        self.depth = self.depth + v
            
class Decoder2:
    def __init__(self, seq):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
        for m in seq:
            self.move(m)

        print(self.horizontal, self.depth)
        print("result is:", self.horizontal * self.depth)

    def move(self, m):
        c,v = m.split()
        v = int(v)
        if c == 'forward':
            self.horizontal = self.horizontal + v
            self.depth = self.depth + self.aim * v
        elif c == 'up':
            self.aim = self.aim - v
        else:
            self.aim = self.aim + v

if __name__ == '__main__':

    f = open('Day2.txt', mode='r')
    seq = f.read().split('\n')
    Decoder1(seq)
    Decoder2(seq)
    #cProfile.run('Decoder1(seq)')
