package com.example.java.java1.methodscope;

public class Main {
    public static void main(String[] args) {

        Knight k1 = new Knight("돈키호테", 30);

        System.out.println("[객체 생성]");
        System.out.printf("     %s\n", k1.toString());

        k1.setHp(k1.getHp() + 30);

        System.out.println("[체력 증가 + 30]");
        System.out.printf("     %s\n", k1.toString());
    }
}

class Knight {
    private String name;
    private int hp;

    public Knight(String name, int hp) {
        this.name = name;
        this.hp = hp;
    }

    public int getHp() {
        return hp;
    }

    public void setHp(int hp) {
        this.hp = hp;
    }

    public String toString() {
        return String.format("Knights { name: %s, hp: %d }", this.name, this.hp);
    }
}
