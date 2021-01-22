import random
import numpy as np
EMPTY = 0
PAINT = 1
CROSS = -1

class Cell:
    def __init__(self):
        self.status = random.randint(0,1)
    def __str__(self):
        x = [" ", "#", "X"]
        return x[self.status]
    def __repr__(self):
        return self.__str__()

class Table:
    def __init__(self,dim):
        self.table = [[Cell() for i in range(dim)] for j in range(dim)]
        self.rows_hints = []
        self.cols_hints = []
        for i in range(dim):
            r = 0
            c = 0
            rr = []
            cc = []
            for j in range(dim):
                if self.table[i][j].status == 1:
                    r +=1
                else:
                    if r != 0:
                        rr.append(r)
                        r = 0
                if self.table[j][i].status== 1:
                    c +=1
                else:
                    if c != 0:
                        cc.append(c)
                        c = 0
            if r != 0:
                rr.append(r)
                r = 0
            if c != 0:
                cc.append(c)
                c = 0
            if rr == []:
                rr = [0]
            if cc == []:
                cc = [0]
            self.rows_hints.append(rr)
            self.cols_hints.append(cc)

    def __str__(self):
        max_rows = max([len(x) for x in self.rows_hints])
        max_cols = max([len(x) for x in self.cols_hints])

        d = len(self.table)
        total_dims = [d + max_rows, d + max_cols]
        s = [[" " for i in range(total_dims[0])] for j in range(total_dims[1])]
        for i,r in enumerate(self.table):


            for j,x in enumerate(r):
                s[i+max_rows][j+max_cols] = "{}".format(self.table[i][j])
        for i,r in enumerate(self.rows_hints):
            for j,x in enumerate(r):
                s[i+max_cols][j] = x
        for i,r in enumerate(self.cols_hints):
            for j,x in enumerate(r):
                s[j][i+max_rows] = x
        st = "\n|"
        for i in s:
            for x in i:
                st += f"{x}|"
            st += "\n|"

        return st[:-1]

def find_consecutives(row,condition):
        """condition as f(x) -> bool"""
        c =  0
        consecutives = []
        coordinates = []
        for i,x in enumerate(row):
            if condition(x):
                if c == 0:
                    coordinates.append(i)
                c +=1
            elif c != 0:
                consecutives.append(c)
        if c!= 0:
            consecutives.append(c)
        return consecutives,coordinates
def apply_hints(row,hints):
    touched = []
    # find gaps
    gaps,coords = find_consecutives(row,lambda x: x != CROSS)
    # fill what we know of the gaps:
    cur_hint = 0
    for i,gap in enumerate(gaps):
        if gap < hints[cur_hint]: # the gap is not fillable
            row[coords[i]:coords[i]+gap] = CROSS
            touched.extend(range(coords[i],coords[i]+gap))
        elif gap == hints[cur_hint]:
            row[coords[i]:coords[i]+gap] = PAINT
            touched.extend(range(coords[i],coords[i]+gap))
            cur_hint += 1
        else: # gap > current hint
            #


    # check if the hints fill the row
    if sum(hints) + len(hints) -1 == np.size(row):
        i = 0
        for x in hints:
            for j in range(x):
                row[i] = PAINT
                touched.append(i)
                i+=1
            if (i < np.size(row)):
                row[i] = CROSS
                touched.append(i)
                i += 1




ta = Table(5)
print("{}".format(ta))
