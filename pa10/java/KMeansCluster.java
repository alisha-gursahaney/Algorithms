import java.util.*;

public class KMeansCluster{

    public static double distance(Point p1, Point p2){
        // Calculates the Euclidean Distance between two points
	double deltax = p1.x - p2.x;
	double deltay = p1.y - p2.y;
	return Math.sqrt(deltax * deltax + deltay * deltay);
    }

    public static Point centroid(ArrayList<Point> points){
        //Computes the centroid of a set of points.
        //The centroid is the "average" point in the set.
        //That is, its x coordinate is the average x among the points in the set
        //and the y coordinate is the average y among the points in the set.
	return new Point(0,0);
    }

    public static ArrayList<ArrayList<Point>> cluster(ArrayList<Point> reference, ArrayList<Point> points){
        //Clusters the given points using the reference points.
        //Points in the same cluster should be closest to the same reference point.
        //In other words, if points A and B are in cluster i then they should both be
        //closer to reference point i than any of the other reference points.
	return new ArrayList<ArrayList<Point>>();
    }

    public static ArrayList<ArrayList<Point>> k_means(int k, ArrayList<Point> points){
        //Performs the k-means clustering.
	ArrayList<Point> reference_points = new ArrayList<>();
	for (int i = 0; i < k; i++){
            reference_points.add(points.get(i));
	}

	//Using the reference points, cluster the points
	
	//calculate the new reference points by finding the centroid of each cluster
	
	//re-cluster the points using the centroids
	
	//repeat until the centroids do not change between iterations.
	
	//return a list of lists of points representing the clusters.
	return new ArrayList<ArrayList<Point>>();
    }

}
