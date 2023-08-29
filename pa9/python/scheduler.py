from flownetwork import *
from collections import defaultdict
from typing import List

def schedule(stationcounts, stationtimes, employeetraining, employeetimes):
    """station counts: a list of length 4 containing (in order):
    number of employees per shift on blending
    number of employees per shift on cooking
    number of employees per shift on straining
    number of employees per shift on finishing

    stationtimes:  list of lists of length 4 containing (in order):
    shift times for blending
    shift times for cooking
    shift times for straining
    shift times for finishing

    employeetraining: index i contains the list of stations that employee i is trained to work on
    empolyeetimes: index i contains the list of times that employee i can work
    """
    stations = ["blend", "cook", "strain", "finish"]
    shifts = defaultdict(list)
    for i in range(len(stations)):
        for j in range(len(stationtimes[i])):
            shifts[stations[i]].append((stationtimes[i][j], stationcounts[i]))

    # Create a list of employees, their training, and their availability
    employees = []
    for i in range(len(employeetraining)):
        employees.append((i, employeetraining[i], employeetimes[i]))

    # Create a graph with a source, sink, and a node for each employee and shift
    graph = graph = flownetwork(len(employees) + len(shifts) + 2, len(shifts) + 1)
    source = 0
    sink = len(employees) + len(shifts) + 1

    # Connect the source to each employee node
    for i in range(len(employees)):
        graph.add_edge(source, i + 1, 1)

    # Connect each employee node to the shifts they can work
    for i in range(len(employees)):
        for j in range(len(employees[i][1])):
            station = employees[i][1][j]
            for k in range(len(shifts[station])):
                shift = shifts[station][k]
                if employees[i][2][0] <= shift[0] and employees[i][2][-1] >= shift[0]:
                    for l in range(shift[1]):
                        graph.add_edge(i + 1, len(employees) + k + 1, 1)

    # Connect the shift nodes to the sink
    for i in range(len(shifts)):
        for j in range(len(shifts[stations[i]])):
            shift = shifts[stations[i]][j]
            graph.add_edge(len(employees) + j + 1, sink, shift[1])

    # Use max flow to determine if all shifts can be staffed
    return graph.max_flow(source, sink) == sum(stationcounts) * len(stationtimes[0])



