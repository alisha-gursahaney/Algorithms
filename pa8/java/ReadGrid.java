import java.util.*;
import java.io.*;


public class ReadGrid{

    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int r = s.nextInt();
        int c = s.nextInt();
        int[][] grid = new int[r][c];
        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                grid[i][j] = s.nextInt();
	    }
	}
	Drainage.max_run(grid);
	
    }

}
