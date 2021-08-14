package com.example.java.doitjava.day3.staticex;

public class Student {

    private static int serialNum = 10000;

    int studentID;
    String studentName;

    public Student() {
        serialNum++;
        studentID = serialNum;
    }

    // static 메서드에서 멤버변수 사용할 수 없음
    public static int getSerialNum() {
        return serialNum;
    }
}
