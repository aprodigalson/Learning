package top.guyueyu;

import java.util.Scanner;

public class Maxmin {
	public static void main(String[] args) {
		System.out.println("������double�������У�����5λ��");
		int number =5;
		double a[] = new double[number];// ����Ķ���
		Scanner z = new Scanner(System.in);
		for (int i = 0; i < number; i++)// ѭ����������
		{
			a[i] = z.nextDouble();
		}
		double result = 0;
		System.out.println("��Ҫ�������е����ֵ������1����Сֵ����2��ƽ��������3,������������4");
		
		while(true){
			int j=z.nextInt();
			switch (j) {
			case 1:
				result = max(a);
			break;
			case 2:
				result = min(a);
				break;
			case 3:
				result = average(a);
				break;
			case 4:System.exit(0);}
			System.out.println("���Ϊ��" + result);
			prints(a);
		}
		
	}
	private static void prints(double[] array){
		for(int i=0;i<array.length;i++){
			System.out.print(array[i]+" ");
		}
	}
	public static double max(double[] array) {
		double max = array[0];
		for(int i=1; i<array.length; i++){
			if(array[i]>max){
				max = array[i];
			}
		}
		return max;
	}

	public static double min(double[] array) {
		double min = array[0];
		for(int i=1; i<array.length; i++){
			if(array[i]<min){
				min = array[i];
			}
		}
		return min;
	}

	public static double average(double[] array) {
		double y = 0;
		for (int i = 0; i < array.length; i++) {
			y = y + array[i];
		}
		return y=y/5;
	}
}