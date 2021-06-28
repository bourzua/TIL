package BOJ;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class BOJ11399 {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int ans = 0;
		
		int N = sc.nextInt();
		
		Integer[] arr = new Integer[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.sort(arr, Collections.reverseOrder());
		
		for (int i = 0; i<arr.length; i++) {
			ans += arr[i]*(i+1);
		}
		
		System.out.println(ans);
		
	}

}
