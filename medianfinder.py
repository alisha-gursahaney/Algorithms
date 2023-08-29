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
        m = (c.request(middle) + c.request((middle+1))) / 2
    else:
        m = c.request(middle)
    return m


def recurs(c1, c2):
    global s1, s2, e1, e2
    # base case
    if e1+1-s1 + e2+1-s2 <= 4:
        x = c1.request(s1)
        x2 = c1.request(e1)
        y = c2.request(s2)
        y2 = c2.request(e2)
        if x < y2:
            return (x2 + y) / 2
        else:
            return (x + y2) / 2
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
    e1 = c1.size - 1
    e2 = c2.size - 1
    return recurs(c1, c2)