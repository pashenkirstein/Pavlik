#finding straight-flush-C
SF = 0
sSF = 0
CS1 = ["2c", "3c", "4c", "5c", "6c"]
CS2 = ["3c", "4c", "5c", "6c", "7c"]
CS3 = ["4c", "5c", "6c", "7c", "8c"]
CS4 = ["5c", "6c", "7c", "8c", "9c"]
CS5 = ["6c", "7c", "8c", "9c", "10c"]
CS6 = ["7c", "8c", "9c", "10c", "Jc"]
CS7 = ["8c", "9c", "10c", "Jc", "Qc"]
CS8 = ["9c", "10c", "Jc", "Qc", "Kc"]
CS9 = ["2c", "3c", "4c", "5c", "Ac"]
def straight_flush_c(lst):
    rC = len(list(set(lst) & set(CS1)))
    if rC >= 5:
        global SF
        global sSF
        SF = 1
        sSF = 20
    rC = len(list(set(lst) & set(CS2)))
    if rC >= 5:
        SF = 1
        sSF = 25
    rC = len(list(set(lst) & set(CS3)))
    if rC >= 5:
        SF = 1
        sSF = 30
    rC = len(list(set(lst) & set(CS4)))
    if rC >= 5:
        SF = 1
        sSF = 35
    rC = len(list(set(lst) & set(CS5)))
    if rC >= 5:
        SF = 1
        sSF = 40
    rC = len(list(set(lst) & set(CS6)))
    if rC >= 5:
        SF = 1
        sSF = 45
    rC= len(list(set(lst) & set(CS7)))
    if rC >= 5:
        SF = 1
        sSF = 50
    rC = len(list(set(lst) & set(CS8)))
    if rC >= 5:
        SF = 1
        sSF = 55
    rC = len(list(set(lst) & set(CS9)))
    if rC >= 5:
        SF = 1
        sSF = 15