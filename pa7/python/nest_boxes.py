
def max_depth(boxes):
    #print(boxes)
    n = len(boxes)
    # initialize array of size n and update values later
    memory = [1] * n
    #print(memory)
    # sort boxes in descending order
    boxes.sort(key=lambda b: (-b.l, b.w))
    for i in range(1, n):
        for j in range(0, i):
            # if dimensions of i box are less than box j, then it can fit inside
            if boxes[i].l < boxes[j].l and boxes[i].w < boxes[j].w and boxes[i].h < boxes[j].h:
                memory[i] = max(memory[i], memory[j] + 1)
    #print(memory)
    depth = max(memory)
    # print(depth)
    return depth





