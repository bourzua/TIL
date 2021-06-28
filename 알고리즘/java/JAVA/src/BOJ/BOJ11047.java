package BOJ;

import java.util.Scanner;

public class BOJ11047 {
	public static void main(String[] args) {
		int ans = 0;
		
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int money = sc.nextInt();
		
		int[] coin = new int[N];
		
		for (int i = 0; i < N; i++) {
			coin[i] = sc.nextInt();
		}
		
		
		for (int i = N-1; i > -1; i--) {
			if (coin[i] <= money) {
				ans += money/coin[i];
				money = money%coin[i];
			}
//			if (money == 0) {
//				break;
//			}
		}
		
		System.out.println(ans);
	}

}
