import math
import random
import medianfinder

class Company:
    # Company.size contains size of the array of values, you may reference this
    # Company._list contains the list of values, do not use, do not use in final submission
    # Company._queries_left tracks number of queries remaining, do not use in final submission
    # Company._queried tracks which indices have been previously queried, do not use in final submission
    # Company._list contains the list of values, do not use, do not use in final submission
    def __init__(self, size, alist=[]):
        # Constructor for Company, if you give it just a size then it populates the list
        # with random values. If you additionally give it a list then it will use the list
        # instead, provided the length of the list matches the given size.
        self.size = size
        if len(alist) == size:
            self._list = alist
        else:
            self._list = sorted(random.sample(range(5*size**3), size))
        self._queries_left = 1 + 2*math.ceil(math.log(size, 2))
        self._queried = set()

    def __repr__(self):
        # for debugging purposes only, prints list of values with only previously-queried values visible,
        # do not use in final submission
        listcopy = list(self._list)
        for i in range(len(listcopy)):
            if i not in self._queried:
                listcopy[i] = "??"
        return repr(listcopy)

    def __str__(self):
        return repr(self)

    def printall(self):
        # For debugging purposes only, prints the entire list of values,
        # do not use in final submission
        print(self._list)

    def slice(self, start, end):
        # for debugging purposes only, returns a slice of the list of values,
        # do not use in final submission
        return self._list[start:end]

    def lessthan(self,val):
        # for solution checking only, returns the number of values less than val,
        # do not use in final submission
        self._queries_left = 0
        count = 0
        for item in self._list:
            if item < val:
                count += 1
        return count

    def greaterthan(self,val):
        # for solution checking only, returns the number of values greater than val,
        # do not use in final submission
        self._queries_left = 0
        count = 0
        for item in self._list:
            if item > val:
                count += 1
        return count

    def request(self, i):
        # returns the value at index i of the list of values.
        # This should be the only method you use.
        if self._queries_left <= 0:
            print("out of queries")
            return -1
        self._queries_left -= 1
        self._queried.add(i)
        return self._list[i]


def check_median(c1, c2, answer):
    # for solution checking only, determines whether or not answer is the median value for companies c1 and c2,
    # do not use in final submission
    less = c1.lessthan(answer) + c2.lessthan(answer)
    greater = c1.greaterthan(answer) + c2.greaterthan(answer)
    if less == greater:
        print("median found!")
    else:
        print("response not the median")

def main():
    size = 20
    c1 = Company(size)
    c2 = Company(size)
    answer = medianfinder.find_median(c1, c2)
    check_median(c1, c2, answer)

main()
