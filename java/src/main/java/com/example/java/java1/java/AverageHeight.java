package com.example.java.java1.java;

public class AverageHeight {
    public static void main(String[] args) {

        test(176.3, true);
        test(162.7, false);
        test(171.8, true);
        test(158.4, false);
    }

    public static void test(double height, boolean isMale) {
        String gender = "";
        String result = "";

        if (isMale) {
            gender = "남";
            if (height >=173.5) {
                result = "평균키 이상";
            }
            else {
                result = "평균키 이하";
            }
        }
        else {
            gender = "여";
            if (height >= 160.8) {
                result = "평균키 이상";
            }
            else {
                result = "평균키 이하";
            }
        }
        System.out.printf("%.1fcm, %s => %s\n", height, gender, result);
    }
}
