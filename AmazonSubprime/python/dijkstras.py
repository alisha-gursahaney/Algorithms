import heapq as pq

v = [0,1,2,3,4,5,6,7]
e = [(0,1,30),(0,4,5),(1,2,30),(2,3,30),(3,1,2),(4,3,201),(4,5,5),(5,2,100),(5,6,5),(6,7,50),(7,3,5)]

def build_adjl(v, e):
    adjl = [[] for node in v]
    for edge in e:
        source = edge[0]
        dest = edge[1]
        weight = edge[2]
        adjl[source].append((dest, weight))
    return adjl


def dijkstras(graph, start, end):
    done = [False for node in graph]
    heap = []
    distance = [float('inf') for node in graph]
    distance[start]=0
    pq.heappush(heap,(distance[start],start))
    while len(heap)>0:
        current = pq.heappop(heap)
        current_node = current[1]
        current_dist = current[0]
        done[current_node] = True
        neighbors = graph[current_node]
        for item in neighbors:
            next_node = item[0]
            edge_weight = item[1]
            if not done[next_node]:
                new_distance = current_dist + edge_weight
                if new_distance < distance[next_node]:
                    distance[next_node] = new_distance
                    pq.heappush(heap, (new_distance,next_node))
    return distance[end]

a = [[0.0, 18.0, 21.0, 23.0, 5.0], [18.0, 0.0, 54.0, 30.0, 31.0], [21.0, 54.0, 0.0, 15.0, 32.0], [23.0, 30.0, 15.0, 0.0, 15.0], [5.0, 31.0, 32.0, 15.0, 0.0]]
b = 3
n = 0
print(dijkstras(a,n,b))
