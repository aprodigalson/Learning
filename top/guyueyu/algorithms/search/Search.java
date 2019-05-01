package top.guyueyu.algorithms.search;

public class Search<T extends Comparable<T>>{
	public int squenceSearch(T[] a,int n,T value){
		//˳�����
		int i;
		for(i=0; i<n; i++){
			if(a[i]==value){
				return i;
			}
		}
		return -1;
	}
	public int binarySearch(T[] a,int n,T value){
		//���ֲ���
		int low,high,mid;
		low = 0;
		high = n-1;
		while(low<=high){
			mid = (low+high)/2;
			if(a[mid]==value){
				return mid;
			}
			if(a[mid].compareTo(value)<0){
				low = mid+1;
			}
			if(a[mid].compareTo(value)>0){
				high = mid-1;
			}
		}
		return -1;
	}
	public int insertSearch(int[] a,int n,int value){
		//��ֵ����
		return insertSearch(a, value, 0, n-1);
	}
	private int insertSearch(int[] a,int value,int low,int high){
		int mid = low+(value-a[low])/(a[high]-a[low])*(high-low);
		if(a[mid]==value){
			return mid;
		}
		if(a[mid]>value){
			return insertSearch(a, value, low, mid-1);
		}
		if(a[mid]<value){
			return insertSearch(a, value, mid+1, high);
		}
		return -1;
	}
	
}
