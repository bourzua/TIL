package com.example.java.java2.chapter1.section1;

public class Code01 {

    static int num;

    public static void main(String[] args) {

        int anotherNum = 5;

        num = 2;

        System.out.println("AnotherNum: " + anotherNum);
        System.out.println("Sum: " + num + anotherNum);     //left associativity
        System.out.println("Sum: " + (num + anotherNum));
    }
}
