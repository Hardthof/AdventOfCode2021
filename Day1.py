import cProfile

class Decoder1:
    def __init__(self, seq):
        print("Depth increased " + str(self.countDepthIncreases(seq)) + " times.")
        slidingSeq = [seq[i]+seq[i+1]+seq[i+2] for i in range(len(seq) - 2)]
        print("Sliding Depth increased " + str(self.countDepthIncreases(slidingSeq)) + " times.")

    def countDepthIncreases(self, seq):
        res = 0
        for i,e in enumerate(seq):
            if i == 0: continue
            if e > seq[i-1]: 
                res = res + 1
        return res


if __name__ == '__main__':

    f = open('Day1.txt', mode='r')
    seq = [int(x) for x in f.read().split('\n')]
    cProfile.run('Decoder1(seq)')
