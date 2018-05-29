package top.guyueyu.datastructs;

public class MinHeap<T extends Comparable<T>> {
	/*
	 * ×îĞ¡¶Ñ
	 */
	private List<T> minHeap;
	public MinHeap(){
		this.minHeap = new List<T>();
	}
	private void filterup(int start){
		int c = start;
		
	}
	public void insert(T data){
		int size = minHeap.length();
		minHeap.add(data);
		filterup(size);
	}
}
