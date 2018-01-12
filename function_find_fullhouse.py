P = 0
T = 0
FH = 0
sFH = 0
sP = 0
sT = 0
def full_house(lst):
        fh = []
        lst.sort()
        for j in range(2,15):
                fh.insert(j, lst.count(j))
        
        for i in range(0, 13):
                if fh[i] == 2:
                        global P
                        global sP
                        P = P + 2
                        sP = sP + (i + 2) * 2
                if fh[i] == 3:
                        global T
                        global sT
                        T = 1
                        sT = (i + 2) * 3
        if P == 2 and T == 1:
                global FH
                global sFH
                FH = 1
                sFH = sP + sT
        if P == 4 and T == 1:
                FH = 1
                sFH = sP + sT


        
                



               
        
