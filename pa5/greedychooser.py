
def bakeoff(input_list):
    # input: a list of pairs or floats (active time, passive time)
    # output: index of the component to make first
    # start with component with most passive time to complete all active time in the meantime
    # sort by descending passive time
    x = 0
    index = float('inf')
    for i in range(0, len(input_list)):
        if int(input_list[i][1]) > x:
            x = input_list[i][1]
            index = i
    return index

def deadlines(input_list):
    # input: a list of pairs or floats (completion time, due time)
    # output: index of the assignment to complete first
    # sort by descending deadline
    # start with earliest deadline
    x = float('inf')
    index = float('inf')
    for i in range(0, len(input_list)):
        if int(input_list[i][1]) < x:
            x = input_list[i][1]
            index = i
    return index

def mileage(input_list):
    # input: a list of pairs or floats (mpg, miles)
    # output: index of the car to deliver first
    # sort in order of g = m/e
    # want to find the car that requires the most amount of gas and deliver that first
    x = 0
    index = float('inf')
    for i in range(0, len(input_list)):
        if int(input_list[i][1])/int(input_list[i][0]) > x:
            x = int(input_list[i][1])/int(input_list[i][0])
            index = i
    return index
