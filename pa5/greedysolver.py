#import greedychooser
from greedychooser import *

class GreedySolver:
    def __init__(self, problem, inputlist):
        self.problem = problem
        self.inputlist = inputlist

    def choose(self):
        if self.problem == "bakeoff":
            return bakeoff(self.inputlist)
        elif self.problem == "deadlines":
            return deadlines(self.inputlist)
        else:
            return mileage(self.inputlist)


    def cost_bakeoff(self, schedule):
        elapsed = 0
        earliest_finish = 0
        for component in schedule:
            active = component[0]
            passive = component[1]
            elapsed += active
            earliest_finish = max(earliest_finish, elapsed+passive)
        return earliest_finish

    def cost_deadlines(self,schedule):
        elapsed = 0
        maximum_lateness = 0
        for task in schedule:
            time_taken = task[0]
            deadline = task[1]
            elapsed += time_taken
            lateness = max(elapsed-deadline,0)
            maximum_lateness = max(maximum_lateness, lateness)
        return maximum_lateness

    def cost_mileage(self, schedule):
        fuel_cost = 2
        spent = 0
        for car in schedule:
            mpg = car[0]
            miles = car[1]
            spent += miles/mpg * fuel_cost
            fuel_cost *= 1.05
        return spent


    def cost(self, schedule):
        if self.problem == "bakeoff":
            return self.cost_bakeoff(schedule)
        elif self.problem == "deadlines":
            return self.cost_deadlines(schedule)
        else:
            return self.cost_mileage(schedule)

    def solve(self):
        schedule = []
        while len(self.inputlist)>0:
            first = self.choose()
            schedule.append(self.inputlist[first])
            self.inputlist.pop(first)
        return schedule


def main():
    problem = input()
    length = int(input())
    input_list = []
    for i in range(length):
        line = input()
        input_list.append((float(line.strip().split()[0]),float(line.strip().split()[1])))
    greedy = GreedySolver(problem, input_list)
    schedule = greedy.solve()
    print("schedule:", schedule)
    print("cost", greedy.cost(schedule))

main()
