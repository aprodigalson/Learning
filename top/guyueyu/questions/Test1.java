package top.guyueyu.questions;

import java.util.Scanner;

/*
 * ���Զ����ֿ����������ϰ����������Ҫ���������ƹ���Щ�ϰ��ﵽ�յ��ȡ��������������˴�����˶����յ���ʱ��̵�·���� ��֪������ֻ�����Ŷ���������ϱ������ƶ����ƶ����ٶ�Ϊ1m/s��������ÿת��90����Ҫ����1s��

 ���룺 
��һ�У����λ�����꼰�����˳����磺 
1 0 EAST
��������˳�ʼ����Ϊx=1,y=0���������泯���� 
�ڶ��У��յ�λ�����꼰�����˳����磺 
0 2 WEST
�����������Ҫ�ƶ�����x=0,y=2�����泯���� 
������������ǵ�ͼ�� 
��������������r,c�������е�ͼ�����ж�����������У��磺
2 3
0 1 0
0 0 0 
���У����Ͻ�Ϊ����ԭ�㣬��������Ϊx������ķ����Ƕ��������ϵ���Ϊy������ķ������Ϸ���
��ͼ��1�������ϰ�������˲���ǰ����0�������ϰ�������˿���ǰ�� ��ͼ�����ڵ�ÿ������֮��ľ���Ϊ1m��
0 <= l,w <= 128 
����� 
�����˴�����ƶ����յ�����Ҫ����������������ɴ�ʱ���65535
 */


/*
 * �������汾: Java 1.8.0_66
��ʹ�ñ�׼�������(System.in, System.out)���ѽ���ͼ�Ρ��ļ������硢ϵͳ��صĲ�������java.lang.Process , javax.swing.JFrame , Runtime.getRuntime����Ҫ�Զ�������ƣ�����ᱨ������Ҫ���package answer֮�����䣻������д�ܶ���࣬���Ǳ�����һ������ΪMain������Ϊpublic���ԣ�����MainΪΨһ��public class��Main�������������һ������Ϊ'main'�ľ�̬����������������������ǳ�������
ʱ������: 3S (C/C++���������Ϊ: 5 S)   �ڴ�����: 128M (C/C++���������Ϊ: 640 M)
����:
��һ�У����λ�����꼰�����˳����磺 
1 0 EAST
��������˳�ʼ����Ϊx=1,y=0���������泯���� 
�ڶ��У��յ�λ�����꼰�����˳����磺 
0 2 WEST
�����������Ҫ�ƶ�����x=0,y=2�����泯���� 
������������ǵ�ͼ�� 
��������������r,c�������е�ͼ�����ж�����������У��磺
2 3
0 1 0
0 0 0 
���У����Ͻ�Ϊ����ԭ�㣬��������Ϊx������ķ����Ƕ��������ϵ���Ϊy������ķ������Ϸ���
��ͼ��1�������ϰ�������˲���ǰ����0�������ϰ�������˿���ǰ�� ��ͼ�����ڵ�ÿ������֮��ľ���Ϊ1m��
0 <= l,w <= 128
���:
��һ�У����λ�����꼰�����˳����磺 
1 0 EAST
��������˳�ʼ����Ϊx=1,y=0���������泯���� 
�ڶ��У��յ�λ�����꼰�����˳����磺 
0 2 WEST
�����������Ҫ�ƶ�����x=0,y=2�����泯���� 
������������ǵ�ͼ�� 
��������������r,c�������е�ͼ�����ж�����������У��磺
2 3
0 1 0
0 0 0 
���У����Ͻ�Ϊ����ԭ�㣬��������Ϊx������ķ����Ƕ��������ϵ���Ϊy������ķ������Ϸ���
��ͼ��1�������ϰ�������˲���ǰ����0�������ϰ�������˿���ǰ�� ��ͼ�����ڵ�ÿ������֮��ľ���Ϊ1m��
0 <= l,w <= 128
���뷶��:
0 0 NORTH
2 0 SOUTH
2 3
0 1 0
0 0 0
�������:
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
