package com.example.java.java1.java;

public class Pork {
    public static void main(String[] args) {

        int num = 3;

        double result = cal(num);

        System.out.printf("삼겹살 %d인분: %.2f kcal", num, result);

    }

    public static double cal(int a) {
        return a * 180 * 5.179;
    }
}
