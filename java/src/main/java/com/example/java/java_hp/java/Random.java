package com.example.java.java_hp.java;

public class Random {
    public static void main(String[] args) {

        int x = rollDie();
        System.out.printf("주사위의 눈: %d", x);
    }
    public static int rollDie() {
        double r = 6 * Math.random();
        int temp = (int) r;
        int n = temp + 1;
        return n;
    }
}
