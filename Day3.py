import cProfile
import pandas as pd

class Decoder1:
    def __init__(self, df):
        self.gr = ''
        self.er = ''
        for v in df.sum(axis=0):
            if 2*v < df.shape[0]:
                self.gr += '0'  
                self.er += '1' 
            else:
                self.gr += '1'
                self.er += '0'

        result = int(self.gr, 2) * int(self.er, 2)
        print("result is", result, int(self.gr), int(self.er))


class Decoder2:
    def __init__(self, df):
        self.oxygen  = ''
        self.co2 = ''
        self.iterate(df)
        result = int(self.oxygen, 2) * int(self.co2, 2)
        print("result is", result, int(self.co2), int(self.co2))

    def iterate(self, df):

        df2 = df.copy()
    
        #iterate through all columns
        for c in df:
            if df.shape[0] <= 1: return
            if df[c].sum() >= df.shape[0] / 2: # more or equal 1s
                self.oxygen += '1'
                df = df.loc[df[c] == 1]
            else: #more 0s
                self.oxygen += '0'
                df = df.loc[df[c] == 0]


        for c in df2:
            if df2.shape[0] <= 1:
                self.co2 = ''.join([str(s) for s in df2.values.tolist()[0]])
                return
            if df2[c].sum() >= df2.shape[0] / 2: # more or equal 1s
                df2 = df2.loc[df2[c] == 0]
            else: #more 0s
                df2 = df2.loc[df2[c] == 1]

    
if __name__ == '__main__':

    f = open('Day3.txt', mode='r')
    seq = f.read().split('\n')
    seq = [list(s) for s in seq]
    df = pd.DataFrame(seq).astype(int)
    #cProfile.run('Decoder1(df)')
    Decoder2(df)

