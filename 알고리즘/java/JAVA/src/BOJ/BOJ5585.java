package BOJ;

import java.util.Scanner;

public class BOJ5585 {
	public static void main(String[] args) {
		
		int[] coin = {500, 100, 50, 10, 5, 1};
		
		int ans = 0;
		
		Scanner sc = new Scanner(System.in);
		
		int money = 1000 - sc.nextInt();
		
		for (int i = 0; i < coin.length; i++) {
			if (money/coin[i] > 0) {
				ans += money/coin[i];
				money %= coin[i];
			}
		}
		System.out.println(ans);
	}

}
