package top.guyueyu.questions;
/*
 * 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
 * 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 */

public class FindIntegerInTwoDimensionArray {
	public boolean Find(int target, int [][] array) {
		//每行进行一次二分查找
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
		//从右上角开始查找，也可以从左下角开始查找
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
