package top.guyueyu.questions.easy;

import java.util.ArrayList;

/*
 * 输入一个链表，从尾到头打印链表每个节点的值
 */
public class ReserveList {
	public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
		//自己写的，好蠢
        ArrayList <Integer> list = new ArrayList<>();
        ListNode t = listNode;
        while(t!=null){//把节点值放到ArrayList里
            list.add(t.val); 
            t = t.next;
        }
        int[]a = new int [list.size()];
        for(int i=0;i<list.size();i++){//把ArrayList的值放到数组里
        	a[i] = list.get(i);
        }
        for(int i=0;i<list.size()/2;i++){//将数组逆转
        	int temp = a[i];
        	a[i] =a[list.size()-i-1];
        	a[list.size()-i-1] =temp;
        }
        ArrayList<Integer> list2 = new ArrayList<>();
        for(int i=0;i<a.length;i++){//将逆转的数值的值放到ArrayList里
        	list2.add(a[i]);
        }
        return list2;
    }
	public ArrayList<Integer> printListFromTailToHead1(ListNode listNode){
		//递归版本
		//本质上仍然是用的栈
		ArrayList<Integer> list = new ArrayList<>();
		if(listNode!=null){
			list = printListFromTailToHead1(listNode.next);
			list.add(listNode.val);
		}
		return list;
	}
	class ListNode {
		  int val;
	      ListNode next = null;
	      ListNode(int val) {
		       this.val = val;
		  }
	}
}
