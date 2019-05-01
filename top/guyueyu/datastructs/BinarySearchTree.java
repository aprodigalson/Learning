package top.guyueyu.datastructs;

public class BinarySearchTree <E extends Comparable<E>> {
	/*
	 * 二叉查找树
	 */
	protected Node<E> root;
	public BinarySearchTree() {
		setRoot(null);
	}
	public BinarySearchTree(E e) {
		setRoot(new Node<E>(e));
	}
	
	public boolean isEmpty(){
		return getRoot() == null;
	}
	public void makeEmpty(){
		root = null;
	}
	public boolean contain(E e){
		return contains(e, getRoot());
	}
	private boolean contains(E e ,Node<E> t){//递归
		//树t是否包含值e;
		if(t==null){
			return false;
		}
		int result = e.compareTo(t.data);
		if(result>0){
			return contains(e, t.right);
		}else if(result<0){
			return contains(e, t.left);
		}else {
			return true;
		}
	}
	private boolean contains(E e){//非递归
		Node<E> node = root;
		while(node!=null){
			int result = e.compareTo(node.data);
			if(result<0){
				node = node.left;
			}else if (result>0) {
				node = node.right;
			}else {
				break;
			}
		}
		return node!=null;
	}
	public void insert(E e){
		setRoot(insert(e,getRoot()));
	}
	private Node<E> insert(E e,Node<E> t){
		if(t==null){
			return new Node<E>(e);
		}
		int result = e.compareTo(t.data);//如果节点值相同，则不处理
		if(result>0){
			t.right = insert(e, t.right);
		}else if (result<0) {
			t.left = insert(e, t.left);
		}
		return t;
	}
	public void remove(E value){
		root = remove(value, root);
	}
	private Node<E> remove(E value,Node<E> node){//地柜
		if(node==null){
			return node;
		}
		int result = value.compareTo(node.data);
		if(result<0){
			node.left = remove(value, node.left);
		}else if (result>0) {
			node.right = remove(value, node.right);
		}else if(node.left!=null && node.right!=null){//要删除的节点就是当前节点
			//如果被删除节点有两个儿子，则将当前节点值用其右子树的最小值代替
			node.data = findMin(node.right).data;
			node = remove(node.data, node.right);
		}else {
			//如果被删除节点有一个或没有儿子
			node = (node.left!=null)?node.left:node.right;
		}
		return node;
	}
	public E findMin(){
		if(root==null){
			System.out.println("空树");
			return null;
		}
		return findMin(root).data;
	}
	private Node<E> findMin(Node<E> node){
		if(node==null){
			return null;
		}else if (node.left==null) {
			return node;
		}
		return findMin(node.left);
	}
	public E findMax(){
		if(root==null){
			System.out.println("空树");
			return null;
		}
		return findMax(root).data;
	}
	private Node<E> findMax(Node<E> node){
		if(node==null){
			return null;
		}else if(node.right==null){
			return node;
		}
		return findMax(node.right);
	}
	public void inorder(){
		inorder(root);
	}
	private void inorder(Node<E> node){//中序遍历
		if(node!=null){
			inorder(node.left);
			System.out.println(node.data);
			inorder(node.right);
		}
	}
	
	public Node<E> getRoot() {
		return root;
	}
	public void setRoot(Node<E> root) {
		this.root = root;
	}
	protected class Node<E extends Comparable<E>> {
		private E data;
		private Node<E> left;
		private Node<E> right;
		public Node(E e) {
			this(e,null,null);
		}
		public Node(E data, Node<E> left, Node<E> right) {
			this.data = data;
			this.left = left;
			this.right = right;
		}
	}
}

