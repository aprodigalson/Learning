package top.guyueyu.datastructs;

import java.util.Iterator;

import org.w3c.dom.html.HTMLHeadElement;

public class List<E> implements Iterable<E> {
	/*
	 * 链表实现
	 * 
	 */
	private Node<E> head = null;
	private Node<E> tail = null;
	public void makeEmpty(){
		head = tail = null;
	}
	public void add(E item){
		Node<E> newNode = new Node<E>(item);
		if(head==null){
			head = newNode;
			tail = newNode;
			return;
		}
		tail.next = newNode;
		tail = newNode;
		return;
	}
	public boolean contains(E e){
		if(head==null){
			return false;
		}
		Node<E> tmp = head;
		while(tmp!=null){
			if(tmp.data==e){
				return true;
			}
			tmp = tmp.next;
		}
		return false;
	}
	public E getIndex(int index){
		/*
		 * 返回第index个节点元素
		 * 从1开始到length()
		 */
		if(index<1 || index>length()){
			return null;
		}
		int i=1;
		Node<E> preNode;
		Node<E> curNode = head;
		while (curNode!=null) {
			if(i==index){
				return curNode.data;
			}
			preNode = curNode;
			curNode = curNode.next;
			i++;
		}
		return null;
	}
	public Node<E> remove(E e){
		/*
		 * 删除值e
		 */
		if(head==null){
			return null;
		}
		if(head.data==e){
			Node<E> removeNode = head;
			head = head.next;
			return removeNode;
		}
		Node<E> preNode = head;
		Node<E> currNode = head.next;
		while(currNode!=null){
			if(currNode.data==e){
				if(currNode == tail){
					tail = preNode;
				}
				preNode.next = currNode.next;
				return currNode;
			}
			preNode = currNode;
			currNode = currNode.next;
		}
		return null;
	}
	public Node<E> remove(int index){
	/*
	 * 移除第index个元素
	 */
		if(index<1 || index>length()){
			return null;
		}
		Node<E> removeNode = null;
		if(index==1){//删除头时，头特殊处理
			removeNode = head;
			head=head.next;
			if(length()==1){
				tail = null;
			}
			return removeNode;
		}
		if (index==length()) {//删除尾时，尾特殊处理
			removeNode = tail;
			tail = preNode(tail);
			if(length()==1){
				head = null;
				return removeNode;
			}
			tail.next = null;
			return removeNode;
		}
		int i = 2;
		Node<E> preNode = head;
		Node<E> curNode = head.next;
		while (curNode!=null) {
			if(i==index){
				preNode.next = curNode.next;
				return curNode;
			}
			preNode = curNode;
			curNode = curNode.next;
			i++;
		}
		return null;
	}
	private Node<E> preNode(Node<E> node){
		if(node == head){
			return null;
		}
		Node<E>tmp = head;
		while(tmp.next!=null){
			if(tmp.next==node){
				return tmp;
			}
			tmp = tmp.next;
		}
		return null;
	}
	public int length(){
		Node<E> tmp = head;
		int length = 0;
		while(tmp!=null){
			tmp = tmp.next;
			length++;
		}
		return length;
	}
	public boolean isEmpty(){
		if(head==null){
			return true;
		}
		return false;
	}
	public void printList(){
		Node<E> tmp = head;
		while(tmp!=null){
			System.out.print(tmp.data+" ");
			tmp = tmp.next;
		}
		System.out.println();
	}
	
	public Node<E> getHead() {
		return head;
	}

	public void setHead(Node<E> head) {
		this.head = head;
	}

	public Node<E> getTail() {
		return tail;
	}

	public void setTail(Node<E> tail) {
		this.tail = tail;
	}

	class Node<E>{
		E data;
		Node<E> next=null;
		public Node(E item){
			this.data = item;
		}
	}

	@Override
	public Iterator<E> iterator() {
		return new Iterator<E>() {
			private int index = 1;
			@Override
			public boolean hasNext() {
				return index<=length();
			}
			@Override
			public E next(){
				return getIndex(index++);
			}
		};
	}


}
