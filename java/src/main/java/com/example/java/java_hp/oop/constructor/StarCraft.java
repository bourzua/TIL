package com.example.java.java_hp.oop.constructor;

public class StarCraft {
    public static void main(String[] args) {

        Marine ma = new Marine("레이너", 80);
        Medic me = new Medic("모랄레스", 60, 60);

        ma.stimpack();
        me.heal(ma);
    }
}

class Marine {
    String name;
    int hp;

    Marine(String n, int h) {
        name = n;
        hp = h;
    }
    void stimpack() {
        System.out.printf("[%s]의 스팀팩! HP: %d -> ", name, hp);
        hp -= 10;
        System.out.printf("%d\n", hp);
    }
}

class Medic {
    String name;
    int hp;
    int mp;

    Medic(String n, int h, int m) {
        name = n;
        hp = h;
        mp = m;
    }
    void heal(Marine marine) {
        mp -= 10;
        System.out.printf("[%s]의 치유! => [%s] HP(%d -> ", name, marine.name, marine.hp);
        marine.hp += 10;
        System.out.printf("%d)\n", marine.hp);
    }
}