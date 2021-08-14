package com.example.java.java_hp.oop;

public class CatTest {
    public static void main(String[] args) {

        // 인스턴스
        Cat cat1 = new Cat();
        Cat cat2 = new Cat();

        // 인스턴스 메소드 호출
        cat1.meow();
        cat2.meow();

        cat1.claw();
        cat2.claw();
    }
}

class Cat {
    String name;
    String breeds;
    int age;

    void meow() {
        System.out.println("야옹~");
    }

    void claw() {
        System.out.println("할퀴기!! 슥샥!");
    }
}