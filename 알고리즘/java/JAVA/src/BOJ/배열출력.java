package BOJ;

import java.util.Arrays;

public class 배열출력 {
	public static void main(String[] args) {
		
		int[] array = {1, 2, 3, 4};		
		int[] temp = Arrays.copyOfRange(array, 1, 3);
		
		System.out.println(Arrays.toString(temp));
	}
}
