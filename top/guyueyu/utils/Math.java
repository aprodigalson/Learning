package top.guyueyu.utils;

import java.util.ArrayList;

public class Math{
	public static int min(int a,int b){
		return a<b?a:b;
	}
	public static int max(int a,int b){
		return a>b?a:b;
	}
	public static boolean isPrime(int n){
		//�ж�n�Ƿ�������
		for(int i=2;i*i <= n;i++){
			if(n%i==0){
				return false;
			}
		}
		return true;
	}
	public static ArrayList<Integer> Prime(int x){
		//����ɸ��
		//����С��x�������������б�
		boolean[] Mark = new boolean[x+1];//true ��Mark[i]Ϊ����
		ArrayList<Integer> list = new ArrayList<>();
		Mark[0]=Mark[1]=false;
		for(int i=0;i<Mark.length;i++){
			Mark[i]=true;
		}
		for(int i=2; i<=x;i++){
			if(Mark[i]){
				list.add(i);
			}
			for(int j=i*i; j<=x ;j+=i){//ɸ���������ظ��������Ż�
				Mark[j] = false;
			}
			/*indexΪ�Ѿ��õ��������ĸ�������list���ڵĳ���
			 * for(int j=0;j<index && i*list.get[j]<=x;j++){
			 * 		Mark[i*list.get[j]]=false;
			 * 		if(i%list.get[j]==0)break;�ؼ��㣬���i�Ǻ�������i�Ѿ���ɸȥ��
			 */
		}
		return list;
	}
	public static ArrayList<Integer> getzhiyinshu(int a){
		//�������ֽ�
		//��������a������������
		ArrayList<Integer>list = new ArrayList<>();
		for(int i=2; i*i<=a; i++){//���a%i==0 ��a%(a/i)==0
			if(a%i==0){
				a/=i;
				list.add(i);
				i--;
			}
		}
		return list;
	}
}
