package top.guyueyu.datastructs;

public class Stack<E> {
	/*
	 * ջ
	 */
	private List<E> list = new List<E>();
	private int length=0;
	public boolean isEmpty(){
		return length==0;
	}
	public void push(E item){
		list.add(item);
		length++;
	}
	public E pop(){
		if(isEmpty()){
			return null;
		}
		E elemnet = list.getTail().data;
		list.remove(length);
		length--;
		return elemnet;
	} 
	public E top(){
		if(isEmpty()){
			return null;
		}
		return list.getTail().data;
	}
	public void printStack(){
		list.printList();
	}
}
