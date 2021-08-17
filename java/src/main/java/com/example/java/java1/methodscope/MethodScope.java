package com.example.java.java1.methodscope;

public class MethodScope {
    public static void main(String[] args) {

        // main 메소드의 지역변수 score
        int score = 88;
        System.out.printf("score = %d in main()\n", score);

        // Record 클래스의 메소드 수행
        Record.foo(score);

        System.out.printf("score = %d in main()\n", score);

    }
}

class Record {
    public  static void foo(int score) {

        score -= 10;

        System.out.printf("score = %d in foo()\n", score);
    }
}
