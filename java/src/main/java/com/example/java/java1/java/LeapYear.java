package com.example.java.java1.java;

import java.util.Scanner;

public class LeapYear {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int year = Integer.parseInt(sc.next());

        check(year);
    }

    public static void check(int y) {

        boolean isLeap = false;

        if (y % 4 == 0) {
            isLeap = true;
            if (y % 100 == 0) {
                isLeap = false;
                if (y % 1000 == 0) {
                    isLeap = true;
                }
            }
        }

        System.out.printf("%d년은 윤년입니까? %s", y, isLeap);
    }
}
