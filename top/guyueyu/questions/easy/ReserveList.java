package top.guyueyu.questions.easy;

import java.util.ArrayList;

/*
 * ����һ��������β��ͷ��ӡ����ÿ���ڵ��ֵ
 */
public class ReserveList {
	public ArrayList<Integer> printListFromTailToHead(ListNode listNode) {
		//�Լ�д�ģ��ô�
        ArrayList <Integer> list = new ArrayList<>();
        ListNode t = listNode;
        while(t!=null){//�ѽڵ�ֵ�ŵ�ArrayList��
            list.add(t.val); 
            t = t.next;
        }
        int[]a = new int [list.size()];
        for(int i=0;i<list.size();i++){//��ArrayList��ֵ�ŵ�������
        	a[i] = list.get(i);
        }
        for(int i=0;i<list.size()/2;i++){//��������ת
        	int temp = a[i];
        	a[i] =a[list.size()-i-1];
        	a[list.size()-i-1] =temp;
        }
        ArrayList<Integer> list2 = new ArrayList<>();
        for(int i=0;i<a.length;i++){//����ת����ֵ��ֵ�ŵ�ArrayList��
        	list2.add(a[i]);
        }
        return list2;
    }
	public ArrayList<Integer> printListFromTailToHead1(ListNode listNode){
		//�ݹ�汾
		//��������Ȼ���õ�ջ
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
