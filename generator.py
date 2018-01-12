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
