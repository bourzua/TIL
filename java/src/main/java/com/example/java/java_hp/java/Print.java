package com.example.java.java_hp.java;

public class Print {
    public static void main(String[] args) {

        int age = 27;
        System.out.printf("주아의 나이는 %d세입니다.", age);

        System.out.println();

        int month = 10;
        int day = 7;
        System.out.printf("제 생일은 %d월 %d일입니다.", month, day);

        System.out.println();

        double x = 7.0 / 2.0;
        double y = 7 / 2;
        System.out.printf("x = %f, y = %f", x, y);

        String name = "주아";
        String hobby = "산책하기";

        System.out.println();

        System.out.printf("이름: %s\n", name);
        System.out.printf("취미: %s", hobby);

        System.out.println();

        double pi = 3.14159265;
        System.out.printf("%.2f\n", pi);
    }
}
