import java.io.*;
import java.util.*;

public class Dijkstras{

    public static ArrayList<ArrayList<Pair>> build_adjl(int[] v, int[][] e){
        ArrayList<ArrayList<Pair>> adjl = new ArrayList<ArrayList<Pair>>();
        for (int i = 0; i < v.length; i++){
            adjl.add(new ArrayList<Pair>());
        }
        for (int i = 0; i < e.length; i++){
            int source = e[i][0];
            int dest = e[i][1];
            int weight = e[i][2];
            Pair p = new Pair(dest, weight);
            adjl.get(source).add(p);
        }
	return adjl;
    }

    public static int dijkstras(ArrayList<ArrayList<Pair>> graph, int start, int end){
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>();
        int[] distances = new int[graph.size()];
        for (int i = 0; i < distances.length; i++){
            distances[i] = Integer.MAX_VALUE;
        }
        boolean[] done = new boolean[graph.size()];
        distances[start] = 0;
        pq.add(new Pair(0, start));
        while(pq.size()>0){
            Pair current = pq.poll();
            int current_node = current.second;
            int current_dist = current.first;
            done[current_node] = true;
            ArrayList<Pair> neighbors = graph.get(current_node);
            for (Pair item : neighbors){
                int next_node = item.first;
                int edge_weight = item.second;
                if (!done[next_node]){
                    int new_dist = current_dist + edge_weight;
                    if (new_dist < distances[next_node]){
                        distances[next_node] = new_dist;
                        pq.add(new Pair(new_dist, next_node));
                    }
                }
            }
        } 
        return distances[end];
    }

    public static void main(String[] args){
        int[] v = {0,1,2,3,4,5,6,7};
        int[][] e = {{0,1,30},{0,4,5},{1,2,30},{2,3,30},{3,1,2},{4,3,201},{4,5,5},{5,2,100},{5,6,5},{6,7,50},{7,3,5}};
        ArrayList<ArrayList<Pair>> adjl = build_adjl(v,e);
        System.out.println(dijkstras(adjl, 0, 3));
    }

}

class Pair implements Comparable<Pair>{
    public int first;
    public int second;
    public Pair(int a1, int a2) {
        first = a1;
        second = a2;
    }

    public boolean equals(Pair other){
        return (this.first == other.first) && (this.second == other.second);
    }

    public int hashCode(){
        return this.first ^ this.second;
    }

    public int compareTo(Pair other){
        if (this.first != other.first){
            return this.first - other.first;
        }
        return this.second - other.second;
    }

    public String toString(){
        return "(" + this.first + "," + this.second + ")";
    }
}

