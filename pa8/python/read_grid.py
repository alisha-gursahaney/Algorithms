import drainage

def main():
    line1 = input().strip().split()
    r = int(line1[0])
    c = int(line1[1])
    grid = [[] for i in range(r)]
    for i in range(r):
        line = input().strip().split()
        for j in range(c):
            grid[i].append(int(line[j]))
    drainage.max_run(grid)

main()
