HRF = ["10h", "Jh", "Qh", "Kh", "Ah"]
DRF = ["10d", "Jd", "Qd", "Kd", "Ad"]
CRF = ["10c", "Jc", "Qc", "Kc", "Ac"]
SRF = ["10s", "Js", "Qs", "Ks", "As"]
RF = 0
def royal_flush(lst):
    rH = 0
    rH = len(list(set(lst) & set(HRF)))
    if rH == 5:
        global RF
        RF = 1
    rD = 0
    rD = len(list(set(lst) & set(DRF)))
    if rD == 5:
        RF = 1
    rC = 0
    rC = len(list(set(lst) & set(CRF)))
    if rC == 5:
        RF = 1
    rS = 0
    rS = len(list(set(lst) & set(SRF)))
    if rS == 5:
        RF = 1
    


