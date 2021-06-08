package BOJ;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class 배열_Set변환 {
	public static void main(String[] args) {
		
		int[] arr = {1, 2, 3, 4, 4, 5, 5};		
		Set<Integer> s = new HashSet<>();
		
		for (int i = 0; i < arr.length; i++) {
			s.add(arr[i]);
		}
		
		System.out.println(s);
		System.out.println(s.size());
	}

}
