import java.util.*;
import java.io.*;

public class InputReader{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
	s.next();
	int blendcount = s.nextInt();
	ArrayList<Integer> blendtimes = new ArrayList<>();
	String value = s.next();
	while(!value.contains("n") && !value.contains("c")){
	    blendtimes.add(Integer.parseInt(value));
	    value = s.next();
	}
	int cookcount = s.nextInt();
        ArrayList<Integer> cooktimes = new ArrayList<>();
        value = s.next();
        while(!value.contains("n") && !value.contains("c")){
            cooktimes.add(Integer.parseInt(value));
            value = s.next();
        }
	int straincount = s.nextInt();
        ArrayList<Integer> straintimes = new ArrayList<>();
        value = s.next();
        while(!value.contains("n") && !value.contains("c")){
            straintimes.add(Integer.parseInt(value));
            value = s.next();
        }
	int finishcount = s.nextInt();
        ArrayList<Integer> finishtimes = new ArrayList<>();
        value = s.next();
        while(!value.contains("n") && !value.contains("o")){
            finishtimes.add(Integer.parseInt(value));
            value = s.next();
        }

        ArrayList<Integer> stationcounts = new ArrayList<>();
	stationcounts.add(blendcount);
	stationcounts.add(cookcount);
	stationcounts.add(straincount);
	stationcounts.add(finishcount);
	ArrayList<ArrayList<Integer>> stationtimes = new ArrayList<>();
	stationtimes.add(blendtimes);
        stationtimes.add(cooktimes);
	stationtimes.add(straintimes);
	stationtimes.add(finishtimes);

	int employeecount = s.nextInt();
	ArrayList<ArrayList<String>> employee_training = new ArrayList<>();
	ArrayList<ArrayList<Integer>> employee_times = new ArrayList<>();
	value = s.next();
	for(int i = 0; i < employeecount; i++){
	    ArrayList<String> training = new ArrayList<>();
	    ArrayList<Integer> times = new ArrayList<>();
	    //value = s.next();
            while(value.contains("n") || value.contains("o")){
                training.add(value);
                value = s.next();
            }
            while(!value.contains("n") && !value.contains("o")){
                times.add(Integer.parseInt(value));
                value = s.next();
            }
	    employee_training.add(training);
	    employee_times.add(times);
	}
	System.out.println(Scheduler.schedule(stationcounts, stationtimes, employee_training, employee_times));
    }
}
