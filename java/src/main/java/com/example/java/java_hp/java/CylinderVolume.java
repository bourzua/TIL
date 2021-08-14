package com.example.java.java_hp.java;

public class CylinderVolume {
    public static void main(String[] args) {

        double r = 7.0;
        double h = 5.0;

        double v = volume(r, h);

        System.out.printf("반지름이 %.1f, 높이가 %.1f인 원기둥의 부피: %.1f", r, h, v);
    }

    public static double volume(double a, double b) {
        return  Math.PI * a * a * b;
    }
}
