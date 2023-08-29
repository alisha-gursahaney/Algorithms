import java.io.*;
import java.util.*;

public class Company{

    public int size; // The size of the array of values, you may reference this
    protected int queriesLeft; // tracks number of queries remaining, do not use in final submission
    protected Set<Integer> queried; // tracks which indices have been previously queried, do not use in final submission
    protected double[] list; // contains the list of values, do not use, do not use in final submission

    Company(int listsize){
        // Constructs a company with a random list of the given size, do not use in final submission
        this.size = listsize;
        Random rand = new Random();
        this.list = new double[listsize];
        this.queriesLeft = 1 + 2*(int) Math.ceil(Math.log(this.size)/ Math.log(2));
        this.queried = new HashSet<Integer>();
        for (int i = 0; i < listsize; i++){
            double val = (double) rand.nextInt(10000000);
            for (int j = 0; j < i; j++){
                if (val == list[j]){
                    val = (double) rand.nextInt(10000000);
                    j=0;
                }
            }
            this.list[i] = val;
        }
        Arrays.sort(this.list);
    }

    Company(double[] alist){
        // Constructs a company using the given list, do not use in final submission
        this(alist.length);
        this.list = alist;
    }

    public void printall(){
        // For debugging purposes only, prints the entire list of values, do not use in final submission
        String s = "[";
        for (int i = 0; i < this.list.length-1; i++){
            s += this.list[i] + ",";
        }
        s += this.list[this.list.length-1] + "]";
        System.out.println(s);
    }

    public String toString(){
        // for debugging purposes only, prints list of values with only previously-queried values visible, do not use in final submission
        String s = "[";
        for (int i = 0; i < this.list.length-1; i++){
            if (this.queried.contains(i)){
                s += this.list[i] + ",";
            }
            else{
                s += "??,";
            }
        }
        if (this.queried.contains(this.list.length-1)){
            s += this.list[this.list.length-1];
        }
        else{
            s += "??";
        }
        s += "]";
        return s;
    }


    public double[] slice(int start, int end){
        // for debugging purposes only, returns a slice of the list of values, do not use in final submission
        double[] s = new double[end-start];
        for (int i = 0; i < s.length; i++){
            s[i] = this.list[start + i];
        }
        return s;
    }

    protected int lessthan(double val){
        // for solution checking only, returns the number of values less than val, do not use in final submission
        this.queriesLeft = 0;
        int count = 0;
        for (double item : this.list){
            if (item < val){count += 1;}
        }
        return count;
    }

    protected int greaterthan(double val){
        // for solution checking only, returns the number of values greater than val, do not use in final submission
        this.queriesLeft = 0;
        int count = 0;
        for (double item : this.list){
            if (item > val){count += 1;}
        }
        return count;
    }

    public double request(int i){
        // returns the value at index i of the list of values. This should be the only method you use.
        if (this.queriesLeft <= 0){
            System.out.println("out of queries");
            return -1;
        }
        this.queriesLeft -= 1;
        this.queried.add(i);
        return this.list[i];
    }

    private static void check_median(Company c1, Company c2, double answer){
        // for solution checking only, determines whether or not answer is the median value for companies c1 and c2, do not use in final submission
        int less = c1.lessthan(answer) + c2.lessthan(answer);
        int greater = c1.greaterthan(answer) + c2.greaterthan(answer);
        if (less == greater){ System.out.println("median found!");}
        else{System.out.println("response not the median");}
    }


    public static void main(String[] args){
        int size = 1001;
        Company c1 = new Company(size);
        Company c2 = new Company(size);
        double answer = MedianFinder.findMedian(c1, c2);
        check_median(c1, c2, answer);
    }
    

}

