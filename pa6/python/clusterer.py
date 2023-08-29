import heapq as pq


def cluster_cost(k, distances):
    # groups = []
    # for i in range(0, len(distances)):
    #     # use dictionary to avoid repeats
    #     groups.append({i})
    groups = [{i} for i in range(0,len(distances))]
    # print('distances', distances)
    # print('k', k)
    # print('groups', groups)
    closest = []
    for i in range(0, len(distances)):
        for j in range(i + 1, len(distances)):
            # use heap for ordering
            # push value onto heap
            pq.heappush(closest, (distances[i][j], i, j))
    # print('closest', closest)
    # cluster sizes
    while k < len(groups):
        # pop value off heap
        dist, i, j = pq.heappop(closest)
        x = 0
        y = 0
        for each in groups:
            # print(each)
            if i in each:
                x = each
            if j in each:
                y = each
        # change dictionary
        x.update(y)
        # groups is now clustered
        groups.remove(y)
    # print('groups', groups)
    # initialize cost to infinity to iterate through all values and find the minimum cost
    cost = float('inf')
    for i in range(0, len(groups)):
        # start second for loop on 1 element past i
        a = list(groups[i])
        for j in range(i + 1, len(groups)):
            # print('a', a)
            b = list(groups[j])
            # print('b', b)
            for c in a:
                # print('c', c)
                for d in b:
                    # print('d', d)
                    # find minimum distance and update cost variable
                    # if distances[c][d] < cost:
                    #     cost = distances[c][d]
                    cost = min(distances[c][d], cost)
    print(cost)
    return cost
