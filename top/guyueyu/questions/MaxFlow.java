package top.guyueyu.questions;

import java.util.PriorityQueue;
import java.util.Scanner;

public class MaxFlow {
	private static int[][] capacity;
	private static int[] flow;
	private static int[] pre;
	private static int m,n;
	private static int maxData = 0x7fffffff;
	//private static Queue<Integer> queue = new Queue<>();
	//�Լ�д�Ķ���������
	private static java.util.Queue<Integer> queue = new PriorityQueue<>();
	public int BFS(int src,int des){//ͨ����ȱ�����ò��������ϵ�һ������·������������·���ϵ���Сֵ�����޸�ǰ�����顣
		show();
		for(int i=1; i<m+1; i++){
			pre[i] = -1;
		}
		//queue.makeEmpty();
		queue.clear();
		pre[src] = 0;
		flow[src] = maxData;
		//queue.push(src);
		queue.add(src);
		while(!queue.isEmpty()){
			//int index = queue.pop();
			int index = queue.remove();
			if(index==des){//�ҵ�����·��
				break;
			}
			for(int i=1; i<m+1; i++){
				if(i!=src && capacity[index][i]>0 && pre[i]==-1){
					pre[i] = index;
					flow[i] = Math.min(capacity[index][i], flow[index]);
					//queue.push(i);
					queue.add(i);
				}
			}
		}
		if(pre[des]==-1){
			return -1;
		}else {
			return flow[des];
		}
	}
	public int maxFlow(int src,int des){
		int increasement = 0;
		int sumflow = 0;
		while((increasement = BFS(src,des))!=-1){//�ҵ��������������·���ϵ���Сֵ
			int k = des;
			while(k!=src){//��������·���ϵĲ�������
				int last = pre[k];//����ǰ��Ѱ��·��
				capacity[last][k] -= increasement;
				capacity[k][last] += increasement;
				k = last;
			}
			sumflow += increasement;
		}
		return sumflow;
	}
	public void init(){
		Scanner in = new Scanner(System.in);
		m = in.nextInt();//����
		n = in.nextInt();//��
		pre = new int[m+1];
		capacity = new int[m+1][m+1];
		flow = new int[m+1];
		for(int i=0; i<m+1; i++){
			flow[i] = 0;
			for(int j=0; j<m+1; j++){
				capacity[i][j] = 0;
			}
		}
		for(int i=0; i<n; i++){
			int start = in.nextInt();
			int end = in.nextInt();
			int ci = in.nextInt();
			capacity[start][end] += ci;
		}
		System.out.println(maxFlow(1, m));
	}
	private void show(){
		System.out.println("Capacity:");
		for(int i=0;i<m+1;i++){
			for(int j=0;j<m+1;j++){
				System.out.print(" "+capacity[i][j]);
			}
			System.out.println();
		}
		System.out.println("flow:");
		for(int i=0;i<m+1;i++){
			System.out.print(" "+flow[i]);
		}
		System.out.println();
		System.out.println("pre");
		for(int i=0;i<m+1;i++){
			System.out.print(" "+pre[i]);
		}
		System.out.println();
		System.out.println("queue");
		//queue.printQueue();
		
	}
	
	/*
	 * 4 5
1 2 100
1 3 100
1 4 100
2 4 1
3 4 1
	 */
}
