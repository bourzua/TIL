package com.example.java.day3.Array;

public class ArrayTest {
    public static void main(String[] args) {

        int[] numbers = new int[3];

        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;

        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // 초기화
        int[] numbers2 = new int[] {0, 1, 2};
        int[] numbers3 = {0, 1, 2};

        System.out.println(numbers2.length);
        System.out.println(numbers3.length);

        int[] studentIDs = new int[5];

        for (int i = 0; i < studentIDs.length; i++) {
            System.out.println(studentIDs[i]);
        }
    }
}
