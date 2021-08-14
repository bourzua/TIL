package com.example.java.java_hp.java;

import java.util.Scanner;

public class Circle {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int r = Integer.parseInt(sc.next());

        double S = Math.PI * r * r;

        System.out.printf("반지름이 %d인 원의 넓이 => %.3f", r, S);
    }
}
