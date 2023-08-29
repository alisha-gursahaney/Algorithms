
def distance(p1, p2):
    # Calculates the Euclidean Distance between two points
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5


def centroid(points):
    # Computes the centroid of a set of points.
    # The centroid is the "average" point in the set.
    # That is, its x coordinate is the average x among the points in the set
    # and the y coordinate is the average y among the points in the set.
    x = 0
    y = 0
    for each in points:
        x += each[0]
        y += each[1]
    x_value = x/len(points)
    y_value = y/len(points)
    return (x_value, y_value)


def cluster(reference, points):
    # Clusters the given points using the reference points.
    # Points in the same cluster should be closest to the same reference point.
    # In other words, if points A and B are in cluster i then they should both be
    # closer to reference point i than any of the other reference points.
    #print(points)
    clusters = [[] for i in range(len(reference))]
    for each in points:
        min_distance = float("inf")
        closest = None
        for i, ref in enumerate(reference):
            d = distance(each, ref)
            #print(d)
            # loop through and find minimum value in d
            if d < min_distance:
                min_distance = d
                closest = i
                # print(closest)
        clusters[closest].append(each)
        #print(each)
        #print(closest)
    return clusters


def k_means(k, points):
    # Performs the k-means clustering.
    #print(k)
    #print(points)
    reference_points = points[:k]  # our initial reference points
    while True:
        clusters = cluster(reference_points, points)
        new_reference_points = []
        for c in clusters:
            #print(c)
            x = centroid(c)
            new_reference_points.append(x)
        if reference_points == new_reference_points:
            break
        reference_points = new_reference_points
        #print(new_reference_points)
    return clusters
