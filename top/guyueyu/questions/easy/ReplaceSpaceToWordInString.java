package top.guyueyu.questions.easy;

/*
 * ��ʵ��һ����������һ���ַ����еĿո��滻�ɡ�%20����
 * ���磬���ַ���ΪWe Are Happy.�򾭹��滻֮����ַ���ΪWe%20Are%20Happy��
 */
public class ReplaceSpaceToWordInString {
	
	 public String replaceSpace(StringBuffer str) {
		return str.toString().replace(" ", "%20");
	 }
	 public String replaceSpace1(StringBuffer str){
		 //����һ���µ��ַ���
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
		 //��ԭ�ַ������滻
		 //�ȼ�����ո���Ŀ���Ӻ���ǰ�滻
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
