package com.example.java.java_hp.oop.constructor;

public class HeroTest {
    public static void main(String[] args) {
        Hero ironMan = new Hero("아이언맨", 80);
        Hero thanos = new Hero("타노스", 160);
        Hero thor = new Hero("토르", 150);
        Hero groot = new Hero("그루트", 40);

        System.out.println(ironMan.toStr());
        System.out.println(thanos.toStr());
        System.out.println(thor.toStr());
        System.out.println(groot.toStr());
    }
}

class Hero {
    String name;
    int hp;

    Hero(String n, int h) {
        name = n;
        hp = h;
    }

    String toStr() {
        return String.format("Hero { name: %s, hp: %d }", name, hp);
    }
}