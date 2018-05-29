package top.guyueyu.questions;

import java.util.ArrayList;

import top.guyueyu.utils.Math;

public class GreatestCommonDivider {
	public static int getGreatestCommonDivider(int a,int b){
		//返回a和b 的最大公因子
		//Euclid's algorithm
		while(b!=0){
			int r = a%b;
			a = b;
			b = r;
		}
		return a;
	}
	public static int get(int a,int b){
		//连续整数检测
		int t = Math.min(a, b);
		while(t>0 && (a%t!=0 || b%t!=0)){
			t--;
		}
		return t;
	}
	

}
