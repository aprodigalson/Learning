package top.guyueyu.algorithms.sort;

public class Sort<T extends Comparable<T>> {
	
	public  void insertsort(T[] a,int n){
		//直接插入排序
		for(int i=1; i<n; i++){
			int j=i-1;
			T t = a[i];
			for(; j>=0 && t.compareTo(a[j])<0; j--){
				a[j+1] = a[j];
			}
			a[j+1] = t;
		}
	}
	public void selectsort(T[] a, int n){
		//简单选择排序
		for(int i=0; i<n; i++){
			int minIndex = i;
			for(int j=i+1; j<n; j++){
				if(a[j].compareTo(a[minIndex])<0){
					minIndex = j;
				}
			}
			swap(a,i,minIndex);
		}
	}
	public void bubblesort(T[] a,int n){
		//冒泡排序
		for(int i=0; i<n-1; i++){
			for(int j=0; j<n-i-1; j++){
				if(a[j].compareTo(a[j+1])>0){
					swap(a, j, j+1);
				}
			}
		}
	}
	public void quicksort(T[] a,int n){
		//快速排序
		quicksortmain(a, 0, n-1);
	}


	private void quicksortmain(T[] a,int l, int h){
		if(l<h){
			int divideLoc = partition(a, l, h);
			quicksortmain(a, l, divideLoc-1);
			quicksortmain(a, divideLoc+1, h);
		}
	}
	private int partition(T[] a,int l,int h){
		//快排划分
		T key = a[l];
		int index = l+1;
		for(int i=index; i<=h && l<h; i++){
			if(a[i].compareTo(key)<0){
				swap(a, i, index);
				index++;
			}
		}
		swap(a, l, index-1);
		return index-1;
	}
	public void shellsort(T[] a,int n){
		//希尔排序
		int gap = 1;
		T temp;
		while(gap<n/3){//动态生成gap
			gap = gap*3+1;
		}
		while (gap>0) {
			for(int i=gap; i<n ; i++){//插入排序
				temp = a[i];
				int j;
				for(j=i-gap; j>=0 && a[j].compareTo(temp)>0;j-=gap){
					a[j+gap] = a[j];
				}
				a[j+gap] = temp;
			}
			gap/=2;
		}
	}
	public void mergesort(T[] a,int n){
		//归并排序
		mergesortMain(a, 0, n-1);
	}
	private void mergesortMain(T[] a,int left, int right){
		if(left==right){
			return;
		}
		int mid = (left+right)/2;
		mergesortMain(a, left, mid);
		mergesortMain(a, mid+1, right);
		merge(a,left,mid,right);
	}
	private void merge(T[] a,int left,int mid,int right){
		//归并排序的合并操作
		int len = right-left+1;
		T[] temp = (T[])new Comparable[len];
		int k = 0;
		int i = left;
		int j = mid+1;
		while(i<=mid && j<=right){
			temp[k++] = a[i].compareTo(a[j])<=0?a[i++]:a[j++];
		}
		while(i<=mid){
			temp[k++] = a[i++];
		}
		while(j<=right){
			temp[k++] = a[j++];
		}
		for(int s=0; s<len; s++){
			a[left++] = temp[s];
		}
	}
	public void heapsort(T[] a,int n){
		//堆排序
		buildMaxHeap(a,n);
		for(int i=n-1; i>0; i--){
			swap(a, 0, i);
			n--;
			heapify(a,0,n);
		}
	}
	private void buildMaxHeap(T[] a,int n){
		//建大顶堆
		for(int i=n/2;i>=0;i--){
			heapify(a, i, n);
		}
	}
	private void heapify(T[] a,int i,int length){
		//堆调整
		int left = 2*i+1;
		int right = 2*i+2;
		int largest = i;
		if(left<length && a[left].compareTo(a[largest])>0){
			largest = left;
		}
		if(right<length && a[right].compareTo(a[largest])>0){
			largest = right;
		}
		if(largest != i){
			swap(a, i, largest);
			heapify(a, largest, length);
		}
	}
	public void countingsort(int[] a, int n){
		//计数排序
		int min,max;
		int index = 0;
		min=max=a[0];
		for(int i=1; i<n; i++){
			min = (a[i]<min)?a[i]:min;
			max = (a[i]>max)?a[i]:max;
		}
		int k = max-min+1;
		int[] bucket = new int[k];
		for(int i=0; i<k; i++){
			bucket[i]=0;
		}
		for(int i=0; i<n; i++){
			bucket[a[i]-min]++;
		}
		for(int i=min; i<=max; i++){
			for(int j=0; j<bucket[i-min]; j++){
				a[index++] = i;
			}
		}
		
	}
	private void swap(T[] a, int i,int j){
		T tmp = a[i];
		a[i] = a[j];
		a[j] = tmp;
	}
}
