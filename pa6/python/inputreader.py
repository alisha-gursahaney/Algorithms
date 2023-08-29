import clusterer


def main():
    k = int(input())
    n = int(input())
    distances = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        row = input().strip().split()
        for j in range(len(row)):
            distances[i][j] = float(row[j])
    clusterer.cluster_cost(k, distances)


main()
