package com.example.java.java_hp.java;

public class Type {
    public static void main(String[] args) {

        double a = 2;
        System.out.println(a);

        int b = (int) 10.4;
        System.out.println(b);

        int c = 5 / 2;
        System.out.println(c);

        String strSeven = "7";
        String strPi = "3.14";

        int d = Integer.parseInt(strSeven);
        double e = Double.parseDouble(strPi);

        double f = d + e;

        System.out.printf("%d + %.2f = %.2f", d, e, f);
    }
}
