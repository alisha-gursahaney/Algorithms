import java.io.*;
import java.util.*;

public class GreedySolver{

    private String problem;
    private ArrayList<Pair> inputlist;

    public GreedySolver(String problem, ArrayList<Pair> inputlist){
        this.problem = problem;
        this.inputlist = inputlist;
    }

    public double cost_bakeoff(ArrayList<Pair> schedule){
        double elapsed = 0;
	double earliest_finish = 0;
	for (Pair component : schedule){
            double active = component.first;
	    double passive = component.second;
	    elapsed += active;
	    earliest_finish = Math.max(earliest_finish, elapsed+passive);
	}
	return earliest_finish;
    }

    public double cost_deadlines(ArrayList<Pair> schedule){
        double elapsed = 0;
	double maximum_lateness = 0;
	for (Pair task : schedule){
            double time_taken = task.first;
	    double deadline = task.second;
	    elapsed += time_taken;
	    double lateness = Math.max(elapsed - deadline, 0);
	    maximum_lateness = Math.max(maximum_lateness, lateness);
	}
	return maximum_lateness;
    }

    public double cost_mileage(ArrayList<Pair> schedule){
        double fuel_cost = 2;
	double spent = 0;
	for (Pair car : schedule){
            double mpg = car.first;
	    double miles = car.second;
	    spent += (miles/mpg)*fuel_cost;
	    fuel_cost *= 1.05;
	}
	return spent;
    }

    public double cost(ArrayList<Pair> schedule){
        if (this.problem.equals("bakeoff")){
            return this.cost_bakeoff(schedule);
	}
	else if (this.problem.equals("deadlines")){
            return this.cost_deadlines(schedule);
	}
	else{
            return this.cost_mileage(schedule);
	}
    }

    public int choose(){
        if (this.problem.equals("bakeoff")){
            return GreedyChooser.bakeoff(this.inputlist);
        }
        else if (this.problem.equals("deadlines")){
            return GreedyChooser.deadlines(this.inputlist);
        }
        else{
            return GreedyChooser.mileage(this.inputlist);
        }
    }

    public ArrayList<Pair> solve(){
        ArrayList<Pair> schedule = new ArrayList<Pair>();
	int input_size = this.inputlist.size();
	for (int i = 0; i < input_size; i++){
	    int next = this.choose();
            schedule.add(this.inputlist.get(next));
	    this.inputlist.remove(next);
	}
	return schedule;
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
	String problem = s.next();
	int length = s.nextInt();
	ArrayList<Pair> input = new ArrayList<Pair>();
	for (int i = 0; i < length; i++){
	    double first = Double.parseDouble(s.next());
	    double second = Double.parseDouble(s.next());
	    Pair p = new Pair(first, second);
	    input.add(p);
	}
        GreedySolver greedy = new GreedySolver(problem, input);
	ArrayList<Pair> schedule = greedy.solve();
        String print = "[";
        for (Pair p : schedule){
            print += p + ",";
        }
        print += "]";
        System.out.println(print);
        System.out.println(greedy.cost(schedule));
    }

}

class Pair {
    public double first;
    public double second;
    public Pair(double a1, double a2) {
        first = a1;
        second = a2;
    }

    public String toString(){
        return "(" + this.first + "," + this.second + ")";
    }
}
