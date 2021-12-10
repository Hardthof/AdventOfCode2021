import cProfile
from statistics import median

score = {')':3, ']':57, '}':1197, '>':25137}
scoreI = {'(':1, '[':2, '{':3, '<':4}

class Decoder1:
    def __init__(self, seq):
        sum = 0
        incomplete = []
        for l in seq:
            s,l = self.lineScore(l)
            score = self.scoreIncomplete(l)
            if score > 0: incomplete.append(score)
            sum +=s
        print('p1: ', sum)
        print('p2: ', median(incomplete))

    def scoreIncomplete(self, l):
        #l = l[:-1]
        sum = 0
        for c in reversed(l):
            sum *= 5
            sum += scoreI[c]
        return sum

    def lineScore(self, l):
        search = set(['()','[]','{}', '<>'])
        
        while(len(l) > 0):
            reduced = False
            for s in search:
                i = l.find(s)
                if i != -1:
                    l = l[:i]+l[i+2:] # remove find
                    reduced = True
                    break
            if not reduced: break

        # find first closing and return score
        for c in list(l):
            if c in score: return score[c], ''
        return 0, l

if __name__ == '__main__':

    f = open('Day10.txt', mode='r')
    seq = f.read().split('\n')
    Decoder1(seq)
    #cProfile.run('Decoder1(seq)')
