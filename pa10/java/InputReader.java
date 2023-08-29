import java.util.*;
import java.io.*;

public class InputReader{

    public static void main (String[] args){
        Scanner s = new Scanner(System.in);
	int k = s.nextInt();
	//System.out.println(k);
        int n = s.nextInt();
	ArrayList<Point> points = new ArrayList<>();
	for (int i = 0; i < n; i ++){
            double x = s.nextDouble();
	    double y = s.nextDouble();
            Point p = new Point(x,y);
            points.add(p);
	}
	for (Point p : points){
             System.out.println(p);
	}
	ArrayList<ArrayList<Point>> clusters = KMeansCluster.k_means(k, points);
        for(int i = 0; i < k; i++){
            System.out.println("cluster " + i + ":");
	    for (Point p : clusters.get(i)){
	        System.out.println("  " + p);
	    }
	}
    } 

}
