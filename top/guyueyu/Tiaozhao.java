package top.guyueyu;

import java.util.*;

public class Tiaozhao {
	private int x,y;				//当前跳蚤的坐标
	private int m,n;				//m行n列
	private int[][] times;			//跳蚤在每一块瓷砖上的次数
	
	public Tiaozhao(int m,int n) {
		this.m = m;this.n = n;
		x = 0; y = 0;
		times = new int[m][n];
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				times[i][j] = 0;
			}
		}
		init();
	}
	
	/*
	 * 初始化
	 */
	private void init(){
		Random random = new Random();
		x = (int) (Math.abs(random.nextInt())%m);
		y = (int) (Math.abs(random.nextInt())%n);
		times[x][y] = 1;
	}
	
	/*
	 * 移动
	 */
	public void start(){		
		while(hasSpace()){
			move();
		}
	}
	
	/*
	 * 动一次
	 */
	private void move(){
		Random random = new Random();
		int faceTo = Math.abs(random.nextInt(4)+1);
		boolean flag = true;
		while(flag){
			if((x==0&&faceTo==3)||(y==0&&faceTo==1)||(y==m-1&&faceTo==2)||(x==n-1&&faceTo==4)){
				faceTo = Math.abs(random.nextInt(4)+1);
			}else {
				flag = false;
			}
		}
		switch (faceTo) {
		case 1:
			y-=1;
			break;
		case 2:
			y+=1;
			break;
		case 3:
			x-=1;
			break;
		case 4:
			x+=1;
			break;
		default:
			break;
		}
		times[x][y]+=1;
	}
	/*
	 * 求总步数
	 */
	public int total(){
		int sum = 0;
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				sum+=times[i][j];
			}
		}
		return sum;
	}
	
	/*
	 * 判断是否还有没有跳到的
	 */
	private boolean hasSpace(){
		for(int i=0; i<m;i++){
			for(int j=0;j<n;j++){
				if(times[i][j]==0){
					return true;
				}
			}
		}
		return false;
	}
	
	/*
	 * 输出
	 */
	public void  printTimes() {
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++){
				System.out.print(times[i][j]+" ");
			}
			System.out.println();
		}
	}
}
