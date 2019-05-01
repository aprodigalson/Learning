package top.guyueyu.datastructs;

public class Tree<E> {
	private Node<E> root;

	public Node<E> getRoot() {
		return root;
	}
	public Tree(Node<E> node){
		this.root = node;
	}
	public Tree(E e){
		this.root = new Node<E>(e);
	}
	public boolean addNode(Node<E> parent,Node<E> child){
		if(parent==null){
			return false;
		}
		parent.getList().add(child);
		return true;
	}
	public void printTree(Node<E> root){
		System.out.println(root.getData());
		for(int i=0;i<root.getList().length();i++){
			printTree(root.getList().getIndex(i+1));
		}	
	}
	public Node<E> getNode(E e){
		return new Node<E>(e);
	}
	class Node<E>{
		private E data;//节点元素 
		private Node<E> parent;//父节点 
		private List<Node<E>> list;//子节点列表
		public Node(E e) {
			this.data = e;
			this.list = new List<Node<E>>();
		}
		public E getData() {
			return data;
		}
		public void setData(E data) {
			this.data = data;
		}
		public Node<E> getParent() {
			return parent;
		}
		public void setParent(Node<E> parent) {
			this.parent = parent;
		}
		public List<Node<E>> getList() {
			return list;
		}
		public void setList(List<Node<E>> list) {
			this.list = list;
		}
		
	}
	
}

