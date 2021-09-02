package com.example.java.java2.chapter1.section2;

import java.util.Scanner;

public class Code18_2 {

    public static void main(String[] args) {

        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] data = new int[n];
        for (int i = 0; i < n; i++)
            data[i] = kb.nextInt();
        kb.close();

        bubbleSort(n, data);

        System.out.println("Sorted data: ");
        for (int i=0; i<n; i++)
            System.out.println(data[i]);
    }

    static void bubbleSort(int n, int[] array) {
        for (int i=n-1; i>0; i--) {
            for (int j=0; j<i; j++) {
                if (array[j] > array[j+1]) {
                    // swap data[j] and data[j+1]
                    swap(array[j], array[j+1]);
                }
            }
        }
    }

    // swqp 메서드를 호출하는 순간 data[j]와 data[j+1]의 값이 각각 a와 b에 복사된다. 완전히 별개의 변수이다. => 값에 의한 호출
    static void swap(int a, int b) {
        int tmp = a;
        a = b;
        b = tmp;
    }
}
