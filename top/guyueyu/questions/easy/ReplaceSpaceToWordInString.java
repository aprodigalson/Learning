package top.guyueyu.questions.easy;

/*
 * 请实现一个函数，将一个字符串中的空格替换成“%20”。
 * 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
 */
public class ReplaceSpaceToWordInString {
	
	 public String replaceSpace(StringBuffer str) {
		return str.toString().replace(" ", "%20");
	 }
	 public String replaceSpace1(StringBuffer str){
		 //开辟一个新的字符串
		 StringBuffer newStr= new StringBuffer();
		 int i=0;
		 while(i<str.length()){
			 char c = str.charAt(i);
			 if(c!=' '){
				 newStr.append(c);
			 }else {
				newStr.append("%20");
			}
			 i++;
		 }
		 return newStr.toString();
	 }
	 public String replaceSpace2(StringBuffer str){
		 //在原字符串上替换
		 //先计算出空格数目，从后往前替换
		 int count = 0;
		 for(int i=0;i<str.length();i++){
			 if(str.charAt(i)==' '){
				 count++;
			 }
		 }
		 int newLength = str.length()+count*2;
		 int oldIndex = str.length()-1;
		 int newIndex = newLength-1;
		 str.setLength(newLength);
		 for(;newIndex>=0 && oldIndex>=0;oldIndex--){
			 if(str.charAt(oldIndex)==' '){
				 str.setCharAt(newIndex--, '0');
				 str.setCharAt(newIndex--, '2');
				 str.setCharAt(newIndex--, '%');
			 }else {
				str.setCharAt(newIndex--, str.charAt(oldIndex));
			}
		 }
		 return str.toString();
	 }
 	 
}
