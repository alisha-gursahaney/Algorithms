import math
#import company


# s1 = 0
# s2 = 0
#
# e1 = -1
# e2 = -1

# def find_m(x):
#     n = x.size
#     if n % 2 == 0:
#         middle = n // 2
#         m = (x.request(middle - 1) + x.request(middle)) / 2
#     else:
#         m = x.request(int(n / 2))
#     return m


def find_median(c1, c2):
    global s1,s2,e1,e2
    s1 = 0
    s2 = 0
    e1 = c1.size -1
    e2 = c2.size -1

    def med(c,s,e):
        n = e+1
        if n % 2 == 0:
            middle = n // 2
            m = (c.request(middle - 1) + c.request(middle)) / 2
        else:
            m = c.request(int(n / 2))
        return m

    def recurs(c1,c2):
        # base case
        global s1,s2,e1,e2
        if c1.size + c2.size <= 4:
            return med(c1, s1, e1)
        # return (find_m(c1) + find_m(c2)) /2
        else:
            if med(c1, s1, e1) == med(c2, s2, e2):
                return med(c1, s1, e1)
            elif med(c1,s1,e1) < med(c2,s2,e2):
                s1 = int(e1/2)
                e2 = int(e2/2) + 1
                return recurs(c1,c2)
            else:
                s2 = int(e2/2)
                e1 = int(e1/2) + 1
                return recurs(c1,c2)


#c1 = [12.2,21.5,22.7,29.0,37.3] # m = 22.7
#c2 = [13.5,22.1,25.6,28.9,33.4] # m = 25.6

#print(find_median(c1,c2))