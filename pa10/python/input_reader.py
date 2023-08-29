from k_means_cluster import k_means

def main():
    k = int(input().strip())
    n = int(input().strip())
    points = []
    for i in range(n):
        line = input().strip().split()
        point = (float(line[0]),float(line[1]))
        points.append(point)
    clusters = k_means(k, points)
    for i in range(k):
        print("cluster " + str(i) + ":")
        for p in clusters[i]:
            print('  ', p)

main()
