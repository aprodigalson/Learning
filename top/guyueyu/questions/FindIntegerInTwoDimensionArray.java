package top.guyueyu.questions;
/*
 * ��һ����ά�����У�ÿһ�ж����մ����ҵ�����˳������ÿһ�ж����մ��ϵ��µ�����˳������
 * �����һ������������������һ����ά�����һ���������ж��������Ƿ��и�������
 */

public class FindIntegerInTwoDimensionArray {
	public boolean Find(int target, int [][] array) {
		//ÿ�н���һ�ζ��ֲ���
		for(int i=0;i<array.length;i++){
			int low = 0;
			int high = array[i].length-1;
			while (low<high) {
				int mid = (low+high)/2;
				if(array[i][mid]==target){
					return true;
				}
				if(array[i][mid]>target){
					high = mid-1;
				}
				if(array[i][mid]<target){
					low = mid+1;
				}
			}
		}
		return false;
	}
	public boolean Find1(int target,int[][]array){
		//�����Ͻǿ�ʼ���ң�Ҳ���Դ����½ǿ�ʼ����
		int row = array.length;
		int col = array[0].length;
		int i,j;
		for(i=0,j=col-1; j>0 && i<row;){
			if(target>array[i][j]){
				i++;
				continue;
			}
			if(target<array[i][j]){
				j--;
			}
			if(target==array[i][j]){
				return true;
			}
		}
		return false;
	}
}
