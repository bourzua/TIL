package com.example.java.java1.referencestatic;

public class GalaxyTest {
    public static void main(String[] args) {

        Galaxy[] phones = new Galaxy[5];

        for (int i = 0; i < phones.length; i++) {
            phones[i] = new Galaxy();
        }

        for (int i = 0; i < phones.length; i++) {
            phones[i].print();
        }

        System.out.println("=======================");

        System.out.printf("Galaxy 객체의 개수: %d", Galaxy.count);
    }
}

class Galaxy {

    String serialNum;

    // static 붙이면 class 영역으로!
    // 객체 만들 때마다 + 1
    static int count = 0;

    Galaxy() {
        count ++;
        char c = randomAlphabet();
        serialNum = String.format("%c-%d", c, count);
    }

    char randomAlphabet() {
        return (char) ('A' + Math.random() * 26);
    }

    void print() {
        System.out.printf("Galaxy { serialNum: %s }\n", serialNum);
    }

}
