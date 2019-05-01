package top.guyueyu.datastructs;

import java.util.Scanner;

public class Graph {
	/*
	 * 图的邻接表表示
	 */
	private Vertex[] head;
	private int vertexNum;//顶点的个数
	private int edgeNum;//边数
	private boolean hasDirect;//有向图？无向图？
	public Graph() {}
	public Graph(int v, int e){
		this.vertexNum = v;
		this.edgeNum = e;
		head = new Vertex[v+1];
		hasDirect = true;
	}
	
	public int getVertexNum() {
		return vertexNum;
	}
	public void setVertexNum(int vertexNum) {
		this.vertexNum = vertexNum;
	}
	public int getEdgeNum() {
		return edgeNum;
	}
	public void setEdgeNum(int edgeNum) {
		this.edgeNum = edgeNum;
	}
	public void init(){
		Scanner scanner = new Scanner(System.in);
		EdgeElement [] edgeElements = new EdgeElement[edgeNum];
		for(int i=0;i<edgeNum;i++){
			int from = scanner.nextInt();
			int to = scanner.nextInt();
			double weight = scanner.nextDouble();
			EdgeElement edgeElement = new EdgeElement(from, to, weight);
			edgeElements[i] = edgeElement;
		}
		init(edgeElements);
	}
	public void init(EdgeElement[] edges){
		//从边数组中读取图，生成邻接表
		for(int i=0; i<=vertexNum; i++){
			head[i] = new Vertex();
			head[i].vertexName = i;
			head[i].adjacent = null;
		}
		for(int i=0; i<edges.length; i++){
			if(edges[i]==null)
				break;
			int v1 = edges[i].fromvertex;
			int v2 = edges[i].tovertex;
			double weight = edges[i].weight;
			if(v1<0 || v2<0 || v1==v2){
				System.out.println("边顶点序号无效");
				System.exit(0);
			}
			Edge edge = new Edge(v2, null, weight);
			Edge q = head[v1].adjacent;
			if(q==null){
				head[v1].adjacent = edge;
			}else {
				while(q.link!=null){
					q = q.link;
				}
				q.link = edge;
			}
			if(hasDirect == false){//如果是无向图，需要在处理
				Edge edge2 = new Edge(v1, null, weight);
				Edge n = head[v2].adjacent;
				if (n==null) {
					head[v2].adjacent = edge2;
				}else{
					while(n.link!=null){
						n = n.link;
					}
					n.link = edge2;
				}
			}
		}
	}
	public boolean findEdge(int i, int j){
		if(i<0 || j<0 || i==j){
			System.out.println("边顶点序号无效");
			System.exit(0);
		}
		Edge p = head[i].adjacent;
		while(p!=null){
			if(p.verAdj==j){
				return true;
			}
			p = p.link;
		}
		return false;
	}
	public void putEdge(int i, int j){
		//i,j必须已经存在
		if(i<0 || j<0 || i==j){
			System.out.println("边顶点序号无效");
			System.exit(0);
		}
		Edge p = head[i].adjacent;
		while(p!=null){
			if(p.verAdj == j){
				break;
			}
			p = p.link;
		}
		if(p==null){//如果邻接表里没有这条边
			edgeNum++;
			//无权图
			head[i].adjacent = new Edge(j, head[i].adjacent);
		}
		
	}
	public void removeEdge(int i, int j){
		if(i<0 || j<0 || i==j){
			System.out.println("边顶点序号无效");
			System.exit(0);
		}
		Edge p = head[i].adjacent;
		Edge q = null;
		while(p!=null){
			if(p.verAdj==j){
				break;
			}
			q = p;
			p = p.link;
		}
		if(p==null){
			System.out.println("边不存在");
			System.exit(0);
		}
		if(q==null){//该节点是在表头
			head[i].adjacent = head[i].adjacent.link;
		}else{
			q.link = p.link;
		}
	}
	public int degree(int i){
		return inDegree(i)+outDegree(i);
	}
	public int inDegree(int i){
		int k = 0;
		if(i<0){
			System.out.println("顶点序号无效");
			System.exit(0);
		}
		for(int j=0;j<vertexNum;j++){
			Edge p = head[j].adjacent;
			while(p!=null){
				if(p.verAdj==i){
					k++;
				}
				p = p.link;
			}
		}
		return k;
	}
	public int outDegree(int i){
		int k = 0;
		Edge p = head[i].adjacent;
		while (p!=null) {
			k++;
			p = p.link;
		}
		return k;
	}
	public double[][] getMatrix(){
		double[][] matrix = new double[vertexNum][vertexNum]; 
		for(int i=0; i<vertexNum; i++){
			Edge p = head[i].adjacent;
			while(p!=null){
				matrix[i][p.verAdj-1] = p.cost;
				p = p.link;
			}
		}
		return matrix;
	}
	public void output(){
		double[][] n = getMatrix();
		for(int i=0;i<vertexNum;i++){
			for(int j=0;j<vertexNum;j++){
				System.out.print(n[i][j]+"\t");
			}
			System.out.println();
		}
	}
	public void DFS(int v){
		boolean visited[] = new boolean[vertexNum+1];
		for(int i=0; i<vertexNum; i++){
			visited[i] = false;
		}
		dfs(v, visited);
		System.out.println();
	}
	private void dfs(int i, boolean[] visited){
		System.out.print(i+" ");
		visited[i] = true;
		int v=getFirstEdge(i);
		while(v != -1){
			if(visited[v]==false){
				dfs(v, visited);
			}
			v = getNextNeighbor(i, v);
		}
	}
	private int getFirstEdge(int i){
		/*
		 * 获得顶点i的第一个邻接顶点的序号
		 */
		if(i<0){
			return -1;
		}
		int v;
		if (head[i].adjacent!=null) {
			v = head[i].adjacent.verAdj;
		}else{
			v = -1;
		}
		return v;
	}
	private int getNextNeighbor(int i,int j){
		/*
		 * 获得顶点i的邻接顶点序号为j的下一个顶点的序号
		 */
		if(i<0 || j<0){
			return -1;
		}
		Edge p = head[i].adjacent;
		while(p.verAdj!=j && p!=null){
			p = p.link;
		}
		if(p==null)
			return -1;
		p = p.link;
		if(p==null)
			return -1;
		return p.verAdj;
	}
	public void BFS(int v){
		
	}
	class Edge{
		//邻接表边类
		private int verAdj;//邻接顶点序号
		private double cost;//边的权值
		private Edge link; //下一个边节点
		public Edge(int adj, Edge e) {
			//无权图
			this.verAdj = adj;
			this.link = e;
			this.cost = 1;
		}
		public Edge(int adj, Edge e, double c){
			this.verAdj = adj;
			this.link = e;
			this.cost = c;
		}
	}
	class Vertex{
		//邻接表顶点类
		private int vertexName;//顶点序号
		private Edge adjacent;//边链表的头指针
	}
	class EdgeElement{
		//边类
		private int fromvertex;
		private int tovertex;
		private double weight;
		public EdgeElement(int v1, int v2) {
			//无权图
			fromvertex = v1;
			tovertex = v2;
			weight = 1;
		}
		public EdgeElement(int v1, int v2, double w) {
			//有权图
			fromvertex = v1;
			tovertex = v2;
			weight = w;
		}
	}
}
