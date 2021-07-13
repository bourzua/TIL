package com.example.java.day1;

public class ImplicitConversion {
    public static void main(String[] args) {

        byte bNum = 10;
        int num = bNum;

        System.out.println(num);

        long lNum = 10;
        float fNum = lNum;

        System.out.println(fNum);

        double dNum = fNum + num; //fNum + num: float으로 형변환  더하기하면서 double로 형변환

        System.out.println(dNum);
    }
}
