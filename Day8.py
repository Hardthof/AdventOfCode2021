import cProfile

class Decoder1:
    def __init__(self, seq):
        finalsum = 0
        count = {}
        values = {}
        for line in seq:
            patterns,output = line.split(' | ')
            #print(output)
            for p in patterns.split():
                if len(p) == 2:
                    values[1] = set(p)
                elif len(p) == 3:
                    values[7] = set(p)
                elif len(p) == 4:
                    values[4] = set(p)
                elif len(p) == 7:
                    values[8] = set(p)

            for p in patterns.split():
                if len(p) == 6:
                    new = set(p)
                    if not values[1].issubset(new):
                        values[6] = new
                    elif values[4].issubset(new):
                        values[9] = new
                    else: values[0] = new
                elif len(p) == 5:
                    new = set(p)
                    if values[1].issubset(new):
                        values[3] = new
                    elif values[4].difference(values[1]).issubset(new):
                        values[5] = new
                    else:
                        values[2] = new

            displayed = []
            for code in output.split():
                #print(code)
                if len(code) == 2:
                    count[1] = count.get(1, 0) + 1
                elif len(code) == 3:
                    count[7] = count.get(7, 0) + 1
                elif len(code) == 4:
                    count[4] = count.get(4, 0) + 1
                elif len(code) == 7:
                    count[8] = count.get(8, 0) + 1

                displayed.append(list(values.keys())[list(values.values()).index(set(code))])
            
            # ugly conversion of list [1, 2, 3, 4] to number
            v = int("".join([str(integer) for integer in displayed]))
            print(v)
            finalsum += v

        print('p1: ', sum(count.values()))
        print('p2: ', finalsum)


if __name__ == '__main__':

    f = open('Day8.txt', mode='r')
    seq = f.read().split('\n')
    cProfile.run('Decoder1(seq)')
