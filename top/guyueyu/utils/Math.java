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
		//判断n是否是素数
		for(int i=2;i*i <= n;i++){
			if(n%i==0){
				return false;
			}
		}
		return true;
	}
	public static ArrayList<Integer> Prime(int x){
		//素数筛法
		//返回小于x的所有素数的列表
		boolean[] Mark = new boolean[x+1];//true 则Mark[i]为素数
		ArrayList<Integer> list = new ArrayList<>();
		Mark[0]=Mark[1]=false;
		for(int i=0;i<Mark.length;i++){
			Mark[i]=true;
		}
		for(int i=2; i<=x;i++){
			if(Mark[i]){
				list.add(i);
			}
			for(int j=i*i; j<=x ;j+=i){//筛掉的数有重复，可以优化
				Mark[j] = false;
			}
			/*index为已经得到的素数的个数，即list现在的长度
			 * for(int j=0;j<index && i*list.get[j]<=x;j++){
			 * 		Mark[i*list.get[j]]=false;
			 * 		if(i%list.get[j]==0)break;关键点，如果i是合数，则i已经被筛去，
			 */
		}
		return list;
	}
	public static ArrayList<Integer> getzhiyinshu(int a){
		//质因数分解
		//返回整数a的质因数数组
		ArrayList<Integer>list = new ArrayList<>();
		for(int i=2; i*i<=a; i++){//如果a%i==0 则a%(a/i)==0
			if(a%i==0){
				a/=i;
				list.add(i);
				i--;
			}
		}
		return list;
	}
}
