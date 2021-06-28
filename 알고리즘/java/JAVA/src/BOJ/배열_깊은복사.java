package BOJ;

import java.util.Arrays;

public class 배열_깊은복사 {
	public static void main(String[] args) {
		
		int[] a = {1, 2, 3, 4};
		int[] b = a.clone();
		
		System.out.println(Arrays.toString(b));
	}

}
