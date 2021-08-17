package com.example.java.java1.oop;

public class Main {
    public static void main(String[] args) {

        Dog d = new Dog();

        System.out.printf("이름: %s\n", d.name);
        System.out.printf("품종: %s\n", d.breeds);
        System.out.printf("나이: %d\n", d.age);
    }

}

class Dog {
    String name;
    String breeds;
    int age;

    void wag() {
        System.out.println("살랑살랑 꼬리를 친다!");
    }

    void bark() {
        System.out.println("멍멍! 개가 짖습니다!");
    }
}
