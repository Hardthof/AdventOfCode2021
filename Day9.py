import cProfile
import numpy as np

class Decoder1:
    def __init__(self, b):
        s = np.full(b.shape, True)

        # 2x2 sliding window
        for x in range(b.shape[0] - 1):
            for y in range(b.shape[1] - 1):                
                # find min in b[sliding window]
                a = (b[x:x+2, y:y+2])
                res = np.where(a != a.min())
                s[res[0] + x, res[1] + y] = False


        print('result1: ', np.sum(b[s]) + len(b[s]))
        results = [self.findBasinvalue(b, c) for c in np.asarray(np.where(s == True)).T]
        print(np.prod(sorted(results, reverse=True)[:3]))

    def findBasinvalue(self, b, c):
        s = np.full(b.shape, False)
        v = np.full(b.shape, False)
        self.searchNeighbors(b, s, v, c)
        result = np.count_nonzero(s)
        return result

    def searchNeighbors(self, b, s, v, c):
        if v[c[0], c[1]] == True: return # visited before
        v[c[0], c[1]] = True
        x,y = c[0], c[1]
        s[x, y] = self.checkPos(b, x, y)
        if s[x,y] == False: return # path end

        # search up
        for x in reversed(range(0,c[0])):
            s[x, y] = self.checkPos(b, x, y)
            if not s[x, y]: break
            else: self.searchNeighbors(b, s, v, (x,y))

        # search down
        for x in range(c[0]+1, b.shape[0]):
            s[x, y] = self.checkPos(b, x, y)
            if not s[x, y]: break
            else: self.searchNeighbors(b, s, v, (x,y))

        # search left
        x = c[0]
        for y in reversed(range(0,c[1])):
            s[x, y] = self.checkPos(b, x, y)
            if not s[x, y]: break
            else: self.searchNeighbors(b, s, v, (x,y))

        for y in range(c[1] + 1, b.shape[1]):
            s[x, y] = self.checkPos(b, x, y)
            if not s[x, y]: break
            else: self.searchNeighbors(b, s, v, (x,y))

    def checkPos(self, b, x, y):
            return b[x, y] != 9

if __name__ == '__main__':

    f = 'Day9.txt'
    seq = [l for l in open(f, mode='r').read().split('\n')]

    board = []
    for e in seq:
        board.append([int(n) for n in e])
    board = np.asarray(board, dtype=int)

    cProfile.run('Decoder1(board)')