import java.io.*;
import java.util.*;

public class Subprime{

    public static void subprime_path(ArrayList<ArrayList<Pair>> capacities, ArrayList<ArrayList<Pair>> loads, int start, int end){
        System.out.println("Hello World.");
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        int c = s.nextInt();
        ArrayList<ArrayList<Pair>> capacities = new ArrayList<ArrayList<Pair>>();
        ArrayList<ArrayList<Pair>> loads = new ArrayList<ArrayList<Pair>>();
        for (int i = 0; i < c; i++){
            capacities.add(new ArrayList<Pair>());
            String nextline = s.next();
            if (nextline.startsWith(".")){continue;}
            String[] pairs = nextline.split(";",0);
            for (String p : pairs){
                String[] pair = p.split(",",0);
                int destination = Integer.parseInt(pair[0]);
                int weight = Integer.parseInt(pair[1]);
                capacities.get(i).add(new Pair(destination,weight));
            }
        }
        for (int i = 0; i < c; i++){
            loads.add(new ArrayList<Pair>());
            String nextline = s.next();
            if (nextline.startsWith(".")){continue;}
            String[] pairs = nextline.split(";",0);
            for (String p : pairs){
                String[] pair = p.split(",",0);
                int destination = Integer.parseInt(pair[0]);
                int weight = Integer.parseInt(pair[1]);
                loads.get(i).add(new Pair(destination,weight));
            }
        }
        int start = s.nextInt();
        int end = s.nextInt();
        subprime_path(capacities, loads, start, end);
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