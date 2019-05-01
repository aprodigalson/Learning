package top.guyueyu.questions;

import java.util.Scanner;

/*
 * 在自动化仓库中有若干障碍物，机器人需要从起点出发绕过这些障碍物到终点搬取货柜，现试求机器人从起点运动到终点用时最短的路径。 已知机器人只能沿着东西方向或南北方向移动，移动的速度为1m/s，机器人每转向90度需要花费1s。

 输入： 
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128 
输出： 
机器人从起点移动到终点所需要的最短秒数，当不可达时输出65535
 */


/*
 * 编译器版本: Java 1.8.0_66
请使用标准输入输出(System.in, System.out)；已禁用图形、文件、网络、系统相关的操作，如java.lang.Process , javax.swing.JFrame , Runtime.getRuntime；不要自定义包名称，否则会报错，即不要添加package answer之类的语句；您可以写很多个类，但是必须有一个类名为Main，并且为public属性，并且Main为唯一的public class，Main类的里面必须包含一个名字为'main'的静态方法（函数），这个方法是程序的入口
时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128
输出:
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128
输入范例:
0 0 NORTH
2 0 SOUTH
2 3
0 1 0
0 0 0
输出范例:
0 0 NORTH
1 1 SOUTH
2 2
0 1
0 0
 */
public class Test1 {
	private static int startX;
	private static int startY;
	private static String startFaceTo;
	private static int endX;
	private static int endY;
	private static String endFaceTo;
	private static int[][]map;
	private static int row;
	private static int col;
	
	private static int x;
	private static int y;
	private static int faceTo = faceTo(startFaceTo);
	private static int length = 0;
	public static void main(String[]args) {
		read();
		
	}
	private static void read(){
		Scanner scanner = new Scanner(System.in);
		String line1 = scanner.nextLine();
		String[] line1split = line1.split(" ");
		startX = Integer.parseInt(line1split[0]);
		startY = Integer.parseInt(line1split[1]);
		startFaceTo = line1split[2];
		String line2 = scanner.nextLine();
		String[] line2split = line2.split(" ");
		endX = Integer.parseInt(line2split[0]);
		endY = Integer.parseInt(line2split[1]);
		endFaceTo = line2split[2];
		row = scanner.nextInt();
		col = scanner.nextInt();
		for(int i=0; i<row; i++){
			for(int j=0; j<col;j++){
				map[i][j] = scanner.nextInt();
			}
		}
	}
	private static void solution(){
		
	}
	private static void move(int x,int y,int faceTo){
		
		length++;
	}
	private static int faceTo(String faceTo){
		switch (faceTo) {
		case "NORTH":
			return 1;
		case "EAST":
			return 2;
		case "SOUTH":
			return 3;
		case "WEST":
			return 4;
		default:
			return 0;
		}
	}
}
