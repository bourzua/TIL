package BOJ;

import java.util.Arrays;

public class 배열_최솟값 {
	public static void main(String[] args) {
		int[] a = {5, 8, 2, 9};
		
		int minValue = a[0];
		
		for (int i = 1; i < a.length; i++) {
			if (minValue > a[i]) {
				minValue = a[i];
			}
		}
		
		System.out.println(minValue);
	}

}
