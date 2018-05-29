package top.guyueyu.datastructs;


public class Hash<T>{
	private static int DEFAULT_SIZE = 11;
	private List<T> [] lists;
	private int currentSize;
	public Hash() {
		this(DEFAULT_SIZE);
	}
	public Hash(int size){
		lists = new List[nextPrime(size)];
		for(int i=0; i<lists.length; i++){
			lists[i] = new List<>();
		}
	}
	public void insert(T t){
		List<T> thislist = lists[hash(t)];
		if(!thislist.contains(t)){
			thislist.add(t);
			if(++currentSize>lists.length){
				rehash();
			}
		}
	}
	public void makeEmpty(){
		for(int i=0; i<lists.length; i++){
			lists[i].makeEmpty();
		}
		currentSize = 0;
	}
	public void remove(T t){
		List<T> thislist = lists[hash(t)];
		if(thislist.contains(t)){
			thislist.remove(t);
			currentSize--;
		}
	}
	public void printHash(){
		for(int i=0; i<lists.length; i++){
			List<T> list = lists[i];
			list.printList();
		}
	}
	private void rehash(){
		//有问题。。。。。。。
		//再散列
		List<T>[] oldLists = lists;
		lists = new List[nextPrime(2*lists.length)];
		for(int j=0; j<lists.length; j++){
			lists[j] = new List<>();
		}
		currentSize = 0;
		for(List<T> list:oldLists){
			for(T item:list){
				insert(item);
			}
		}
	}
	private boolean contains(T t){
		List<T> thislist = lists[hash(t)];
		return thislist.contains(t);
	}
	private int hash(T t){
		//获得t在哈希表中的地址
		int hashValue = t.hashCode();
		hashValue %=lists.length;
		if(hashValue<0){
			hashValue+=lists.length;
		}
		return hashValue;
	}
	private static int nextPrime(int n){
		//生成n的下一个素数
		if(n%2==0){
			n++;
		}
		for(;!isPrime(n);n+=2);
		return n;
	}
	private static boolean isPrime(int n){
		//判断一个数是否是素数
		if(n==2 || n==3){
			return true;
		}
		for(int i=2;i*i<n;i++){
			if(n%i==0){
				return false;
			}
		}
		return true;
	}
}
