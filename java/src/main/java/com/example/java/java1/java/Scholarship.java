package com.example.java.java1.java;

public class Scholarship {
    public static void main(String[] args) {

        printTest("Park", 100, 92);
        printTest("Kim", 82, 96);
        printTest("Choi", 82, 88);

    }

    public static void printTest(String name, int math, int eng) {
        String result = "";

        if ((math >= 90) && (eng >= 90)) {
            result = "전액 장학금!";
        } else if ((math >= 90) || (eng >= 90)) {
            result = "반액 장학금!";
        } else {
            result = "다음 기회에~";
        }

        System.out.printf("%s => %s\n", name, result);
    }
}
