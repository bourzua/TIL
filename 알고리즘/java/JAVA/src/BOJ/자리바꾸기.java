package BOJ;

public class 자리바꾸기 {
	public static void main(String[] args) {
		int a = 3;
		int b = 5;
		
		int temp = a;
		a = b;
		b = temp;
		
		System.out.println(a);
		System.out.println(b);
	}

}
