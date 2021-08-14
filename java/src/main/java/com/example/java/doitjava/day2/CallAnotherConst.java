package com.example.java.doitjava.day2;

class Person{

    String name;
    int age;

    // 2. 생성자에서 다른 생성자를 호출
    public Person() {
        //생성자에서 다른 생성자 호출하려면 호출 전에 아무 것도 없어야 함
        this("이름없음", 1);
    }

    // 1. 자신의 메모리를 가리킴
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Person returnSelf(){
        return this;
    }


}

public class CallAnotherConst {
    public static void main(String[] args) {

        Person p1 = new Person();
        System.out.println(p1.name);

        System.out.println(p1.returnSelf());
    }
}
