import java.io.*;
import java.util.*;


public class InputReader{

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
	int k = s.nextInt();
	int n = s.nextInt();
	double[][] distances = new double[n][n];
	for(int i = 0; i < n; i++){
	    for(int j = 0; j < n; j++){
                distances[i][j] = Double.parseDouble(s.next());
	    }
	}
        Clusterer.cluster_cost(k, distances);

    }

}
