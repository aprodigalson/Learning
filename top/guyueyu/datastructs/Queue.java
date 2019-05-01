package top.guyueyu.datastructs;

public class Queue<E> {
	/*
	 * ╤сап
	 */
	private List<E> list = new List<E>();
	private int length = 0;
	public E first(){
		return list.getIndex(1);
	}
	public void makeEmpty(){
		list.makeEmpty();
		length = 0;
	}
	public boolean isEmpty(){
		return length==0;
	}
	public void push(E item){
		list.add(item);
		length++;
	}
	public E pop(){
		if(length==0){
			return null;
		}
		length--;
		return list.remove(1).data;
	}
	public void printQueue(){
		list.printList();
	}
}
