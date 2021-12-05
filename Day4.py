import cProfile
import numpy as np

class Decoder1:
    def __init__(self, numbers, boards):

        found_first_winner = False
        boards_to_delete =  []
        for n in numbers:
            for i,t in enumerate(boards):
                if i in boards_to_delete:
                    continue
                b,s = t
                s[np.where(b == n)] = True
                winner = self.isCompleted(s)
                if winner:
                    if not found_first_winner:
                        print('first winner')
                        print(self.score(b, s, n))
                        found_first_winner = True
                    if (len(boards) - len(boards_to_delete)) == 1:#
                        print('last winner')
                        print(self.score(b, s, n))
                        return
                    
                    boards_to_delete.append(i)


    def isCompleted(self, shadow):
        if any(np.all(shadow, axis = 0)): return True
        if any(np.all(shadow, axis = 1)): return True
        return False

    def score(self, b, s, n):
        return np.sum(b[np.where(s == False)]) * n


if __name__ == '__main__':

    f = 'Day4.txt'
    seq = [l for l in open(f, mode='r').read().split('\n\n')]

    drawn_number = [int(i) for i in seq.pop(0).split(',')]

    boards = []

    for e in seq:
        b = np.asarray([n.split() for n in e.split('\n')], dtype=int)
        board = (b, np.full(b.shape, False))
        boards.append(board)

    cProfile.run('Decoder1(drawn_number, boards)')