directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
length = 0
p = None


def max_run(grid):
    # print('grid',grid)
    global length, p
    rows = len(grid)
    cols = len(grid[0])
    memory = [[-1 for j in range(cols)] for i in range(rows)]

    # recursive function
    def drain(i, j):
        global directions

        nonlocal memory, grid, rows, cols
        if memory[i][j] != -1:
            return memory[i][j]

        longest = 0

        for long, lat in directions:
            l, a = i + long, j + lat
            if 0 <= l < rows and 0 <= a < cols:
                if grid[i][j] > grid[l][a]:
                    path_len = drain(l, a)
                    longest = max(longest, path_len)

        memory[i][j] = longest + 1
        global length, p
        if memory[i][j] > length:
            length = memory[i][j]
            p = (i, j)

        return memory[i][j]

    for i in range(rows):
        for j in range(cols):
            # recursive call
            drain(i, j)

    path = [p]
    while memory[path[-1][0]][path[-1][1]] > 1:
        for long, lat in directions:
            l, a = path[-1][0] + long, path[-1][1] + lat
            if 0 <= l < rows and 0 <= a < cols and \
                    grid[path[-1][0]][path[-1][1]] > grid[l][a] and \
                    memory[l][a] == memory[path[-1][0]][path[-1][1]] - 1:
                path.append((l, a))
                break
    for i, j in path:
        print(i, j)
