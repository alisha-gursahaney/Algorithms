import java.util.*;
import java.io.*;

public class Box{
    
    public double length;
    public double width;
    public double height;

    public Box(double l,double w,double h){
        this.length = l;
	this.width = w;
	this.height = h;
    }

    public String toString(){
        String s = "";
        s += this.length;
	s += " x ";
	s += this.width;
	s += " x ";
	s += this.height;
	return s;
    }

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
	Box[] boxes = new Box[n];
	for (int i = 0; i < n; i++){
            double l = Double.parseDouble(s.next());
	    double w = Double.parseDouble(s.next());
	    double h = Double.parseDouble(s.next());
	    Box b = new Box(l,w,h);
	    boxes[i] = b;
	}
	int depth = NestBoxes.max_depth(boxes);
	System.out.println(depth);
    }

}
