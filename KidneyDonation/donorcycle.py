# Name: Alisha Meena Gursahaney
# Net Id: amg9zd

# Office Hours
# build matrix function
# size is n*n

# if 1,1 is a donor match, then put a 1 in that matrix spot
# if not, (less than 60)   then put a 0 in that matrix spot

# then call DFS on the matrix

def find_edges(match_scores, donor_friends):
    edges = []
    for i in range(0,len(match_scores)):
        #print(i)
        for j in range(0, len(match_scores[i])):
            #print(match_scores[i][j])
            if match_scores[i][j] >= 60:
                #print(match_scores[i][j])
                edges.append((j,donor_friends[i]))
    return edges

def isInCycle(match_scores,donor_friends,query):
    vertices = list(range(0,len(match_scores[0])))
    #print(vertices)
    edges = find_edges(match_scores, donor_friends)
    #print("edges")
    #print(edges)
    for i in edges:
        #print(i[0])
        if i[0] == query:
            return True
    return False

def take_input():
    n = int(input())
    m = int(input())
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []

    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    print(isInCycle(match_scores,donor_friends,query))

    # delete after
    # print("match scores")
    # print(match_scores)
    # print("donor friends")
    # print(donor_friends)
    # print("query")
    # print(query)

take_input()

# def build_adjacency_list(vertices,edges):
#     adj_list = []
#     for v in vertices:
#         adj_list.append([])
#     for e in edges:
#         adj_list[e[0]].append(e[1])
#     return adj_list








