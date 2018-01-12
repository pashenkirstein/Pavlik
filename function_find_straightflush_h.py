#finding straight-flush-hearts
SF = 0
sSF = 0
HS1 = ["2h", "3h", "4h", "5h", "6h"]
HS2 = ["3h", "4h", "5h", "6h", "7h"]
HS3 = ["4h", "5h", "6h", "7h", "8h"]
HS4 = ["5h", "6h", "7h", "8h", "9h"]
HS5 = ["6h", "7h", "8h", "9h", "10h"]
HS6 = ["7h", "8h", "9h", "10h", "Jh"]
HS7 = ["8h", "9h", "10h", "Jh", "Qh"]
HS8 = ["9h", "10h", "Jh", "Qh", "Kh"]
HS9 = ["2h", "3h", "4h", "5h", "Ah"]
def straight_flush_hearts(lst):
    rH = len(list(set(lst) & set(HS1)))
    if rH >= 5:
        global SF
        global sSF
        SF = 1
        sSF = 20
    rH = len(list(set(lst) & set(HS2)))
    if rH >= 5:
        SF = 1
        sSF = 25
    rH = len(list(set(lst) & set(HS3)))
    if rH >= 5:
        SF = 1
        sSF = 30
    rH = len(list(set(lst) & set(HS4)))
    if rH >= 5:
        SF = 1
        sSF = 35
    rH = len(list(set(lst) & set(HS5)))
    if rH >= 5:
        SF = 1
        sSF = 40
    rH = len(list(set(lst) & set(HS6)))
    if rH >= 5:
        SF = 1
        sSF = 45
    rH = len(list(set(lst) & set(HS7)))
    if rH >= 5:
        SF = 1
        sSF = 50
    rH = len(list(set(lst) & set(HS8)))
    if rH >= 5:
        SF = 1
        sSF = 55
    rH = len(list(set(lst) & set(HS9)))
    if rH >= 5:
        SF = 1
        sSF = 15
    
    

