# Alisha Meena Gursahaney
# amg9zd

import heapq as pq

global c

def build_adjl(v, e):
    adjl = [[] for node in v]
    for edge in e:
        source = edge[0]
        dest = edge[1]
        weight = edge[2]
        adjl[source].append((dest, weight))
    return adjl


def weight_percentage_graph(load_graph, capacity_graph):
    total_graph = []
    for i in range(0, len(load_graph)):
        weight_graph = []
        for j in range(0, len(load_graph[i])):
            #if load_graph[i][j][0] == capacity_graph[i][j][0]:
            node = load_graph[i][j][0]
            percentage = float(load_graph[i][j][1] / capacity_graph[i][j][1]) * 100
            weight_graph.append((node,percentage))
        total_graph.append(weight_graph)
    return total_graph


def dijkstras(graph, start, end):
    done = [False for node in graph]
    heap = []

    distance = [float('inf') for node in graph]
    distance[start]=0
    pq.heappush(heap,(distance[start],start))
    path = [None for node in graph]
    path[start] = start
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
                if new_distance < distance[next_node] and edge_weight < 100:
                    distance[next_node] = new_distance
                    path[next_node] = current_node
                    pq.heappush(heap, (new_distance, next_node))
    final = []
    i = end
    #print(distance)
    #print(path)
    final.append(end)
    while i != start:
        final.append(path[i])
        i = path[i]
    final.reverse()
    for n in final:
        print(n)
    return #distance[end]


def subprime_path(capacity_graph, load_graph, start, end):
    new_graph = weight_percentage_graph(load_graph,capacity_graph)
    dijkstras(new_graph,start,end)



def main():
    global c
    c = int(input())
    adjl_capacities = [[] for i in range(c)]
    adjl_loads = [[] for i in range(c)]
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_capacities[i].append((int(pair[0]),int(pair[1])))
    for i in range(c):
        line = input().strip()
        if line.startswith('.'):
            continue
        pairs = line.split(';')
        for p in pairs:
            pair = p.split(',')
            adjl_loads[i].append((int(pair[0]),int(pair[1])))
    start = int(input())
    end=int(input())
    subprime_path(adjl_capacities,adjl_loads,start,end)

main()