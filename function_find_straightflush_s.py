#finding straight-flush-S

SF = 0
sSF = 0
SS1 = ["2s", "3s", "4s", "5s", "6s"]
SS2 = ["3s", "4s", "5s", "6s", "7s"]
SS3 = ["4s", "5s", "6s", "7s", "8s"]
SS4 = ["5s", "6s", "7s", "8s", "9s"]
SS5 = ["6s", "7s", "8s", "9s", "10s"]
SS6 = ["7s", "8s", "9s", "10s", "Js"]
SS7 = ["8s", "9s", "10s", "Js", "Qs"]
SS8 = ["9s", "10s", "Js", "Qs", "Ks"]
SS9 = ["2s", "3s", "4s", "5s", "As"]
def straight_flush_s(lst):
    rS = len(list(set(lst) & set(SS1)))
    if rS >= 5:
        global SF
        global sSF
        SF = 1
        sSF = 20
    rS = len(list(set(lst) & set(SS2)))
    if rS >= 5:
        SF = 1
        sSF = 25
    rS = len(list(set(lst) & set(SS3)))
    if rS >= 5:
        SF = 1
        sSF = 30
    rS = len(list(set(lst) & set(SS4)))
    if rS >= 5:
        SF = 1
        sSF = 35
    rS = len(list(set(lst) & set(SS5)))
    if rS >= 5:
        SF = 1
        sSF = 40
    rS = len(list(set(lst) & set(SS6)))
    if rS >= 5:
        SF = 1
        sSF = 45
    rS= len(list(set(lst) & set(SS7)))
    if rS >= 5:
        SF = 1
        sSF = 50
    rS = len(list(set(lst) & set(SS8)))
    if rS >= 5:
        SF = 1
        sSF = 55
    rS = len(list(set(lst) & set(SS9)))
    if rS >= 5:
        SF = 1
        sSF = 15

