package top.guyueyu;

import java.util.Random;

import top.guyueyu.datastructs.AVLTree;

public class Main {
	public static void main(String[] args) {
		AVLTree<Integer> avlTree= new AVLTree<>();
		avlTree.insert(1);
		avlTree.insert(2);
		avlTree.insert(4);
		avlTree.insert(5);
		avlTree.insert(6);
		avlTree.insert(7);
		avlTree.inorder();
		
	}

}
