import java.util.*;

public class FlowNetwork{
    public String source;
    public String sink;
    public HashMap<String, ArrayList<Edge>> network;
    public HashMap<String, ArrayList<Edge>> back;

    public FlowNetwork(String source, String sink){
        this.source = source;
	this.sink = sink;
	this.network = new HashMap<>();
	this.back = new HashMap<>();
	this.addNode(source);
	this.addNode(sink);
    }

    public String toString(){
        String s = "";
	for (String node : this.network.keySet()){
            for (Edge e : this.network.get(node)){
                s += e + "\n";
	    }
	}
	return s;
    }

    public void addNode(String node){
        if(!network.containsKey(node)){
            network.put(node, new ArrayList<>());
	    back.put(node, new ArrayList<>());
	}
    }

    public void addEdge(String start, String dest, int capacity){
        this.addNode(start);
	this.addNode(dest);
	Edge e = new Edge(start, dest, capacity);
	this.network.get(start).add(e);
	this.back.get(dest).add(e);
    }

    public boolean addFlow(String start, String dest, int amount){
        boolean added = false;
        for(Edge e : this.network.get(start)){
            if (e.dest == dest && e.flow+amount <= e.capacity){
                e.flow += amount;
		added = true;
		break;
	    }
	}
	if(!added){
            for(Edge e : this.back.get(start)){
                if(e.source == dest && e.flow >= amount){
                    e.flow -= amount;
		    added = true;
		    break;
		}
	    }
	}
	return added;
    }

    public static void main(String[] args){
        FlowNetwork graph = new FlowNetwork("s","t");
	graph.addEdge("s","a",20);
	graph.addEdge("s","b",10);
	graph.addEdge("a","b",30);
	graph.addEdge("a","t",10);
	graph.addEdge("b","t",23);
	graph.addEdge("s","x",5);
	graph.addEdge("x","a",5);
	System.out.println(graph);
	int f = graph.maxflow();
	System.out.println(graph);
	System.out.println(f);

    }

    public ArrayList<String> residualNeighbors(String node){
        ArrayList<String> n = new ArrayList<>();
	for(Edge e : this.network.get(node)){
            if(e.flow < e.capacity){
                n.add(e.dest);
	    }
	}
	for(Edge e : this.back.get(node)){
            if(e.flow > 0){
                n.add(e.source);
	    }
	}
	return n;
    }

    public ArrayList<String> augmentingPath(){
        HashMap<String, String> parents = new HashMap<>();
	parents.put(this.source, "");
	ArrayList<String> toVisit = new ArrayList<>();
	toVisit.add(this.source);
	boolean sink_found = false;
	while(toVisit.size() > 0 && !sink_found){
            String current = toVisit.get(0);
	    toVisit.remove(0);
	    for(String neighbor : this.residualNeighbors(current)){
                if(neighbor.equals(this.sink)){
                    sink_found = true;
		}
		if(!parents.containsKey(neighbor)){
                    parents.put(neighbor, current);
		    toVisit.add(neighbor);
		}
	    }
	}
	if(!sink_found){
            return new ArrayList<>();
	}
	ArrayList<String> path = new ArrayList<>();
	path.add(this.sink);
	while(!path.get(0).equals(this.source)){
            String current = path.get(0);
	    String previous = parents.get(current);
	    path.add(0,previous);
	}
	return path;
    }

    public int pathBottleneck(ArrayList<String> path){
	if(path.size()< 2){
            return 0;
	}
	int bottleneck = Integer.MAX_VALUE;
	String current = path.get(0);
	String next = path.get(1);
	for (int i = 0; i < path.size()-1; i++){
            current = path.get(i);
	    next = path.get(i+1);
	    boolean forward = false;
	    for(Edge e : this.network.get(current)){
                if (e.dest.equals(next)){
                    forward = true;
		    if(bottleneck > e.capacity-e.flow){
                        bottleneck = e.capacity-e.flow;
		    }
		}
	    }
	    if(!forward){
                for(Edge e : this.network.get(next)){
                    if(e.dest.equals(current)){
                        if(bottleneck > e.flow){
                            bottleneck = e.flow;
			}
		    }
		}
	    }
	}
	return bottleneck;
    }

    public void pushFlow(ArrayList<String> path, int amount){
	if(path.size() < 2){
            return;
	}
        for(int i = 0; i < path.size()-1; i++){
            String current = path.get(i);
	    String next = path.get(i+1);
	    addFlow(current, next, amount);
	}
    }

    public int maxflow(){
        ArrayList<String> path = augmentingPath();
	while(path.size()>0){
            int amount = pathBottleneck(path);
            pushFlow(path, amount);
	    path = augmentingPath();
	}
	int outflow = 0;
	for(Edge e : this.network.get(this.source)){
            outflow += e.flow;
	}
	for(Edge e : this.back.get(this.source)){
            outflow -= e.flow;
	}
	return outflow;
    }
}

class Edge{
    public String source;
    public String dest;
    public int capacity;
    public int flow;

    public Edge(String source, String dest, int capacity, int flow){
        this.source = source;
	this.dest = dest;
	this.capacity = capacity;
	this.flow = flow;
    }

    public Edge(String source, String dest, int capacity){
        this.source = source;
	this.dest = dest;
	this.capacity = capacity;
	this.flow = 0;
    }

    public String toString(){
        return this.source+"->"+this.dest+":"+this.flow+"/"+this.capacity;
    }
}
