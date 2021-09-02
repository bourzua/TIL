package com.example.java.java2.chapter1.section2;

import java.util.Scanner;

public class Code16 {

    public static void main(String[] args) {
        Scanner kb = new Scanner(System.in);
        int a = kb.nextInt();
        int b = kb.nextInt();

        int result = power(a, b);
        System.out.println("The result is " + result);

        kb.close();
    }

    static int power( int n, int m )
    {
        int prod = 1;
        for (int i = 0; i<m; i++)
            prod *= n;
        return prod;
    }
}
