package com.example.java.java1.oop.constructor;

public class HeroTest2 {
    public static void main(String[] args) {

        Hero2 thor = new Hero2("토르", 150);
        Hero2 thanos = new Hero2("타노스", 160);

        thor.punch(thanos);
        thanos.punch(thor);

    }
}

class Hero2 {
    String name;
    int hp;

    Hero2(String s, int i) {
        name = s;
        hp = i;
    }

    void punch(Hero2 enemy) {
        System.out.printf("[%s]의 펀치!!", name);
        System.out.printf(" %s의 HP: %d -> ", enemy.name, enemy.hp);
        enemy.hp -= 10;
        System.out.printf("%d\n", enemy.hp);
    }
}