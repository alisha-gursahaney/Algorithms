# Name: Alisha Gursahaney
# Net Id: amg9zd

import math
#import company

s1 = 0
s2 = 0
e1 = -1
e2 = -1

def find_m(c,s,e):
    n = (e+1-s) # size of  array
    middle = (e + s) // 2
    if n % 2 == 0:
        m = (c[middle] + c[(middle+1)]) / 2
    else:
        m = c[middle]
    return m


def recurs(c1, c2):
    global s1, s2, e1, e2
    # base case
    if e1+1-s1 + e2+1-s2 <= 4:
        if c1[s1] < c2[e2]:
            return (c1[e1] + c2[s2])/2
        else:
            return (c1[s1] + c2[e1]) / 2
    # divide and conquer
    else:
        c1_m = find_m(c1, s1, e1)
        c2_m = find_m(c2, s2, e2)
        if c1_m == c2_m:
            return c1_m
        elif c1_m < c2_m:
            s1 = math.ceil((s1+e1)/2)
            e2 = (s2+e2)//2
            return recurs(c1,c2)
        else:
            s2 = math.ceil((s2 + e2) / 2)
            e1 = (s1 + e1) // 2
            return recurs(c1,c2)


def find_median(c1, c2):
    global s1, s2, e1, e2
    e1 = len(c1) - 1
    e2 = len(c2) - 1
    return recurs(c1, c2)


a = [12.2,21.5,22.7,29.0,37.3]
b = [13.5,22.1,25.6,28.9,33.4]

x = [1,2,10]
y = [3,4,5]

print(find_median(b,a))

print(find_median(x,y))