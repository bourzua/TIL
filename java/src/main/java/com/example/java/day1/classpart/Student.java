package com.example.java.day1.classpart;

public class Student {
    int studentID;
    String studentName;
    int grade;
    String address;

    // 생성자가 하나도 없는 경우, 자바컴파일러가 기본 생성자 넣어줌

    public Student() {
    }

    public Student(int studentID, String studentName) {
        this.studentID = studentID;
        this.studentName = studentName;
    }

    public void showStudentInfo() {
        System.out.println(studentName + ", " + address);
    }

    public String getStudentName(){
        return studentName;
    }
    public void setStudentName(String name){
        studentName = name;
    }
}