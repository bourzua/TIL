package com.example.java.java1.gettersetter;

public class PersonTest {
    public static void main(String[] args) {

        Person choi = new Person("주아", "010-4799-0000");

        System.out.printf("이 름: %s\n", choi.getName());
        System.out.printf("연락처: %s\n", choi.getPhonNumber());


    }
}

class Person {

    private String name;
    private String phonNumber;

    public Person(String name, String phonNumber) {
        this.name = name;
        this.phonNumber = phonNumber;
    }

    public String getName() {
        return this.name;
    }

    public String getPhonNumber() {
        return this.phonNumber;
    }
}