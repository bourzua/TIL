package com.example.java.doitjava.Chapter10.interfaceex;

// 인터페이스 여러 개 상속 가능 & 모든 추상메서드 구현해야 함
public class MyClass implements MyInterface{
    @Override
    public void myMethod() {
        System.out.println("myMethod()");
    }

    @Override
    public void x() {
        System.out.println("x()");
    }

    @Override
    public void y() {
        System.out.println("y()");
    }

    public static void main(String[] args) {
        MyClass myClass = new MyClass();

        X xClass = myClass;
        xClass.x();
    }
}
