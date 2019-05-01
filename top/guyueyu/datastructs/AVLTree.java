package top.guyueyu.datastructs;

import top.guyueyu.utils.Math;

public class AVLTree <E extends Comparable<E>>{
	private static final int ALLOWED_IMBALANCE = 1;
	private Node<E> root;
	public AVLTree(Node<E> node) {
		this.root = node;
	}
	public AVLTree(){
		this.root = null;
	}
	
	/*
	 * 判空
	 */
	public boolean isEmpty(){
		return root==null;
	}
	private Node<E> findMin(Node<E> root){
		if(root!=null){
			while(root.left!=null) {
				root = root.left;
			}
		}
		return root;
	}
	/*
	 * 插入值e
	 */
	public void insert(E e){
		root = insert(root,e);
	} 
	private Node<E> insert(Node<E> root, E e) {
		if(root==null){
			return new Node<E>(e);
		}
		int result = e.compareTo(root.data);
		if(result<0){
			root.left = insert(root.left, e);
		}else if(result>0){
			root.right = insert(root.right, e);
		}
		return balance(root);
	}
	/*
	 * 调节不平衡节点
	 */
	private Node<E> balance(Node<E> root){
		if(root ==null){
			return root;
		}
		if(height(root.left)-height(root.right)>ALLOWED_IMBALANCE){
			if(height(root.left.left)>=height(root.left.right)){
				root = rotateWithLeftChild(root);
			}else {
				root = doubleWithLeftChild(root);
			}
		}else if(height(root.right)-height(root.left)>ALLOWED_IMBALANCE){
			if(height(root.right.right)>=height(root.right.left)){
				root = rotateWithRightChild(root);
			}else {
				root = doubleWithRightChild(root);
			}
		}
		root .height = Math.max(height(root.left), height(root.right))+1;
		return root;
	}
	/*
	 * 左左旋转
	 */
	private Node<E> rotateWithLeftChild(Node<E> k1){
		Node<E> k2 = k1.left;
		k1.left = k2.right;
		k2.right = k1;
		k1.height = Math.max(height(k1.left), height(k1.right))+1;
		k2.height = Math.max(height(k2.left),height(k1))+1;
		return k2;
	}
	/*
	 * 右右旋转
	 */
	private Node<E> rotateWithRightChild(Node<E> k1){
		Node<E> k2= k1.right;
		k1.right = k2.left;
		k2.left = k1;
		k1.height = Math.max(height(k1.left), height(k1.right))+1;
		k2.height = Math.max(height(k2.right), height(k1))+1;
		return k2;
	}
	/*
	 * 左右旋转
	 */
	private Node<E> doubleWithLeftChild(Node<E> k1){
		k1.left = rotateWithRightChild(k1.left);
		return rotateWithLeftChild(k1);
	}
	/*
	 * 右左旋转
	 */
	private Node<E> doubleWithRightChild(Node<E> k1){
		k1.right = rotateWithLeftChild(k1.right);
		return rotateWithRightChild(k1);
	}
	/*
	 * 删除值为e的节点
	 */
	public void remove(E e){
		root = remove(root,e);
	}
	private Node<E> remove(Node<E> root, E e) {
		if(root==null){
			return root;
		}
		int result = e.compareTo(root.data);
		if(result<0){
			root.left = remove(root.left, e);
		}else if (result>0) {
			root.right = remove(root.right, e);
		}else if (root.left!=null&&root.right!=null) {
			root.data = findMin(root.right).data;
			root = remove(root.right,e);
			
		}else {
			root = (root.left!=null)?root.left:root.right;
		}
		return balance(root);
	}
	/*
	 * 节点为根的树的高度
	 */
	private int height(Node<E> n){
		return n==null?-1:n.height;
	}
	/*
	 * 中序遍历
	 */
	public void inorder(){
		inorder(root);
	}
	private void inorder(Node<E> root){
		if(root!=null){
			inorder(root.left);
			System.out.println(root.data+" "+root.height);
			inorder(root.right);
		}
	}
	/*
	 * 节点类
	 */
	private class Node<E extends Comparable<E>> {
		private E data;
		private Node<E> left;
		private Node<E> right;
		private Node<E> parent;
		private int height;
		public Node(E e) {
			this(e,null,null,null,0);
		}
		public Node(E data, Node<E> left, Node<E> right,Node<E> parent,int height) {
			this.data = data;
			this.left = left;
			this.right = right;
			this.parent = parent;
			this.height = height;
		}
	}

}
