package com.example.java.java_hp.oop;

public class CatTest2 {
    public static void main(String[] args) {

        Cat2 cat1 = new Cat2();
        Cat2 cat2 = new Cat2();

        cat1.name = "네로";
        cat2.name = "나비";

        cat1.meow();
        cat2.meow();

        cat1.claw();
        cat2.claw();

    }
}

class Cat2 {
    String name;
    String breeds;
    int age;

    void meow() {
        System.out.printf("[%s]의 야옹~\n", name);
    }

    void claw() {
        System.out.printf("[%s]의 할퀴기!! 슥샥!\n", name);
    }
}