package com.example.java.day3.Array;

public class TwoDimensionArray {

    public static void main(String[] args) {

//        int[][] arr = new int[2][3];
        int[][] arr = {{1, 2, 3}, {4, 5, 6}};

        // 행
        System.out.println(arr.length);
        // 열
        System.out.println(arr[0].length);

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.println(arr[i][j]);
            }
        }

        char[][] alphabets = new char[13][2];
        char big = 'A';
        char small = 'a';

        for (int i = 0; i < alphabets.length; i++, big++, small++) {
            for (int j = 0; j < alphabets[i].length; j++) {
                if (j == 0){
                    alphabets[i][j] = big;
                }
                else {
                    alphabets[i][j] = small;
                }
            }
        }

        for (int i = 0; i < alphabets.length; i++) {
            for (int j = 0; j < alphabets[i].length; j++) {
                System.out.println(alphabets[i][j]);
            }
        }

    }
}
