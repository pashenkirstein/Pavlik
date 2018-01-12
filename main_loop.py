def main_loop():
    # creating card deck
    l = ["2h", "2d", "2c", "2s",
         "3h", "3d", "3c", "3s",
         "4h", "4d", "4c", "4s",
         "5h", "5d", "5c", "5s",
         "6h", "6d", "6c", "6s",
         "7h", "7d", "7c", "7s",
         "8h", "8d", "8c", "8s",
         "9h", "9d", "9c", "9s",
         "10h", "10d", "10c", "10s",
         "Jh", "Jd", "Jc", "Js",
         "Qh", "Qd", "Qc", "Qs",
         "Kh", "Kd", "Kc", "Ks",
         "Ah", "Ad", "Ac", "As"]

    # creating yours hand
    from random import random
    h1 = []
    m1 = 0
    m2 = 51
    n = int(random() * (m2-m1+1)) + m1
    print ("yours hand:")
    h1.append(l[n])
    l.pop(n)
    m2 = 50
    n = int(random() * (m2-m1+1)) + m1
    h1.append(l[n])
    l.pop(n)
    print(h1)

    # creating flop
    print ("")
    m2 = 47
    n = int(random() * (m2-m1+1)) + m1
    t = [] #creating table list
    t.append(l[n]) #table list
    l.pop(n)
    m2 = 46
    n = int(random() * (m2-m1+1)) + m1
    t.append(l[n]) #table list
    l.pop(n)
    m2 = 45
    n = int(random() * (m2-m1+1)) + m1
    t.append(l[n]) #table list
    l.pop(n)
    print("flop:")
    print(t)
    print("")

    # creating turn
    m2 = 44
    n = int(random() * (m2-m1+1)) + m1
    t.append(l[n]) #table list
    l.pop(n)
    print("turn:")
    print(t)
    print("")

    # creating river
    m2 = 43
    n = int(random() * (m2-m1+1)) + m1
    t.append(l[n]) #table list
    l.pop(n)
    print("river:")
    print(t)
    print("")

    #full combination
    print("you have:")
    g1 = h1 + t
    print(g1)
    print("")

    # full combination (digits)
    gasAA=[0,0,0,0,0,0,0]
    for i in g1:    
            if i == "2h" or i == "2d" or i == "2c" or i == "2s":
                a2 = g1.index(i)
                gasAA.pop(a2)
                gasAA.insert(a2, 2)            
    for i in g1:    
            if i == "3h" or i == "3d" or i == "3c" or i == "3s":
                a3 = g1.index(i)
                gasAA.pop(a3)
                gasAA.insert(a3, 3)            
    for i in g1:    
            if i == "4h" or i == "4d" or i == "4c" or i == "4s":
                a4 = g1.index(i)
                gasAA.pop(a4)
                gasAA.insert(a4, 4)            
    for i in g1:    
            if i == "5h" or i == "5d" or i == "5c" or i == "5s":
                a5 = g1.index(i)
                gasAA.pop(a5)
                gasAA.insert(a5, 5)                   
    for i in g1:    
            if i == "6h" or i == "6d" or i == "6c" or i == "6s":
                a6 = g1.index(i)
                gasAA.pop(a6)
                gasAA.insert(a6, 6)                     
    for i in g1:    
            if i == "7h" or i == "7d" or i == "7c" or i == "7s":
                a7 = g1.index(i)
                gasAA.pop(a7)
                gasAA.insert(a7, 7)          
    for i in g1:    
            if i == "8h" or i == "8d" or i == "8c" or i == "8s":
                a8 = g1.index(i)
                gasAA.pop(a8)
                gasAA.insert(a8, 8)            
    for i in g1:    
            if i == "9h" or i == "9d" or i == "9c" or i == "9s":
                a9 = g1.index(i)
                gasAA.pop(a9)
                gasAA.insert(a9, 9)            
    for i in g1:    
            if i == "10h" or i == "10d" or i == "10c" or i == "10s":
                a10 = g1.index(i)
                gasAA.pop(a10)
                gasAA.insert(a10, 10)            
    for i in g1:    
            if i == "Jh" or i == "Jd" or i == "Jc" or i == "Js":
                a11 = g1.index(i)
                gasAA.pop(a11)
                gasAA.insert(a11, 11)           
    for i in g1:    
            if i == "Qh" or i == "Qd" or i == "Qc" or i == "Qs":
                a12 = g1.index(i)
                gasAA.pop(a12)
                gasAA.insert(a12, 12)            
    for i in g1:    
            if i == "Kh" or i == "Kd" or i == "Kc" or i == "Ks":
                a13 = g1.index(i)
                gasAA.pop(a13)
                gasAA.insert(a13, 13)            
    for i in g1:    
            if i == "Ah" or i == "Ad" or i == "Ac" or i == "As":
                a14 = g1.index(i)
                gasAA.pop(a14)
                gasAA.insert(a14, 14)
    weight = 0
    summ = 0

    #check on Royal-flush
    while weight == 0:
            from function_find_royalflush import royal_flush
            royal_flush(g1)
            from function_find_royalflush import RF
            if RF == 1:
                    weight = 10                
    #check on straight-flash (H)
            from function_find_straightflush_h import straight_flush_hearts
            straight_flush_hearts(g1)
            from function_find_straightflush_h import SF
            from function_find_straightflush_h import sSF
            if SF == 1:
                    weight = 9
                    summ = sSF                
    #check on straight-flash (D)
            from function_find_straightflush_d import straight_flush_d
            straight_flush_d(g1)
            from function_find_straightflush_d import SF
            from function_find_straightflush_d import sSF
            if SF == 1:
                    weight = 9
                    summ = sSF                
    #check on straight-flash (C)
            from function_find_straightflush_c import straight_flush_c
            straight_flush_c(g1)
            from function_find_straightflush_c import SF
            from function_find_straightflush_c import sSF
            if SF == 1:
                    weight = 9
                    summ = sSF
    #check on straight-flash (S)
            from function_find_straightflush_s import straight_flush_s
            straight_flush_s(g1)
            from function_find_straightflush_s import SF
            from function_find_straightflush_s import sSF
            if SF == 1:
                    weight = 9
                    summ = sSF
    #check on quads
            from function_find_quads import quads
            quads(g1)
            from function_find_quads import Q
            from function_find_quads import sQ
            if Q == 1:
                    weight = 8
                    summ = sQ
    #check on full house
            if weight == 0:
                    from function_find_fullhouse import full_house
                    full_house(gasAA)
                    from function_find_fullhouse import P
                    from function_find_fullhouse import sP
                    from function_find_fullhouse import T
                    from function_find_fullhouse import sT
                    from function_find_fullhouse import FH
                    from function_find_fullhouse import sFH
                    if P == 4 and T == 1:
                            weight = 7
                            summ = sFH
                    if P == 2 and T == 1:
                            weight = 7
                            summ = sFH
    #check on flush

    #check on straight
            if weight == 0:
                    from function_find_straight import straight
                    straight(gasAA)
                    from function_find_straight import S
                    from function_find_straight import sS
                    if S == 1:
                            weight = 5
                            summ = sS
    #check on triple
            if weight == 0:
                    if T == 1:
                            weight = 4
                            summ = sT
    #check on two pairs
            if weight == 0:
                    if P == 4:
                            weight = 3
                            summ = sP
                    if P == 6:
                            weight = 3
                            summ = sP
    #check on pair
            if weight == 0:
                    if P == 2:
                            weight = 2
                            summ = sP
    #check on high card
            if weight == 0:
                    weight = 1
                    summ = max(gasAA)
    else:
            print("tutk")
